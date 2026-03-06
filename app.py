import streamlit as st
import numpy as np
import plotly.express as px
import requests

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🧬",
    layout="wide"
)

# -------------------------
# SESSION STATE
# -------------------------

if "page" not in st.session_state:
    st.session_state.page="Home"

# -------------------------
# CUSTOM CSS THEME
# -------------------------

st.markdown("""
<style>

body{
background: linear-gradient(135deg,#e6f3ff,#f7fbff);
}

/* TITLE */

.big-title{
font-size:60px;
font-weight:bold;
text-align:center;
padding:20px;
border-radius:20px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
box-shadow:0px 8px 25px rgba(0,0,0,0.2);
}

/* NAVIGATION BUTTON BOX */

div.stButton > button{
background:linear-gradient(135deg,#e3f2fd,#bbdefb);
color:#0d47a1;
font-size:20px;
font-weight:700;
padding:25px;
border-radius:15px;
border:none;
width:100%;
text-align:center;
box-shadow:0px 5px 18px rgba(0,0,0,0.15);
transition:0.3s;
}

div.stButton > button:hover{
transform:scale(1.05);
background:linear-gradient(135deg,#bbdefb,#90caf9);
}

/* FEATURE LIST */

.feature-list{
color:#0d47a1;
font-size:20px;
font-weight:600;
}

</style>
""",unsafe_allow_html=True)

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------

st.sidebar.title("🧭 Navigation")

nav=st.sidebar.radio(
"",
[
"Home",
"AI Disease Prediction",
"Patient Risk Timeline",
"AI Report",
"AI Medical Assistant",
"Doctor Recommendation"
]
)

st.session_state.page=nav

# -------------------------
# DATA
# -------------------------

symptom_options = [

"Fever","Cough","Shortness of Breath","Chest Pain","Headache",
"Fatigue","Body Pain","Dizziness","Nausea","Vomiting","Diarrhea",
"Constipation","Abdominal Pain","Back Pain","Joint Pain","Muscle Pain",
"Blurred Vision","Eye Pain","Skin Rash","Itching","Swelling",
"Weight Loss","Weight Gain","Frequent Urination","Excessive Thirst",
"Loss of Appetite","Sore Throat","Runny Nose","Insomnia","Anxiety",
"Depression","Memory Loss","Confusion","Difficulty Breathing",
"Heart Palpitations","Cold Sensitivity","Heat Sensitivity",
"Numbness","Tingling Sensation","Loss of Balance","Sneezing",
"High Blood Pressure","Low Blood Pressure","Dry Skin","Hair Loss",
"Burning Urination","Night Sweats","Mood Swings","Fainting"
]

diseases = [

"Diabetes","Heart Disease","Glaucoma","Kidney Disease",
"Hypertension","Cancer","Asthma","Arthritis",
"Alzheimer's Disease","Parkinson's Disease","Stroke",
"Liver Disease","Thyroid Disorder","Osteoporosis",
"Depression","Anxiety Disorder","Migraine",
"Pneumonia","Tuberculosis","COVID-19",
"Gastritis","Peptic Ulcer","Obesity","Anemia",
"Skin Allergy","Psoriasis","Eczema",
"Gallstones","Pancreatitis","Chronic Bronchitis",
"Sinusitis","Appendicitis","Hepatitis","Leukemia"
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
"Obesity":"Nutritionist",
"Anemia":"Hematologist",
"Skin Allergy":"Dermatologist",
"Psoriasis":"Dermatologist",
"Eczema":"Dermatologist"
}

conditions = [

"Diabetes","Hypertension","Heart Surgery","Kidney Surgery",
"Liver Transplant","Cancer Treatment","Asthma","Thyroid Disorder",
"Appendectomy","Gallbladder Removal","Hip Replacement",
"Knee Replacement","Spinal Surgery","Brain Surgery",
"Eye Surgery","Dental Surgery","Organ Transplant",
"Chemotherapy","Radiation Therapy","Insulin Therapy",
"Dialysis","Blood Transfusion","Cardiac Bypass",
"Pacemaker Implant","Stent Placement","Physical Therapy",
"Psychiatric Treatment","Obesity Treatment","Allergy Treatment",
"Chronic Pain Treatment"
]

# -------------------------
# HOME PAGE
# -------------------------

if st.session_state.page=="Home":

    st.markdown('<div class="big-title">🧬 AI Healthcare Intelligence System 🤖</div>',unsafe_allow_html=True)

    st.write("")

    col1,col2=st.columns(2)

    with col1:

        if st.button("🧠 AI Disease Prediction"):
            st.session_state.page="AI Disease Prediction"
            st.rerun()

        if st.button("📊 Patient Risk Timeline"):
            st.session_state.page="Patient Risk Timeline"
            st.rerun()

        if st.button("📑 AI Report"):
            st.session_state.page="AI Report"
            st.rerun()

    with col2:

        if st.button("💬 AI Medical Assistant"):
            st.session_state.page="AI Medical Assistant"
            st.rerun()

        if st.button("👨‍⚕ Doctor Recommendation"):
            st.session_state.page="Doctor Recommendation"
            st.rerun()

    st.write("")

    st.markdown('<div class="feature-list">🏥 What This System Can Do</div>',unsafe_allow_html=True)

    st.markdown("""
<div class="feature-list">
✔ AI Disease Prediction <br>
✔ Patient Symptom Analysis <br>
✔ Health Risk Timeline Prediction <br>
✔ Explainable AI Medical Insights <br>
✔ AI Medical Chat Assistant <br>
✔ Doctor & Specialist Recommendation <br>
✔ Early Disease Detection Support <br>
✔ Preventive Healthcare Insights
</div>
""",unsafe_allow_html=True)

# -------------------------
# AI DISEASE PREDICTION
# -------------------------

elif st.session_state.page=="AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age=st.slider("Age",1,100)

    weight=st.number_input("Weight (kg)")
    height=st.number_input("Height (cm)")

    symptoms=st.multiselect("Select Symptoms",symptom_options)

    custom_symptom=st.text_input("Add custom symptom (optional)")

    if st.button("Predict Disease"):

        prediction=np.random.choice(diseases)

        st.success(f"Predicted Disease: {prediction}")

# -------------------------
# PATIENT RISK TIMELINE
# -------------------------

elif st.session_state.page=="Patient Risk Timeline":

    st.title("📊 Patient Health Risk Timeline")

    condition=st.selectbox(
    "Current Medical Condition / Surgery / Treatment",
    conditions
    )

    years=st.slider("Years to Predict Risk",1,10)

    risk=np.random.randint(20,80,years)

    df={"Year":list(range(1,years+1)),"Risk %":risk}

    fig=px.line(df,x="Year",y="Risk %")

    st.plotly_chart(fig)

# -------------------------
# AI REPORT
# -------------------------

elif st.session_state.page=="AI Report":

    st.title("📑 AI Report")

    st.subheader("Understanding the Factors Behind This Health Prediction")

    st.write("• Age may influence disease risk")
    st.write("• BMI and weight can affect health")
    st.write("• Selected symptoms increase probability")
    st.write("• Patient medical history plays a role")
    st.write("• Lifestyle factors may impact prediction")

# -------------------------
# AI MEDICAL ASSISTANT
# -------------------------

elif st.session_state.page=="AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    user_question=st.text_area("Describe your symptoms or medical question")

    if st.button("Ask AI"):

        response="Consult a doctor if symptoms persist."

        st.write(response)

# -------------------------
# DOCTOR RECOMMENDATION
# -------------------------

elif st.session_state.page=="Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation System")

    disease=st.selectbox("Select Disease",diseases)

    custom=st.text_input("Or type disease")

    if disease in doctors:

        doc=doctors[disease]

        st.success(f"Recommended Specialist: {doc}")

        st.write(f"Patients with {disease} should consult a {doc}")

    elif custom!="":

        st.info("Consult a General Physician for initial diagnosis.")
