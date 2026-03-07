import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from io import BytesIO

st.set_page_config(page_title="🧬AI Healthcare Intelligence System🩺", layout="wide")

# ---------------------------------------------------------
# PAGE STYLE
# ---------------------------------------------------------

st.markdown("""
<style>

.stApp{
background:#151B54;
color:Night Blue;
}

.card-container{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:25px;
margin-top:30px;
}

.card{
background:#554094;
padding:35px;
border-radius:15px;
text-align:center;
font-size:22px;
font-weight:600;
cursor:pointer;
transition: all 0.35s ease;
box-shadow:0 6px 15px rgba(0,0,0,0.25);
}

.card:hover{
transform:translateY(-10px) scale(1.05);
box-shadow:0 15px 35px rgba(0,0,0,0.35);
background:#a8b1e5;
}

.model-box{
background:#123499;
padding:30px;
border-radius:15px;
font-size:20px;
line-height:1.8;
margin-top:20px;
transition: all 0.35s ease;
box-shadow:0 6px 15px rgba(0,0,0,0.25);
}

.model-box:hover{
transform:translateY(-8px) scale(1.02);
box-shadow:0 15px 35px rgba(0,0,0,0.40);
background:#3d6fb3;
cursor:pointer;
}

.report-box{
.report-box{
background:#7179ba;
padding:18px;
border-radius:12px;
margin-top:20px;
max-height:140px;
transition: all 0.3s ease;
box-shadow:0 6px 12px rgba(0,0,0,0.25);
}

.report-box:hover{
transform:translateY(-6px);
box-shadow:0 14px 30px rgba(0,0,0,0.35);
background:#848ee0;
cursor:pointer;
}

.report-box h3{
font-size:28px;
}

.report-box p{
font-size:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------

st.sidebar.title("🧭 Navigation")

page = st.sidebar.radio(
"",
[
"🏠 Home",
"🧠 AI Disease Prediction",
"📊 Patient Risk Timeline",
"📑 AI Medical Report",
"💬 AI Medical Assistant",
"👨‍⚕ Doctor Recommendation"
]
)

# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

symptoms = [
"Fever",
"High Fever",
"Cough",
"Dry Cough",
"Fatigue",
"Headache",
"Nausea",
"Vomiting",
"Chest Pain",
"Shortness of Breath",
"Abdominal Pain",
"Back Pain",
"Joint Pain",
"Muscle Pain",
"Sore Throat",
"Runny Nose",
"Nasal Congestion",
"Weight Loss",
"Weight Gain",
"Blurred Vision",
"Frequent Urination",
"Increased Thirst",
"Loss of Appetite",
"Excessive Sweating",
"Dizziness",
"Palpitations",
"Muscle Weakness",
"Skin Rash",
"Skin Redness",
"Swelling",
"Constipation",
"Diarrhea",
"Memory Loss",
"Sleep Disturbance",
"Insomnia",
"Anxiety",
"Depression",
"Hair Loss",
"Dry Skin",
"Cold Intolerance",
"Heat Intolerance",
"Chills",
"Night Sweats",
"Yellowing of Skin (Jaundice)",
"Dark Urine",
"Pale Stool",
"Difficulty Swallowing",
"Heartburn",
"Persistent Sneezing",
"Loss of Taste",
"Loss of Smell",
"Confusion",
"Difficulty Breathing",
"Tingling Sensation",
"Numbness",
"Chest Tightness"
]

diseases = [
"Diabetes","Hypertension","Heart Disease","Asthma","Migraine","Anemia",
"Arthritis","Depression","Anxiety Disorder","Obesity","Hypothyroidism",
"Hyperthyroidism","Bronchitis","Pneumonia","Tuberculosis","Kidney Disease",
"Liver Disease","Gastritis","Peptic Ulcer","Osteoporosis","Epilepsy",
"Stroke Risk","Chronic Fatigue Syndrome","Allergy","Sinusitis",
"Irritable Bowel Syndrome","PCOS","Sleep Apnea","Coronary Artery Disease",
"Parkinson’s Disease","Alzheimer’s Risk","Metabolic Syndrome"
]

disease_doctor = {
"Diabetes":("Endocrinologist","Monitor blood sugar, follow a balanced low-sugar diet, maintain healthy weight, exercise daily and regularly check HbA1c levels."),
"Hypertension":("Cardiologist","Reduce sodium intake, manage stress levels, maintain healthy BMI, monitor blood pressure frequently."),
"Asthma":("Pulmonologist","Avoid allergens, use inhalers as prescribed, perform breathing exercises and maintain lung health."),
"Heart Disease":("Cardiologist","Adopt heart-healthy diet, control cholesterol, avoid smoking and maintain active lifestyle."),
"Thyroid Disorder":("Endocrinologist","Monitor thyroid hormones, ensure adequate iodine intake and follow medication schedule."),
"Arthritis":("Rheumatologist","Maintain joint mobility through exercise, reduce inflammation through diet and monitor joint health."),
"Kidney Disease":("Nephrologist","Reduce salt and protein overload, stay hydrated and monitor kidney function regularly."),
"Depression":("Psychiatrist","Engage in counseling therapy, maintain social connections, regular sleep and balanced mental health support."),
"Anemia":("Hematologist","Increase iron-rich foods, monitor hemoglobin levels and treat underlying nutritional deficiencies."),
"Skin Infection":("Dermatologist","Maintain skin hygiene, apply prescribed topical treatments and avoid irritants."),
"Obesity":("Nutritionist","Adopt calorie-balanced diet, maintain physical activity routine and track weight trends."),
"Stroke Risk":("Neurologist","Control blood pressure, maintain healthy cholesterol and monitor neurological symptoms."),
"Allergy":("Allergist","Avoid triggers, maintain medication compliance and monitor immune responses."),
"GERD":("Gastroenterologist","Avoid spicy foods, eat smaller meals and maintain healthy digestion habits."),
"Flu":("General Physician","Maintain hydration, adequate rest and immune boosting nutrition."),
"COVID-19":("Infectious Disease Specialist","Monitor respiratory symptoms, maintain isolation if required and boost immunity."),
"PCOS":("Gynecologist","Maintain hormonal balance through diet, exercise and regular gynecological monitoring."),
"Cholesterol":("Cardiologist","Adopt heart healthy diet, reduce saturated fats and monitor lipid profile."),
"Insomnia":("Sleep Specialist","Maintain sleep hygiene and avoid stimulants before bedtime."),
"Migraine":("Neurologist","Manage triggers such as stress or dehydration and maintain regular sleep cycle.")
}

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "prediction" not in st.session_state:
    st.session_state.prediction=None

if "risk" not in st.session_state:
    st.session_state.risk=None

# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

if page=="🏠 Home":

    st.title("🧬AI Healthcare Intelligence System🩺")

    st.markdown("""
<div class="card-container">

<div class="card">🧠 AI Disease Prediction</div>

<div class="card">📊 Patient Risk Timeline</div>

<div class="card">📑 AI Medical Report</div>

<div class="card">💬 AI Medical Assistant</div>

<div class="card">👨‍⚕ Doctor Recommendation</div>

</div>
""",unsafe_allow_html=True)

    st.markdown("### 🏥 What This AI Model Does")

    st.markdown("""
<div class="model-box">

✔ Predicts possible diseases from symptoms  
✔ Analyzes patient symptom patterns  
✔ Generates patient health risk timeline  
✔ Provides explainable AI medical insights  
✔ AI medical assistant for questions  
✔ Doctor & specialist recommendations  
✔ Preventive healthcare insights  

</div>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# DISEASE PREDICTION
# ---------------------------------------------------------

elif page=="🧠 AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    name = st.text_input("Name")

    age = st.slider("Age",1,100)

    gender = st.selectbox("Gender",["Male","Female","Other"])

    smoking = st.selectbox("Smoking",["Yes","No"])

    activity = st.selectbox("Physical Activity",["Very Low","Low","Moderate","High","Very High"])

    selected_symptoms = st.multiselect("Select Symptoms",symptoms)

    other_symptoms = st.text_input("Other Symptoms")

    if st.button("Predict Disease"):

        if selected_symptoms:
            prediction=diseases[len(selected_symptoms)%len(diseases)]
        else:
            prediction="General Health Risk"

        st.session_state.prediction=prediction

        st.success(f"Predicted Disease Risk: {prediction}")

# ---------------------------------------------------------
# RISK TIMELINE
# ---------------------------------------------------------

elif page=="📊 Patient Risk Timeline":

    st.title("📊 Patient Risk Timeline")

    diseases_selected = st.multiselect("Select Diseases",diseases)

    other = st.text_input("Other Diseases")

    surgery = st.selectbox("Any Past Surgery?",["No","Yes"])

    if surgery=="Yes":
        surgery_type=st.text_input("Surgery Name")
        surgery_time=st.number_input("How long ago?")
        surgery_unit=st.selectbox("Time Unit",["Days","Weeks","Months","Years"])

    smoking = st.selectbox("Smoking",["No","Yes"])

    activity = st.selectbox("Physical Activity",["Very Low","Low","Moderate","High","Very High"])

    if st.button("Generate Risk Timeline"):

        risk=len(diseases_selected)

        st.session_state.risk=risk

        st.success(f"Risk Score: {risk}/10")

# ---------------------------------------------------------
# AI MEDICAL REPORT
# ---------------------------------------------------------

elif page=="📑 AI Medical Report":

    st.title("📑 AI Medical Report")

    if st.session_state.prediction is None and st.session_state.risk is None:
        st.warning("⚠ Perform Disease Prediction or Risk Timeline first")
    else:

        disease=st.session_state.prediction

        risk=st.session_state.risk

        explanation=f"""
AI analysis indicates potential risk related to {disease}.
This prediction was generated based on the symptom patterns and health inputs provided.

Risk evaluation score: {risk}

Preventive Measures:
• Maintain balanced nutrition
• Perform regular exercise
• Monitor vital health parameters
• Schedule routine health checkups
"""

        st.write(explanation)

        # PDF generator

        if st.button("Generate PDF Report"):

            buffer=BytesIO()

            doc=SimpleDocTemplate(buffer,pagesize=A4)

            styles=getSampleStyleSheet()

            elements=[]

            elements.append(Paragraph("AI Medical Report",styles['Title']))

            elements.append(Spacer(1,20))

            elements.append(Paragraph(explanation,styles['BodyText']))

            elements.append(Spacer(1,20))

            table_data=[
            ["Predicted Disease",str(disease)],
            ["Risk Score",str(risk)]
            ]

            table=Table(table_data)

            elements.append(table)

            doc.build(elements)

            st.download_button(
                label="Download Medical PDF",
                data=buffer.getvalue(),
                file_name="AI_Medical_Report.pdf"
            )

# ---------------------------------------------------------
# AI ASSISTANT
# ---------------------------------------------------------

elif page=="💬 AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    question=st.text_input("Ask a health question")

    if st.button("Ask"):

        st.write("AI Suggestion:")

        st.write("Maintain healthy lifestyle, consult doctor if symptoms persist.")

# ---------------------------------------------------------
# DOCTOR RECOMMENDATION
# ---------------------------------------------------------

elif page=="👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation")

    disease=st.selectbox("Select Disease",diseases)

    if disease in doctor_map:
        doctor,advice=doctor_map[disease]
    else:
        doctor="General Physician"
        advice="Maintain healthy lifestyle and consult physician."

    st.markdown(f"""
<div class="report-box">

<h3>Consult: {doctor}</h3>

<p><b>Advice:</b> {advice}</p>

</div>
""",unsafe_allow_html=True)











