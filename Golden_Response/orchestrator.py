from typing import Dict, Any

from memory.session_memory import SessionMemory
from memory.context_store import MedicalContextStore

from agents.intake_agent import IntakeAgent
from agents.vision_agent import VisionAgent
from agents.rag_report_agent import RAGReportAgent
from agents.planner_agent import PlannerAgent
from agents.guidance_agent import GuidanceAgent
from agents.safety_agent import SafetyAgent


class MedicalAIOrchestrator:
    """
    Central orchestrator for the Medical AI Assistant.
    Controls agent execution, memory, and safety.
    """

    def __init__(self):
        # Memory layers
        self.session_memory = SessionMemory()
        self.context_store = MedicalContextStore()

        # Agents
        self.intake_agent = IntakeAgent(self.context_store)
        self.vision_agent = VisionAgent(self.context_store)
        self.rag_agent = RAGReportAgent(self.context_store)
        self.planner_agent = PlannerAgent()
        self.guidance_agent = GuidanceAgent(self.context_store)
        self.safety_agent = SafetyAgent()

    # --------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        inputs example:
        {
            "intake": {...},
            "image_path": "data/images/mri.png",
            "reports": [
                {"id": "r1", "text": "...", "source": "report.pdf"}
            ],
            "user_query": "What does the report mention about troponin?"
        }
        """

        # Create new session
        session_id = self.session_memory.create_session()

        # Decide execution plan
        plan = self.planner_agent.plan({
            "intake": inputs.get("intake"),
            "image_path": inputs.get("image_path"),
            "report_uploaded": bool(inputs.get("reports")),
            "user_query": inputs.get("user_query")
        })

        # Execute plan
        for step in plan:

            if step == "intake_agent":
                output = self.intake_agent.execute(inputs["intake"])
                self.session_memory.add_agent_output(session_id, step, output)

            elif step == "vision_agent":
                output = self.vision_agent.execute(inputs["image_path"])
                self.session_memory.update_imaging_findings(session_id, output["findings"])
                self.session_memory.add_agent_output(session_id, step, output)

            elif step == "rag_report_agent":
                # Ingest reports first (one-time per session)
                self.rag_agent.ingest_reports(inputs["reports"])
                output = self.rag_agent.execute(inputs["user_query"])
                self.session_memory.add_rag_report(session_id, output)
                self.session_memory.add_agent_output(session_id, step, output)

            elif step == "guidance_agent":
                output = self.guidance_agent.execute()
                self.session_memory.add_agent_output(session_id, step, output)

            elif step == "safety_agent":
                previous = self.session_memory.get_session(session_id)["agent_outputs"].get(
                    "guidance_agent", {}
                )
                output = self.safety_agent.execute(previous)
                self.session_memory.set_final_response(session_id, output)
                self.session_memory.add_agent_output(session_id, step, output)

        # Final response ONLY from safety agent
        final_session = self.session_memory.get_session(session_id)

        return {
            "session_id": session_id,
            "patient_context": self.context_store.get_context(),
            "imaging_findings": final_session.get("imaging_findings"),
            "uploaded_reports": final_session.get("rag_reports"),
            "final_output": final_session.get("final_response")
        }
