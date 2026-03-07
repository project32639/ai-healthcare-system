import streamlit as st
import random
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.set_page_config(page_title="AI Healthcare System", layout="wide")

# -------------------------------------------------
# DASHBOARD STYLE
# -------------------------------------------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#141E30,#243B55);
color:white;
font-family:sans-serif;
}

.title{
text-align:center;
font-size:50px;
font-weight:bold;
margin-bottom:20px;
}

.card{
background:linear-gradient(135deg,#1e5799,#2989d8);
padding:30px;
border-radius:15px;
text-align:center;
font-size:20px;
font-weight:600;
box-shadow:0 8px 20px rgba(0,0,0,0.5);
transition:0.3s;
margin-bottom:20px;
}

.card:hover{
transform:scale(1.05);
background:linear-gradient(135deg,#2989d8,#6dd5fa);
}

.report-box{
background:linear-gradient(135deg,#1e5799,#2989d8);
padding:20px;
border-radius:10px;
box-shadow:0 5px 15px rgba(0,0,0,0.4);
}

.doctor-card{
background:linear-gradient(135deg,#16A085,#2ECC71);
padding:25px;
border-radius:15px;
box-shadow:0 6px 20px rgba(0,0,0,0.4);
transition:0.3s;
}

.doctor-card:hover{
transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DISEASE DATABASE (UNCHANGED)
# -------------------------------------------------

DISEASE_DATABASE = {
"Diabetes":("Endocrinologist","Monitor glucose, reduce sugar intake, exercise regularly"),
"Hypertension":("Cardiologist","Reduce salt intake and manage stress"),
"Heart Disease":("Cardiologist","Maintain heart healthy diet"),
"Asthma":("Pulmonologist","Avoid allergens and pollution"),
"Stroke":("Neurologist","Control blood pressure"),
"Arthritis":("Rheumatologist","Regular joint exercise"),
"Depression":("Psychiatrist","Mental therapy and support"),
"Anxiety Disorder":("Psychiatrist","Meditation and therapy"),
"Kidney Disease":("Nephrologist","Stay hydrated and control BP"),
"Liver Disease":("Hepatologist","Avoid alcohol"),
"Obesity":("Nutritionist","Healthy diet and exercise"),
"Thyroid Disorder":("Endocrinologist","Regular hormone check"),
"Migraine":("Neurologist","Maintain sleep cycle"),
"COVID-19":("Infectious Disease Specialist","Vaccination and hygiene"),
"Tuberculosis":("Pulmonologist","Complete antibiotics course"),
"Malaria":("General Physician","Prevent mosquito bites"),
"Dengue":("General Physician","Hydration and mosquito control"),
"Pneumonia":("Pulmonologist","Vaccination recommended"),
"Bronchitis":("Pulmonologist","Avoid smoking"),
"Skin Allergy":("Dermatologist","Avoid allergens"),
"Psoriasis":("Dermatologist","Moisturize skin"),
"Gastritis":("Gastroenterologist","Avoid spicy food"),
"Ulcer":("Gastroenterologist","Limit NSAIDs"),
"IBS":("Gastroenterologist","Fiber rich diet"),
"Parkinson’s Disease":("Neurologist","Physical therapy"),
"Alzheimer’s Disease":("Neurologist","Brain stimulation activities"),
"Osteoporosis":("Orthopedic","Calcium intake"),
"Anemia":("Hematologist","Iron rich foods"),
"Cancer":("Oncologist","Regular screening"),
"Prostate Disorder":("Urologist","Regular prostate exam"),
"PCOS":("Gynecologist","Weight control"),
"Endometriosis":("Gynecologist","Hormone therapy"),
"Glaucoma":("Ophthalmologist","Eye pressure monitoring"),
"Cataract":("Ophthalmologist","Eye surgery"),
"Sinusitis":("ENT Specialist","Steam inhalation")
}

# -------------------------------------------------
# SYMPTOMS
# -------------------------------------------------

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

# -------------------------------------------------
# PAGE SESSION
# -------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page="Home"

# -------------------------------------------------
# HOME DASHBOARD
# -------------------------------------------------

if st.session_state.page=="Home":

    st.markdown('<div class="title">🏥 AI Healthcare Dashboard</div>',unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        if st.button("🧠 AI Disease Prediction"):
            st.session_state.page="predict"

    with col2:
        if st.button("📊 Patient Risk Timeline"):
            st.session_state.page="timeline"

    with col3:
        if st.button("📑 AI Medical Report"):
            st.session_state.page="report"

    col4,col5=st.columns(2)

    with col4:
        if st.button("💬 AI Medical Assistant"):
            st.session_state.page="chat"

    with col5:
        if st.button("👨‍⚕ Doctor Recommendation"):
            st.session_state.page="doctor"

# -------------------------------------------------
# AI DISEASE PREDICTION
# -------------------------------------------------

elif st.session_state.page=="predict":

    st.title("🧠 AI Disease Prediction")

    age=st.slider("Age",1,100)

    gender=st.selectbox("Gender",["Male","Female","Other"])

    smoking=st.selectbox("Smoking",["Yes","No"])

    activity=st.selectbox(
        "Physical Activity",
        ["Very High","High","Moderate","Low","Very Low"]
    )

    height=st.number_input("Height (m)",1.0,2.5,1.7)
    weight=st.number_input("Weight (kg)",30,200,70)

    bmi=weight/(height**2)

    st.success(f"BMI: {round(bmi,2)}")

    symptoms=st.multiselect("Select Symptoms",SYMPTOMS)

    custom_symptoms=st.text_input("Other Symptoms (comma separated)")

    if st.button("Predict Disease"):

        predicted=random.sample(list(DISEASE_DATABASE.keys()),3)

        st.session_state.predicted=predicted

        probs=[random.randint(50,95) for _ in predicted]

        fig=plt.figure()
        plt.bar(predicted,probs)
        plt.title("Disease Probability %")
        st.pyplot(fig)

        for d,p in zip(predicted,probs):

            doctor,tips=DISEASE_DATABASE[d]

            st.success(f"{d} ({p}%)")

            st.write("Doctor:",doctor)
            st.write("Advice:",tips)

# -------------------------------------------------
# RISK TIMELINE
# -------------------------------------------------

elif st.session_state.page=="timeline":

    st.title("📊 Patient Risk Timeline")

    diseases=st.multiselect("Select Diseases",list(DISEASE_DATABASE.keys()))

    custom=st.text_input("Add Other Diseases (comma separated)")

    surgery=st.selectbox("Any Past Surgery?",["No","Yes"])

    if surgery=="Yes":
        surgery_type=st.text_input("Surgery Type")

    smoking=st.selectbox("Smoking",["No","Yes"])

    activity=st.selectbox(
        "Physical Activity",
        ["Very High","High","Moderate","Low","Very Low"]
    )

    if st.button("Generate Timeline"):

        years=["2025","2026","2027","2028","2029"]

        base=20+len(diseases)*5

        if smoking=="Yes":
            base+=10

        if surgery=="Yes":
            base+=15

        risks=[min(base+random.randint(-5,10),95) for i in years]

        st.session_state.risk=risks[-1]

        fig=plt.figure()
        plt.plot(years,risks,marker="o")
        plt.title("Health Risk Timeline")
        st.pyplot(fig)

# -------------------------------------------------
# REPORT
# -------------------------------------------------

elif st.session_state.page=="report":

    st.title("📑 AI Medical Report")

    name=st.text_input("Patient Name")

    if st.button("Generate Report"):

        predicted=st.session_state.get("predicted",[])
        risk=st.session_state.get("risk","Unknown")

        text=f"Patient: {name}\nPredicted Diseases: {predicted}\nRisk Score: {risk}"

        styles=getSampleStyleSheet()

        file=tempfile.NamedTemporaryFile(delete=False)

        doc=SimpleDocTemplate(file.name)

        story=[Paragraph("AI Healthcare Report",styles['Title']),
        Spacer(1,20),
        Paragraph(text,styles['BodyText'])]

        doc.build(story)

        with open(file.name,"rb") as f:
            st.download_button("Download PDF",f,"medical_report.pdf")

# -------------------------------------------------
# CHATBOT
# -------------------------------------------------

elif st.session_state.page=="chat":

    st.title("💬 AI Medical Assistant")

    q=st.text_input("Ask medical question")

    if st.button("Ask"):
        st.info("Connect GPT API here")

# -------------------------------------------------
# DOCTOR RECOMMENDATION
# -------------------------------------------------

elif st.session_state.page=="doctor":

    st.title("👨‍⚕ Doctor Recommendation")

    disease=st.selectbox("Select Disease",list(DISEASE_DATABASE.keys()))

    if disease:

        doctor,tips=DISEASE_DATABASE[disease]

        st.markdown(f"""
        <div class="doctor-card">
        <h3>Consult: {doctor}</h3>
        <p><b>Advice:</b> {tips}</p>
        </div>
        """,unsafe_allow_html=True)
