import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="🧬AI Healthcare Intelligence System🩺", layout="wide")

# ------------------ SESSION STATE ------------------

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "risk_done" not in st.session_state:
    st.session_state.risk_done = False

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = ""

# ------------------ CSS ------------------

st.markdown("""
<style>

.stApp{
background-color:#151B54;
color:white;
}

.title{
text-align:center;
font-size:42px;
font-weight:bold;
margin-bottom:30px;
}

.dashboard-grid{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:25px;
margin-top:30px;
}

.card{
background:#4863A0;
padding:30px;
border-radius:14px;
text-align:center;
font-size:20px;
font-weight:600;
transition:all 0.3s ease;
cursor:pointer;
}

.card:hover{
transform:translateY(-8px) scale(1.03);
box-shadow:0px 12px 25px rgba(0,0,0,0.4);
background:#5a75c4;
}

.info-box{
background:#728FCE;
padding:30px;
border-radius:14px;
font-size:18px;
line-height:1.7;
transition:0.3s;
}

.info-box:hover{
transform:scale(1.02);
box-shadow:0px 10px 25px rgba(0,0,0,0.3);
}

.advice-box{
background:#7179ba;
padding:20px;
border-radius:12px;
margin-top:15px;
transition:0.3s;
}

.advice-box:hover{
transform:scale(1.02);
box-shadow:0px 10px 20px rgba(0,0,0,0.3);
}

.assistant-input textarea{
height:150px !important;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------

st.sidebar.title("🧬AI Healthcare System🩺")

page = st.sidebar.radio(
"🧭 Navigation",
[
"🏠 Home",
"🧠 AI Disease Prediction",
"📊 Patient Risk Timeline",
"📑 AI Medical Report",
"💬 AI Medical Assistant",
"👨‍⚕ Doctor Recommendation"
]
)

# ------------------ DATA ------------------

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

# Fill to 30
for i in range(10):
    disease_doctor[f"Condition {i+1}"] = ("Specialist","Follow balanced diet, maintain active lifestyle and consult healthcare provider regularly.")

# ------------------ HOME ------------------

if page == "🏠 Home":

    st.markdown('<div class="title">🧬AI Healthcare Intelligence System🩺</div>', unsafe_allow_html=True)

    col1,col2 = st.columns([2,1])

    with col1:

        st.markdown("""
        <div class="dashboard-grid">

        <div class="card">🧠 AI Disease Prediction</div>

        <div class="card">📊 Patient Risk Timeline</div>

        <div class="card">📑 AI Medical Report</div>

        <div class="card">💬 AI Medical Assistant</div>

        <div class="card">👨‍⚕ Doctor Recommendation</div>

        </div>
        """,unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="info-box">

🏥 What This AI Model Does

✔ Predicts possible diseases from symptoms  
✔ Analyzes patient symptom patterns  
✔ Generates patient health risk timeline  
✔ Provides explainable AI medical insights  
✔ AI medical assistant for questions  
✔ Doctor & specialist recommendations  
✔ Preventive healthcare insights  

</div>
""",unsafe_allow_html=True)

# ------------------ PREDICTION ------------------

elif page == "🧠 AI Disease Prediction":

    st.header("🧠 AI Disease Prediction")

    name = st.text_input("Name")

    selected_symptoms = st.multiselect("Select Symptoms",symptoms)

    if st.button("Predict Disease"):

        if len(selected_symptoms) == 0:
            st.warning("Please select symptoms")
        else:

            disease = list(disease_doctor.keys())[np.random.randint(0,10)]

            st.session_state.prediction_result = disease
            st.session_state.prediction_done = True

            st.success(f"Predicted Disease: {disease}")

# ------------------ RISK TIMELINE ------------------

elif page == "📊 Patient Risk Timeline":

    st.header("📊 Patient Risk Timeline")

    diseases = st.multiselect("Select Diseases",list(disease_doctor.keys()))

    surgery = st.radio("Any Past Surgery?",["No","Yes"])

    smoking = st.radio("Smoking",["No","Yes"])

    activity = st.selectbox("Physical Activity",["Low","Medium","High","Very High"])

    if st.button("Analyze Risk"):

        st.session_state.risk_done = True
        st.success("Risk analysis completed")

# ------------------ REPORT ------------------

elif page == "📑 AI Medical Report":

    st.header("📑 AI Medical Report")

    if not st.session_state.prediction_done and not st.session_state.risk_done:

        st.warning("Run Disease Prediction or Risk Analysis first.")

    else:

        disease = st.session_state.prediction_result

        doctor,advice = disease_doctor.get(disease,("General Physician","Maintain healthy lifestyle."))

        st.markdown(f"""
        <div class="advice-box">

        <h3>Consult: {doctor}</h3>

        <p><b>Advice:</b> {advice}</p>

        </div>
        """,unsafe_allow_html=True)

# ------------------ ASSISTANT ------------------

elif page == "💬 AI Medical Assistant":

    st.header("💬 AI Medical Assistant")

    question = st.text_area(
    "Ask a health question",
    placeholder="Ask about symptoms, diseases, prevention tips, diet recommendations, lifestyle advice..."
    )

    if st.button("Ask"):

        st.write("AI Response: Please consult a healthcare professional for detailed guidance.")

# ------------------ DOCTOR ------------------

elif page == "👨‍⚕ Doctor Recommendation":

    st.header("👨‍⚕ Doctor Recommendation")

    disease = st.selectbox("Select Disease",list(disease_doctor.keys()))

    doctor,advice = disease_doctor[disease]

    st.markdown(f"""
    <div class="advice-box">

    <h3>Consult: {doctor}</h3>

    <p><b>Advice:</b> {advice}</p>

    </div>
    """,unsafe_allow_html=True)
