import streamlit as st
import requests
import json
import os
import tempfile

API_URL = "http://127.0.0.1:5000/analyze"

st.set_page_config(
    page_title="Medical AI Assistant",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    # 🏥 Medical AI Assistant  
    **GenAI + Agentic AI | Vision + RAG | Safety-First**
    """
)

st.warning(
    "⚠️ This system provides **general medical guidance only**. "
    "It does NOT provide diagnosis or treatment. "
    "Always consult a qualified healthcare professional."
)

# --------------------------------------------------
# SIDEBAR – PATIENT INTAKE
# --------------------------------------------------

st.sidebar.header("👤 Patient Intake")

age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=40)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
symptoms = st.sidebar.text_area(
    "Symptoms (comma separated)",
    placeholder="e.g. chest discomfort, headache"
)
medications = st.sidebar.text_area(
    "Current Medications",
    placeholder="e.g. aspirin, metformin"
)
allergies = st.sidebar.text_area(
    "Allergies",
    placeholder="e.g. penicillin"
)

vitals_col1, vitals_col2 = st.sidebar.columns(2)
heart_rate = vitals_col1.number_input("Heart Rate", min_value=0, value=72)
blood_pressure = vitals_col2.text_input("Blood Pressure", value="120/80")

intake_data = {
    "demographics": {
        "age": age,
        "gender": gender
    },
    "symptoms": [s.strip() for s in symptoms.split(",") if s.strip()],
    "medications": [m.strip() for m in medications.split(",") if m.strip()],
    "allergies": [a.strip() for a in allergies.split(",") if a.strip()],
    "vitals": {
        "heart_rate": heart_rate,
        "blood_pressure": blood_pressure
    }
}

# --------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------

st.subheader("📤 Upload Medical Data")

col1, col2 = st.columns(2)

with col1:
    image_file = st.file_uploader(
        "Upload MRI / X-ray / Scan Image",
        type=["png", "jpg", "jpeg"]
    )

with col2:
    report_file = st.file_uploader(
        "Upload Medical Report (PDF)",
        type=["pdf"]
    )

user_query = st.text_input(
    "Ask a question about the uploaded report (optional)",
    placeholder="e.g. What does the report mention about troponin?"
)

# --------------------------------------------------
# SUBMIT
# --------------------------------------------------

if st.button("🧠 Run Medical AI Analysis", type="primary"):

    with st.spinner("Running medical AI pipeline..."):

        image_path = None
        reports_payload = []

        # Handle image
        if image_file:
            tmp_img = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            tmp_img.write(image_file.read())
            tmp_img.close()
            image_path = tmp_img.name

        # Handle PDF
        if report_file:
            import fitz
            doc = fitz.open(stream=report_file.read(), filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()

            reports_payload.append({
                "id": "report_1",
                "text": text,
                "source": report_file.name
            })

        payload = {
            "intake": intake_data,
            "image_path": image_path,
            "reports": reports_payload,
            "user_query": user_query
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code != 200:
            st.error("❌ Backend error occurred.")
        else:
            result = response.json()["data"]

            st.success("✅ Analysis completed safely.")

            # --------------------------------------------------
            # RESULTS
            # --------------------------------------------------

            st.subheader("🧠 AI Medical Guidance")
            st.markdown(result["final_output"]["final_output"])

            with st.expander("📊 Structured Medical Context"):
                st.json(result["patient_context"])

            if result.get("imaging_findings"):
                with st.expander("🖼 Imaging Observations"):
                    st.json(result["imaging_findings"])

            if result.get("uploaded_reports"):
                with st.expander("📄 Report-Based Answers (RAG)"):
                    st.json(result["uploaded_reports"])
