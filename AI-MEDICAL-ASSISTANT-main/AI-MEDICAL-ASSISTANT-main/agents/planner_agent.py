from typing import Dict, Any, List
from llm.prompts import PLANNER_PROMPT


class PlannerAgent:
    """
    Agentic Planner

    Responsibilities:
    - Decide which agents to run
    - Enforce execution order
    - NEVER generate medical content
    """

    def __init__(self):
        pass

    def plan(self, inputs: Dict[str, Any]) -> List[str]:
        """
        Decide agent execution order based on available inputs.

        inputs example:
        {
            "intake": {...},
            "image_path": "data/images/scan.png",
            "report_uploaded": True,
            "user_query": "..."
        }
        """

        plan = []

        # Intake is ALWAYS first if provided
        if inputs.get("intake"):
            plan.append("intake_agent")

        # Vision only if image exists
        if inputs.get("image_path"):
            plan.append("vision_agent")

        # RAG only if reports exist AND user asked something
        if inputs.get("report_uploaded") and inputs.get("user_query"):
            plan.append("rag_report_agent")

        # Guidance is generated after data is gathered
        plan.append("guidance_agent")

        # Safety agent ALWAYS runs last
        plan.append("safety_agent")

        return plan
