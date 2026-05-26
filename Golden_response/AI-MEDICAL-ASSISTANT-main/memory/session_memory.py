from typing import Dict, Any
import uuid
import datetime


class SessionMemory:
    """
    Per-session memory store.
    Each patient interaction gets a unique session.
    """

    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------
    # SESSION MANAGEMENT
    # --------------------------------------------------

    def create_session(self) -> str:
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            "created_at": datetime.datetime.utcnow().isoformat(),
            "patient_context": {},
            "imaging_findings": None,
            "rag_reports": [],
            "agent_outputs": {},
            "final_response": None
        }
        return session_id

    def get_session(self, session_id: str) -> Dict[str, Any]:
        return self.sessions.get(session_id, {})

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

    # --------------------------------------------------
    # CONTEXT UPDATES
    # --------------------------------------------------

    def update_patient_context(self, session_id: str, context: Dict[str, Any]):
        self._ensure_session(session_id)
        self.sessions[session_id]["patient_context"] = context

    def update_imaging_findings(self, session_id: str, findings: Dict[str, Any]):
        self._ensure_session(session_id)
        self.sessions[session_id]["imaging_findings"] = findings

    def add_rag_report(self, session_id: str, report: Dict[str, Any]):
        self._ensure_session(session_id)
        self.sessions[session_id]["rag_reports"].append(report)

    def add_agent_output(self, session_id: str, agent_name: str, output: Any):
        self._ensure_session(session_id)
        self.sessions[session_id]["agent_outputs"][agent_name] = output

    def set_final_response(self, session_id: str, response: str):
        self._ensure_session(session_id)
        self.sessions[session_id]["final_response"] = response

    # --------------------------------------------------
    # INTERNAL
    # --------------------------------------------------

    def _ensure_session(self, session_id: str):
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist")
