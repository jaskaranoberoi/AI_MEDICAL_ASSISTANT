from typing import Dict, Any
from memory.context_store import MedicalContextStore


class IntakeAgent:
    """
    Patient Intake Agent

    - Structures patient-provided information
    - Builds clean medical context
    - NO diagnosis
    - NO interpretation
    """

    def __init__(self, context_store: MedicalContextStore):
        self.context_store = context_store

    def execute(self, intake_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        intake_data example:
        {
            "demographics": {...},
            "symptoms": [...],
            "medications": [...],
            "allergies": [...],
            "vitals": {...}
        }
        """

        demographics = intake_data.get("demographics", {})
        symptoms = intake_data.get("symptoms", [])
        medications = intake_data.get("medications", [])
        allergies = intake_data.get("allergies", [])
        vitals = intake_data.get("vitals", {})

        # Update structured medical context
        self.context_store.update_demographics(demographics)
        self.context_store.update_symptoms(symptoms)
        self.context_store.update_medications(medications)
        self.context_store.update_allergies(allergies)
        self.context_store.update_vitals(vitals)

        structured_context = {
            "demographics": demographics,
            "symptoms": symptoms,
            "medications": medications,
            "allergies": allergies,
            "vitals": vitals
        }

        return {
            "status": "success",
            "message": "Patient intake data structured successfully.",
            "context": structured_context
        }
