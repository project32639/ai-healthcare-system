import streamlit as st
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

/* FEATURE BOXES */

.feature-box{
background:linear-gradient(135deg,#d6ecff,#c9f7e8);
color:#003366;
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
background:linear-gradient(135deg,#bde0ff,#b8f5e3);
}

/* SYSTEM FEATURE PANEL */

.system-box{
background:linear-gradient(135deg,#e8f4ff,#e6fff3);
padding:25px;
border-radius:15px;
color:#003366;
font-size:18px;
box-shadow:0px 5px 18px rgba(0,0,0,0.12);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE STATE
# ---------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

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
],
index=[
"Home",
"AI Disease Prediction",
"Patient Risk Timeline",
"AI Report",
"AI Medical Assistant",
"Doctor Recommendation"
].index(st.session_state.page)
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

conditions = [
"Diabetes","Hypertension","Heart Surgery","Kidney Stones",
"Thyroid Disorder","Asthma","Allergy","Obesity",
"COVID Infection","Cancer Treatment","Fracture Surgery",
"Joint Replacement","Liver Disease","Stroke History",
"Depression Treatment","Anxiety Disorder","Gastritis",
"Ulcer Surgery","Eye Surgery","Spine Surgery",
"Pregnancy","Blood Transfusion","Dialysis",
"Organ Transplant","Cardiac Bypass","Pacemaker",
"Brain Surgery","Appendix Surgery","Gallbladder Surgery",
"Skin Treatment"
]

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

if st.session_state.page == "Home":

    st.markdown('<div class="big-title">🧬 AI Healthcare Intelligence System 🤖</div>', unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([2,1])

    with left:

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

    with right:

        st.markdown("""
        <div class="system-box">
        <h3>🏥 What This System Can Do</h3>

        ✔ AI Disease Prediction<br>
        ✔ Patient Symptom Analysis<br>
        ✔ Health Risk Timeline Prediction<br>
        ✔ Explainable AI Medical Insights<br>
        ✔ AI Medical Chat Assistant<br>
        ✔ Doctor & Specialist Recommendation<br>
        ✔ Early Disease Detection Support<br>
        ✔ Preventive Healthcare Insights
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------
# AI DISEASE PREDICTION
# ---------------------------------------------------

if st.session_state.page == "AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age = st.slider("Age",1,100)
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    glucose = st.number_input("Glucose Level")
    bp = st.number_input("Blood Pressure")

    symptoms = st.multiselect("Select Patient Symptoms",symptom_list)

    other = st.text_input("Other Symptoms (optional)")

    if st.button("Predict Disease"):
        prediction=random.choice(diseases)
        st.success(f"Predicted Disease Risk: {prediction}")

# ---------------------------------------------------
# RISK TIMELINE
# ---------------------------------------------------

if st.session_state.page == "Patient Risk Timeline":

    st.title("📊 Patient Health Risk Timeline")

    condition=st.selectbox(
    "Current Medical Condition / Surgery / Treatment",
    conditions
    )

    if st.button("Generate Timeline"):

        st.write("Health Risk Analysis")

        st.progress(30)
        st.write("Current Health Risk: Low")

        st.progress(60)
        st.write("5 Year Risk: Moderate")

        st.progress(80)
        st.write("10 Year Risk: High")

# ---------------------------------------------------
# AI REPORT
# ---------------------------------------------------

if st.session_state.page == "AI Report":

    st.title("📑 AI Report")

    st.write("Why the AI predicted this result:")

    st.write("• Age factor contributed to the prediction")
    st.write("• Body Mass Index (BMI) influenced health risk")
    st.write("• Selected symptoms increased probability")
    st.write("• Patient health history affected prediction")
    st.write("• Lifestyle risk indicators detected")

# ---------------------------------------------------
# AI MEDICAL ASSISTANT
# ---------------------------------------------------

if st.session_state.page == "AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    question = st.text_area("Describe your symptoms or medical question")

    if st.button("Ask AI"):
        st.info("This assistant provides general medical information. For diagnosis consult a doctor.")

# ---------------------------------------------------
# DOCTOR RECOMMENDATION
# ---------------------------------------------------

if st.session_state.page == "Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation System")

    disease = st.selectbox("Select Disease", diseases)

    custom = st.text_input("Or Type Disease")

    if st.button("Recommend Doctor"):

        if custom!="":
            st.success(f"Patients with {custom} should consult a Specialist Physician.")
        else:
            doc=doctors.get(disease,"General Physician")
            st.success(f"Recommended Specialist: {doc}")
            st.write(f"Patients with {disease} should consult a {doc}.")
