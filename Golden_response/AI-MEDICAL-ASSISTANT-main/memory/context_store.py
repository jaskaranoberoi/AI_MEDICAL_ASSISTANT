from typing import Dict, Any


class MedicalContextStore:
    """
    Stores structured, non-diagnostic medical context
    aggregated from multiple agents.
    """

    def __init__(self):
        self.context: Dict[str, Any] = {
            "demographics": {},
            "symptoms": [],
            "medications": [],
            "allergies": [],
            "vitals": {},
            "imaging": None,
            "reports": [],
        }

    # --------------------------------------------------
    # UPDATE METHODS
    # --------------------------------------------------

    def update_demographics(self, data: Dict[str, Any]):
        self.context["demographics"] = data

    def update_symptoms(self, symptoms: list):
        self.context["symptoms"] = symptoms

    def update_medications(self, medications: list):
        self.context["medications"] = medications

    def update_allergies(self, allergies: list):
        self.context["allergies"] = allergies

    def update_vitals(self, vitals: Dict[str, Any]):
        self.context["vitals"] = vitals

    def update_imaging(self, imaging_findings: Dict[str, Any]):
        self.context["imaging"] = imaging_findings

    def add_report_summary(self, report_summary: Dict[str, Any]):
        self.context["reports"].append(report_summary)

    # --------------------------------------------------
    # ACCESS
    # --------------------------------------------------

    def get_context(self) -> Dict[str, Any]:
        """
        Returns the full structured medical context.
        """
        return self.context
