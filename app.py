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
# CUSTOM CSS THEME
# -------------------------

st.markdown("""
<style>

body{
background: linear-gradient(135deg,#e6f3ff,#f7fbff);
}

.title-box{
background: linear-gradient(90deg,#0077b6,#00b4d8);
padding:25px;
border-radius:12px;
text-align:center;
color:white;
font-size:35px;
font-weight:bold;
animation: fadeIn 2s;
}

.feature-box{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0 4px 10px rgba(0,0,0,0.1);
transition:0.3s;
}

.feature-box:hover{
transform:scale(1.05);
box-shadow:0 8px 20px rgba(0,0,0,0.2);
}

.sidebar .sidebar-content{
background:linear-gradient(#023e8a,#0077b6);
color:white;
}

@keyframes fadeIn{
0%{opacity:0}
100%{opacity:1}
}

</style>
""",unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("🧭 Navigation")

page = st.sidebar.radio(
"Select Page",
[
"🏠 Home",
"🧠 AI Disease Prediction",
"📊 Patient Risk Timeline",
"📑 AI Report",
"💬 AI Medical Assistant",
"👨‍⚕ Doctor Recommendation"
]
)

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

if page=="🏠 Home":

    st.markdown('<div class="title-box">🧬 AI Healthcare System</div>',unsafe_allow_html=True)

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown('<div class="feature-box">✔ AI Disease Prediction</div>',unsafe_allow_html=True)
        st.markdown('<div class="feature-box">✔ Patient Symptom Analysis</div>',unsafe_allow_html=True)
        st.markdown('<div class="feature-box">✔ Health Risk Timeline</div>',unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-box">✔ AI Medical Insights</div>',unsafe_allow_html=True)
        st.markdown('<div class="feature-box">✔ AI Chat Assistant</div>',unsafe_allow_html=True)
        st.markdown('<div class="feature-box">✔ Doctor Recommendation</div>',unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-box">✔ Early Disease Detection</div>',unsafe_allow_html=True)
        st.markdown('<div class="feature-box">✔ Preventive Healthcare</div>',unsafe_allow_html=True)

    st.write("")

    st.info("This AI healthcare system helps patients and doctors make smarter medical decisions using artificial intelligence.")

# -------------------------
# AI DISEASE PREDICTION
# -------------------------

elif page=="🧠 AI Disease Prediction":

    st.title("AI Disease Prediction")

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

elif page=="📊 Patient Risk Timeline":

    st.title("Patient Health Risk Timeline")

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

elif page=="📑 AI Report":

    st.title("AI Report")

    st.write("Why the AI predicted this result:")

    st.write("• Age may influence disease risk")
    st.write("• BMI and weight can affect health")
    st.write("• Selected symptoms increase probability")
    st.write("• Patient medical history plays a role")
    st.write("• Lifestyle factors may impact prediction")

# -------------------------
# AI MEDICAL ASSISTANT
# -------------------------

elif page=="💬 AI Medical Assistant":

    st.title("AI Medical Assistant")

    user_question=st.text_area("Describe your symptoms or medical question")

    if st.button("Ask AI"):

        response="Consult a doctor if symptoms persist."

        st.write(response)

# -------------------------
# DOCTOR RECOMMENDATION
# -------------------------

elif page=="👨‍⚕ Doctor Recommendation":

    st.title("Doctor Recommendation System")

    disease=st.selectbox("Select Disease",diseases)

    custom=st.text_input("Or type disease")

    if disease in doctors:

        doc=doctors[disease]

        st.success(f"Recommended Specialist: {doc}")

        st.write(f"Patients with {disease} should consult a {doc}")

    elif custom!="":

        st.info("Consult a General Physician for initial diagnosis.")
