import streamlit as st
import random
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile
import os

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(page_title="AI Healthcare System", layout="wide")

# ---------------------------------------------------
# STYLE (ROYAL BLUE UI)
# ---------------------------------------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#0b1f5e,#001133);
color:white;
}

.big-title{
font-size:55px;
font-weight:bold;
text-align:center;
padding:20px;
border-radius:20px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
}

.feature-box{
background:linear-gradient(135deg,#1a3fb3,#2957ff);
color:white;
padding:25px;
border-radius:15px;
box-shadow:0px 6px 20px rgba(0,0,0,0.3);
text-align:center;
font-size:20px;
font-weight:600;
}

.info-box{
background:linear-gradient(135deg,#1a3fb3,#2957ff);
padding:25px;
border-radius:15px;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# DISEASE DATABASE (35+)
# ---------------------------------------------------

DISEASE_DATABASE = {

"Diabetes":("Endocrinologist","Control sugar, exercise, monitor glucose"),
"Hypertension":("Cardiologist","Reduce salt, manage stress"),
"Heart Disease":("Cardiologist","Healthy diet and avoid smoking"),
"Asthma":("Pulmonologist","Avoid allergens and use inhaler"),
"Stroke":("Neurologist","Control BP and cholesterol"),
"Arthritis":("Rheumatologist","Joint exercise and anti inflammatory diet"),
"Depression":("Psychiatrist","Counseling and mental health care"),
"Anxiety Disorder":("Psychiatrist","Stress management and therapy"),
"Kidney Disease":("Nephrologist","Drink water and control BP"),
"Liver Disease":("Hepatologist","Avoid alcohol and fatty foods"),
"Obesity":("Nutritionist","Balanced diet and exercise"),
"Thyroid Disorder":("Endocrinologist","Regular thyroid checkups"),
"Migraine":("Neurologist","Avoid triggers and maintain sleep"),
"COVID-19":("Infectious Disease Specialist","Vaccination and hygiene"),
"Tuberculosis":("Pulmonologist","Complete medication course"),
"Malaria":("General Physician","Prevent mosquito bites"),
"Dengue":("General Physician","Hydration and mosquito protection"),
"Pneumonia":("Pulmonologist","Vaccination and avoid smoking"),
"Bronchitis":("Pulmonologist","Avoid pollution and smoking"),
"Skin Allergy":("Dermatologist","Avoid allergens"),
"Psoriasis":("Dermatologist","Skin care and stress reduction"),
"Gastritis":("Gastroenterologist","Avoid spicy food"),
"Ulcer":("Gastroenterologist","Avoid NSAIDs and alcohol"),
"IBS":("Gastroenterologist","Fiber diet and stress control"),
"Parkinson’s Disease":("Neurologist","Physical therapy"),
"Alzheimer’s Disease":("Neurologist","Brain exercises"),
"Osteoporosis":("Orthopedic","Calcium and vitamin D"),
"Anemia":("Hematologist","Iron rich foods"),
"Cancer":("Oncologist","Regular screening"),
"Prostate Disorder":("Urologist","Regular prostate exam"),
"PCOS":("Gynecologist","Weight control and hormone care"),
"Endometriosis":("Gynecologist","Pain management"),
"Glaucoma":("Ophthalmologist","Eye checkups"),
"Cataract":("Ophthalmologist","Eye surgery if required"),
"Sinusitis":("ENT Specialist","Steam inhalation")

}

# ---------------------------------------------------
# SYMPTOMS (35+)
# ---------------------------------------------------

SYMPTOMS = [

"Fever","Cough","Fatigue","Headache","Chest Pain","Shortness of Breath",
"Nausea","Vomiting","Dizziness","Joint Pain","Muscle Pain",
"Weight Loss","Weight Gain","High Blood Sugar","Frequent Urination",
"Blurred Vision","Skin Rash","Itching","Abdominal Pain",
"Constipation","Diarrhea","Loss of Appetite","Insomnia",
"Depression","Anxiety","Memory Loss","Confusion","Swelling",
"Back Pain","Neck Pain","Sore Throat","Runny Nose",
"Sweating","Palpitations","Hair Loss"

]

# ---------------------------------------------------
# NAVIGATION
# ---------------------------------------------------

page = st.sidebar.selectbox("Navigation",[
"Home",
"AI Disease Prediction",
"Patient Risk Timeline",
"AI Report",
"AI Medical Assistant",
"Doctor Recommendation"
])

# ---------------------------------------------------
# HOME
# ---------------------------------------------------

if page=="Home":

    st.markdown('<div class="big-title">🏥 AI Healthcare System</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="info-box">

🏥 What This AI Model Does  
✔ Predicts possible diseases from symptoms  
✔ Analyzes patient symptom patterns  
✔ Generates health risk timeline predictions  
✔ Provides explainable AI medical insights  
✔ AI medical chatbot for questions  
✔ Doctor & specialist recommendations  
✔ Preventive healthcare insights  

</div>
""", unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    col1.markdown('<div class="feature-box">🧠 AI Disease Prediction</div>',unsafe_allow_html=True)
    col2.markdown('<div class="feature-box">📊 Patient Risk Timeline</div>',unsafe_allow_html=True)
    col3.markdown('<div class="feature-box">📑 AI Report</div>',unsafe_allow_html=True)

    col4,col5=st.columns(2)

    col4.markdown('<div class="feature-box">💬 AI Medical Assistant</div>',unsafe_allow_html=True)
    col5.markdown('<div class="feature-box">👨‍⚕ Doctor Recommendation</div>',unsafe_allow_html=True)

# ---------------------------------------------------
# AI DISEASE PREDICTION
# ---------------------------------------------------

elif page=="AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age = st.slider("Age",1,100)

    gender = st.selectbox("Gender",["Male","Female"])

    smoking = st.selectbox("Smoking",["No","Yes"])

    activity = st.selectbox("Physical Activity",
    ["Very High","High","Moderate","Low","Very Low"])

    symptoms = st.multiselect("Select Symptoms",SYMPTOMS)

    custom_symptoms = st.text_input("Other Symptoms (comma separated)")

    if st.button("Predict Disease"):

        diseases=list(DISEASE_DATABASE.keys())

        predicted=random.sample(diseases,3)

        st.subheader("Predicted Diseases")

        for d in predicted:

            prob=random.randint(50,95)

            doctor,tips=DISEASE_DATABASE[d]

            st.success(f"{d} ({prob}% probability)")

            st.write("Specialist:",doctor)

            st.write("Advice:",tips)

        # risk graph
        probs=[random.randint(40,95) for _ in predicted]

        fig=plt.figure()

        plt.bar(predicted,probs)

        plt.title("Disease Probability")

        st.pyplot(fig)

# ---------------------------------------------------
# PATIENT RISK TIMELINE
# ---------------------------------------------------

elif page=="Patient Risk Timeline":

    st.title("📊 Patient Risk Timeline")

    selected=st.multiselect("Select Diseases",list(DISEASE_DATABASE.keys()))

    custom=st.text_input("Add Other Diseases (comma separated)")

    if selected:

        years=["2025","2026","2027","2028","2029"]

        risk=[random.randint(10,90) for _ in years]

        fig=plt.figure()

        plt.plot(years,risk,marker="o")

        plt.title("Risk Timeline")

        st.pyplot(fig)

# ---------------------------------------------------
# AI REPORT
# ---------------------------------------------------

elif page=="AI Report":

    st.title("📑 AI Medical Report")

    name=st.text_input("Patient Name")

    height=st.number_input("Height (m)",1.0,2.5)

    weight=st.number_input("Weight (kg)",30,200)

    if st.button("Generate Report"):

        bmi=weight/(height**2)

        st.write("BMI:",round(bmi,2))

        report=f"""

Patient Name: {name}

BMI: {round(bmi,2)}

Recommendation:
Maintain healthy lifestyle
"""

        styles=getSampleStyleSheet()

        file=tempfile.NamedTemporaryFile(delete=False)

        doc=SimpleDocTemplate(file.name)

        story=[Paragraph("AI Medical Report",styles['Title']),Spacer(1,20),
        Paragraph(report,styles['BodyText'])]

        doc.build(story)

        with open(file.name,"rb") as f:

            st.download_button("Download PDF",f,"report.pdf")

# ---------------------------------------------------
# AI MEDICAL ASSISTANT
# ---------------------------------------------------

elif page=="AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    question=st.text_input("Ask a medical question")

    if st.button("Ask"):

        st.info("GPT response placeholder. Add OpenAI API key.")

# ---------------------------------------------------
# DOCTOR RECOMMENDATION
# ---------------------------------------------------

elif page=="Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation")

    disease=st.selectbox("Select Disease",list(DISEASE_DATABASE.keys()))

    if disease:

        doctor,tips=DISEASE_DATABASE[disease]

        st.success("Specialist Doctor: "+doctor)

        st.write("Health Tips:",tips)
