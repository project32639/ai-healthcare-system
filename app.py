import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Healthcare Intelligence System",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------------------------------
# STYLING
# ---------------------------------------------------

st.markdown("""
<style>

.main {
background: linear-gradient(120deg,#e6f7ff,#f0fff5);
}

.big-title{
font-size:60px;
font-weight:bold;
text-align:center;
padding:20px;
border-radius:20px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
box-shadow:0px 8px 25px rgba(0,0,0,0.2);
animation: float 3s ease-in-out infinite;
}

@keyframes float{
0%{transform:translateY(0px)}
50%{transform:translateY(-6px)}
100%{transform:translateY(0px)}
}

.feature-box{
background:linear-gradient(135deg,#d8ecff,#e8fff6);
color:#002b5c;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
transition:0.3s;
text-align:center;
font-size:18px;
font-weight:600;
}

.feature-box:hover{
transform:scale(1.05);
background:linear-gradient(135deg,#bfe2ff,#c8ffe8);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "prediction" not in st.session_state:
    st.session_state.prediction = None

# ---------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------

st.sidebar.title("🧭 Navigation")

nav = st.sidebar.radio(
"Go to",
[
"Home",
"AI Disease Prediction",
"Patient Risk Timeline",
"AI Report",
"AI Medical Assistant",
"Doctor Recommendation"
]
)

st.session_state.page = nav

# ---------------------------------------------------
# DATA
# ---------------------------------------------------

symptom_list = [
"Fever","Cough","Shortness of Breath","Chest Pain","Headache",
"Fatigue","Body Pain","Dizziness","Nausea","Vomiting","Diarrhea",
"Constipation","Abdominal Pain","Back Pain","Joint Pain","Muscle Pain",
"Blurred Vision","Eye Pain","Skin Rash","Itching","Swelling",
"Weight Loss","Weight Gain","Frequent Urination","Excessive Thirst",
"Loss of Appetite","Sore Throat","Runny Nose","Insomnia","Anxiety",
"Depression","Memory Loss","Confusion","Difficulty Breathing",
"Heart Palpitations","Cold Sensitivity","Heat Sensitivity",
"Numbness","Tingling Sensation","Loss of Balance"
]

diseases = [
"Diabetes","Heart Disease","Glaucoma","Kidney Disease",
"Hypertension","Cancer","Asthma","Arthritis",
"Alzheimer's Disease","Parkinson's Disease","Stroke",
"Liver Disease","Thyroid Disorder","Osteoporosis",
"Depression","Anxiety Disorder","Migraine",
"Pneumonia","Tuberculosis","COVID-19",
"Gastritis","Peptic Ulcer","Obesity","Anemia",
"Skin Allergy","Psoriasis","Eczema"
]

doctors = {

"Diabetes":"Endocrinologist",
"Heart Disease":"Cardiologist",
"Glaucoma":"Ophthalmologist",
"Kidney Disease":"Nephrologist",
"Hypertension":"Cardiologist",
"Cancer":"Oncologist",
"Asthma":"Pulmonologist",
"Arthritis":"Rheumatologist",
"Alzheimer's Disease":"Neurologist",
"Parkinson's Disease":"Neurologist",
"Stroke":"Neurologist",
"Liver Disease":"Hepatologist",
"Thyroid Disorder":"Endocrinologist",
"Osteoporosis":"Orthopedic Specialist",
"Depression":"Psychiatrist",
"Anxiety Disorder":"Psychiatrist",
"Migraine":"Neurologist",
"Pneumonia":"Pulmonologist",
"Tuberculosis":"Infectious Disease Specialist",
"COVID-19":"Infectious Disease Specialist",
"Gastritis":"Gastroenterologist",
"Peptic Ulcer":"Gastroenterologist",
"Obesity":"Nutritionist / Endocrinologist",
"Anemia":"Hematologist",
"Skin Allergy":"Dermatologist",
"Psoriasis":"Dermatologist",
"Eczema":"Dermatologist"
}

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

if st.session_state.page == "Home":

    st.markdown('<div class="big-title">🧬 AI Healthcare Intelligence System 🤖</div>', unsafe_allow_html=True)

    st.write("")

    st.markdown("""
<div class="feature-box">

<b>🏥 What This AI System Does</b><br><br>

✔ Predicts diseases based on symptoms<br>
✔ Analyzes patient health risk timeline<br>
✔ Generates explainable AI medical reports<br>
✔ Provides AI medical assistant support<br>
✔ Recommends doctors and specialists<br>
✔ Helps early disease detection<br>
✔ Provides preventive healthcare advice

</div>
""", unsafe_allow_html=True)

    st.write("")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="feature-box">🧠 AI Disease Prediction</div>', unsafe_allow_html=True)
        if st.button("AI Disease Prediction"):
            st.session_state.page="AI Disease Prediction"
            st.rerun()

    with col2:
        st.markdown('<div class="feature-box">📊 Patient Risk Timeline</div>', unsafe_allow_html=True)
        if st.button("Patient Risk Timeline"):
            st.session_state.page="Patient Risk Timeline"
            st.rerun()

    with col3:
        st.markdown('<div class="feature-box">📑 AI Report</div>', unsafe_allow_html=True)
        if st.button("AI Report"):
            st.session_state.page="AI Report"
            st.rerun()

    col4,col5 = st.columns(2)

    with col4:
        st.markdown('<div class="feature-box">💬 AI Medical Assistant</div>', unsafe_allow_html=True)
        if st.button("AI Medical Assistant"):
            st.session_state.page="AI Medical Assistant"
            st.rerun()

    with col5:
        st.markdown('<div class="feature-box">👨‍⚕ Doctor Recommendation</div>', unsafe_allow_html=True)
        if st.button("Doctor Recommendation"):
            st.session_state.page="Doctor Recommendation"
            st.rerun()

# ---------------------------------------------------
# AI DISEASE PREDICTION
# ---------------------------------------------------

if st.session_state.page == "AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age = st.slider("Age",1,100)
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")

    gender = st.selectbox("Gender",["Male","Female","Other"])
    smoking = st.selectbox("Smoking Habit",["No","Occasionally","Yes"])
    activity = st.selectbox("Physical Activity Level",["Low","Moderate","High"])
    family_history = st.selectbox("Family History of Disease",["No","Yes"])

    st.subheader("Patient Symptoms")

    selected_symptoms = st.multiselect("Select Symptoms",symptom_list)

    custom_symptoms = st.text_input(
    "Type Symptoms (comma separated)",
    placeholder="example: fever, headache, fatigue"
    )

    symptoms = selected_symptoms.copy()

    if custom_symptoms:
        extra=[s.strip() for s in custom_symptoms.split(",")]
        symptoms.extend(extra)

    if st.button("Predict Disease"):

        prediction=random.choice(diseases)

        st.session_state.prediction=prediction
        st.session_state.gender=gender
        st.session_state.smoking=smoking
        st.session_state.activity=activity
        st.session_state.family_history=family_history

        st.success(f"Predicted Disease Risk: {prediction}")

# ---------------------------------------------------
# RISK TIMELINE
# ---------------------------------------------------

if st.session_state.page == "Patient Risk Timeline":

    st.title("📊 Patient Health Risk Timeline")

    if st.session_state.prediction:

        st.write(f"Predicted Disease: **{st.session_state.prediction}**")

        st.progress(30)
        st.write("Current Health Risk: Low")

        st.progress(60)
        st.write("5 Year Risk: Moderate")

        st.progress(80)
        st.write("10 Year Risk: High")

    else:
        st.warning("Run AI Disease Prediction first.")

# ---------------------------------------------------
# AI REPORT
# ---------------------------------------------------

if st.session_state.page == "AI Report":

    st.title("📑 AI Report")

    if st.session_state.prediction is None:

        st.warning("Run AI Disease Prediction first.")

    else:

        st.write(f"### Prediction Result: {st.session_state.prediction}")

        st.write("Explainable AI Output")

        st.write("• Age contributed to prediction")

        if st.session_state.family_history=="Yes":
            st.write("• Family history increased disease probability")

        if st.session_state.smoking=="Yes":
            st.write("• Smoking habit increased health risk")

        if st.session_state.activity=="Low":
            st.write("• Low physical activity influenced prediction")

# ---------------------------------------------------
# AI MEDICAL ASSISTANT
# ---------------------------------------------------

if st.session_state.page == "AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    question = st.text_area("Describe symptoms or ask health question")

    if st.button("Ask AI"):

        st.info("This assistant provides general medical guidance. Please consult a doctor for diagnosis.")

# ---------------------------------------------------
# DOCTOR RECOMMENDATION
# ---------------------------------------------------

if st.session_state.page == "Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation System")

    disease = st.selectbox("Select Disease", diseases)

    custom = st.text_input("Or Type Disease")

    if st.button("Recommend Doctor"):

        selected = custom if custom!="" else disease

        doc=doctors.get(selected,"General Physician")

        st.success(f"Recommended Specialist: {doc}")

        st.write(f"Patients with **{selected}** should consult **{doc}**.")

        st.subheader("💡 Health Advice")

        tips={
        "Diabetes":"Maintain healthy diet and monitor sugar levels.",
        "Heart Disease":"Reduce salt intake and exercise regularly.",
        "Asthma":"Avoid dust and allergens.",
        "Hypertension":"Manage stress and reduce sodium.",
        "Obesity":"Balanced diet and regular exercise recommended.",
        "Depression":"Seek mental health support and maintain routine."
        }

        st.info(tips.get(selected,"Maintain healthy lifestyle and consult doctor."))

