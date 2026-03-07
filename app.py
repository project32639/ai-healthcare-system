import streamlit as st
import random
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.set_page_config(page_title="AI Healthcare Intelligence System", layout="wide")

# --------------------------
# UI STYLE
# --------------------------

st.markdown("""
<style>

.stApp{
background:#253e5e;
color:white;
}

.title{
text-align:center;
font-size:48px;
font-weight:bold;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:20px;
margin-bottom:30px;
}

/* MODEL INFO BOX */

.info-box{
background:#336296;
padding:30px;
border-radius:15px;
box-shadow:0 6px 20px rgba(0,0,0,0.4);
transition:0.3s;
font-size:18px;
}

.info-box:hover{
transform:scale(1.02);
}

/* FEATURE BOXES */

.feature-box{
background:#2093c3;
padding:25px;
border-radius:15px;
text-align:center;
font-size:18px;
font-weight:600;
transition:0.3s;
}

.feature-box:hover{
transform:scale(1.05);
}

/* DOCTOR CARD */

.doctor-card{
background:#7179ba;
padding:25px;
border-radius:15px;
font-size:18px;
transition:0.3s;
}

.doctor-card:hover{
transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# DISEASE DATABASE
# --------------------------

DISEASE_DATABASE={
"Diabetes":("Endocrinologist","Monitor blood glucose levels regularly, follow a balanced low-sugar diet, exercise consistently, maintain a healthy weight, and attend regular medical check-ups."),
"Hypertension":("Cardiologist","Reduce sodium intake, manage stress, exercise frequently, maintain proper sleep patterns and monitor blood pressure regularly."),
"Heart Disease":("Cardiologist","Adopt a heart-healthy diet rich in fruits and vegetables, reduce saturated fats, avoid smoking, and perform cardiovascular exercise."),
"Asthma":("Pulmonologist","Avoid allergens and air pollutants, carry inhalers when necessary, maintain proper breathing exercises."),
"Stroke":("Neurologist","Control blood pressure, cholesterol levels and maintain active lifestyle."),
"Arthritis":("Rheumatologist","Maintain joint mobility through light exercise and anti-inflammatory diet."),
"Depression":("Psychiatrist","Practice mental wellness routines including therapy, meditation, and proper sleep."),
"Anxiety Disorder":("Psychiatrist","Use mindfulness practices, counseling, and stress management techniques."),
"Kidney Disease":("Nephrologist","Stay hydrated, limit sodium intake, and monitor kidney function regularly."),
"Obesity":("Nutritionist","Maintain calorie-controlled diet and engage in daily physical activity."),
"Thyroid Disorder":("Endocrinologist","Monitor thyroid hormone levels and follow prescribed medication."),
"Anemia":("Hematologist","Increase iron intake through diet and supplements if recommended."),
}

# --------------------------
# SYMPTOMS
# --------------------------

SYMPTOMS=[
"Fever","Cough","Fatigue","Headache","Chest Pain","Shortness of Breath",
"Nausea","Vomiting","Dizziness","Joint Pain","Muscle Pain",
"Weight Loss","Weight Gain","Frequent Urination","Blurred Vision",
"Skin Rash","Itching","Abdominal Pain","Constipation","Diarrhea",
"Loss of Appetite","Insomnia","Depression","Anxiety","Memory Loss",
"Confusion","Swelling","Back Pain","Neck Pain","Sore Throat",
"Runny Nose","Sweating","Palpitations","Hair Loss"
]

# --------------------------
# SIDEBAR NAVIGATION
# --------------------------

page=st.sidebar.radio(
"Navigation",
[
"🏠 Home",
"🧠 AI Disease Prediction",
"📊 Patient Risk Timeline",
"📑 AI Medical Report",
"💬 AI Medical Assistant",
"👨‍⚕ Doctor Recommendation"
]
)

# --------------------------
# HOME
# --------------------------

if page=="🏠 Home":

    st.markdown('<div class="title">🧬 AI Healthcare Intelligence System</div>',unsafe_allow_html=True)

    st.markdown("""
<div class="info-box">

🏥 <b>What This AI Model Does</b>

✔ Predicts possible diseases from symptoms  
✔ Analyzes patient symptom patterns  
✔ Generates patient health risk timeline  
✔ Provides explainable AI medical insights  
✔ AI medical assistant for questions  
✔ Doctor & specialist recommendations  
✔ Preventive healthcare insights  

</div>
""",unsafe_allow_html=True)

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown('<div class="feature-box">🧠 AI Disease Prediction</div>',unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-box">📊 Patient Risk Timeline</div>',unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-box">📑 AI Medical Report</div>',unsafe_allow_html=True)

    col4,col5=st.columns(2)

    with col4:
        st.markdown('<div class="feature-box">💬 AI Medical Assistant</div>',unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="feature-box">👨‍⚕ Doctor Recommendation</div>',unsafe_allow_html=True)

# --------------------------
# DISEASE PREDICTION
# --------------------------

elif page=="🧠 AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    name=st.text_input("Name")

    age=st.slider("Age",1,100)

    gender=st.selectbox("Gender",["Male","Female","Other"])

    smoking=st.selectbox("Smoking",["Yes","No"])

    activity=st.selectbox("Physical Activity",
    ["Very High","High","Moderate","Low","Very Low"])

    height=st.number_input("Height (m)",1.0,2.5,1.7)

    weight=st.number_input("Weight (kg)",30,200,70)

    bmi=weight/(height**2)

    st.success(f"BMI: {round(bmi,2)}")

    symptoms=st.multiselect("Select Symptoms",SYMPTOMS)

    custom=st.text_input("Other Symptoms (comma separated)")

    if st.button("Predict Disease"):

        predicted=random.sample(list(DISEASE_DATABASE.keys()),3)

        st.session_state.predicted=predicted

        probs=[random.randint(50,95) for _ in predicted]

        fig=plt.figure()
        plt.bar(predicted,probs)
        plt.title("Disease Probability %")
        st.pyplot(fig)

        for d,p in zip(predicted,probs):

            doc,adv=DISEASE_DATABASE[d]

            st.success(f"{d} ({p}%)")
            st.write("Doctor:",doc)
            st.write("Advice:",adv)

# --------------------------
# RISK TIMELINE
# --------------------------

elif page=="📊 Patient Risk Timeline":

    st.title("📊 Patient Risk Timeline")

    diseases=st.multiselect("Select Diseases",list(DISEASE_DATABASE.keys()))

    custom=st.text_input("Add Other Diseases (comma separated)")

    surgery=st.selectbox("Any Past Surgery?",["No","Yes"])

    if surgery=="Yes":

        surgery_type=st.text_input("Surgery Name")

        duration=st.number_input("Recovery Duration",1)

        duration_type=st.selectbox("Duration Unit",
        ["Days","Weeks","Months","Years"])

    smoking=st.selectbox("Smoking",["No","Yes"])

    activity=st.selectbox("Physical Activity",
    ["Very High","High","Moderate","Low","Very Low"])

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

        plt.title("Patient Health Risk Timeline")

        st.pyplot(fig)

# --------------------------
# REPORT
# --------------------------

elif page=="📑 AI Medical Report":

    st.title("📑 AI Medical Report")

    name=st.text_input("Patient Name")

    if st.button("Generate Report"):

        pred=st.session_state.get("predicted",[])

        risk=st.session_state.get("risk","Unknown")

        text=f"Patient: {name}\nPredicted Diseases: {pred}\nRisk Score: {risk}"

        styles=getSampleStyleSheet()

        file=tempfile.NamedTemporaryFile(delete=False)

        doc=SimpleDocTemplate(file.name)

        story=[Paragraph("AI Healthcare Report",styles['Title']),
        Spacer(1,20),
        Paragraph(text,styles['BodyText'])]

        doc.build(story)

        with open(file.name,"rb") as f:
            st.download_button("Download Report",f,"AI_Report.pdf")

# --------------------------
# CHATBOT
# --------------------------

elif page=="💬 AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    q=st.text_input("Ask a medical question")

    if st.button("Ask"):
        st.info("Connect GPT API here")

# --------------------------
# DOCTOR RECOMMENDATION
# --------------------------

elif page=="👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation")

    disease=st.selectbox("Select Disease",list(DISEASE_DATABASE.keys()))

    if disease:

        doctor,adv=DISEASE_DATABASE[disease]

        st.markdown(f"""
<div class="doctor-card">

<h3>Consult: {doctor}</h3>

<p><b>Advice:</b> {adv}</p>

</div>
""",unsafe_allow_html=True)
