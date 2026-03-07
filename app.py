import streamlit as st
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.set_page_config(page_title="🧬AI Healthcare Intelligence System🩺", layout="wide")

# --------------------------------------------------
# UI STYLE
# --------------------------------------------------

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
margin-bottom:20px;
}

.info-box{
background:#336296;
padding:30px;
border-radius:15px;
margin-bottom:40px;
transition:0.3s;
}

.info-box:hover{
transform:scale(1.02);
}

.feature-card{
background:#949eca;
padding:30px;
border-radius:15px;
text-align:center;
font-size:20px;
font-weight:bold;
margin:15px;
transition:0.3s;
}

.feature-card:hover{
transform:scale(1.05);
}

.doctor-card{
background:#7179ba;
padding:25px;
border-radius:15px;
margin-top:20px;
transition:0.3s;
}

.doctor-card:hover{
transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DISEASE DATABASE
# --------------------------------------------------

DISEASE_DATABASE={
"Diabetes":{
"doctor":"Endocrinologist",
"symptoms":["Frequent Urination","Blurred Vision","Fatigue","Weight Loss"],
"advice":"Maintain healthy diet, reduce sugar intake, exercise daily and monitor blood glucose regularly."
},
"Hypertension":{
"doctor":"Cardiologist",
"symptoms":["Headache","Chest Pain","Dizziness"],
"advice":"Reduce salt intake, maintain healthy weight and monitor blood pressure frequently."
},
"Asthma":{
"doctor":"Pulmonologist",
"symptoms":["Shortness of Breath","Chest Pain","Cough"],
"advice":"Avoid allergens, carry inhaler and maintain respiratory exercises."
},
"Anemia":{
"doctor":"Hematologist",
"symptoms":["Fatigue","Dizziness","Shortness of Breath"],
"advice":"Increase iron intake and consume iron rich foods."
},
"Arthritis":{
"doctor":"Rheumatologist",
"symptoms":["Joint Pain","Swelling","Muscle Pain"],
"advice":"Perform gentle joint exercises and maintain anti-inflammatory diet."
}
}

# --------------------------------------------------
# SYMPTOMS
# --------------------------------------------------

SYMPTOMS=[
"Fever","Cough","Fatigue","Headache","Chest Pain","Shortness of Breath",
"Nausea","Vomiting","Dizziness","Joint Pain","Muscle Pain",
"Weight Loss","Frequent Urination","Blurred Vision","Swelling",
"Skin Rash","Abdominal Pain","Constipation","Diarrhea",
"Loss of Appetite","Insomnia","Back Pain","Neck Pain",
"Sore Throat","Runny Nose","Sweating","Palpitations"
]

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

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

# --------------------------------------------------
# HOME
# --------------------------------------------------

if page=="🏠 Home":

    st.markdown('<div class="title">🧬AI Healthcare Intelligence System🩺</div>',unsafe_allow_html=True)

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

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown('<div class="feature-card">🧠 AI Disease Prediction</div>',unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-card">📊 Patient Risk Timeline</div>',unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-card">📑 AI Medical Report</div>',unsafe_allow_html=True)

    col4,col5=st.columns(2)

    with col4:
        st.markdown('<div class="feature-card">💬 AI Medical Assistant</div>',unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="feature-card">👨‍⚕ Doctor Recommendation</div>',unsafe_allow_html=True)

# --------------------------------------------------
# DISEASE PREDICTION
# --------------------------------------------------

elif page=="🧠 AI Disease Prediction":

    st.title("AI Disease Prediction")

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

    if st.button("Predict Disease"):

        scores={}

        for disease,data in DISEASE_DATABASE.items():

            match=len(set(symptoms) & set(data["symptoms"]))

            scores[disease]=match

        predicted=sorted(scores,key=scores.get,reverse=True)[:3]

        st.session_state.predicted=predicted
        st.session_state.symptoms=symptoms

        for d in predicted:

            data=DISEASE_DATABASE[d]

            st.success(d)

            st.write("Doctor:",data["doctor"])

            st.write("Advice:",data["advice"])

# --------------------------------------------------
# RISK TIMELINE
# --------------------------------------------------

elif page=="📊 Patient Risk Timeline":

    st.title("Patient Risk Timeline")

    diseases=st.multiselect("Select Diseases",list(DISEASE_DATABASE.keys()))

    custom=st.text_input("Add Other Diseases")

    surgery=st.selectbox("Any Past Surgery?",["No","Yes"])

    if surgery=="Yes":

        surgery_name=st.text_input("Surgery Name")

        duration=st.number_input("Duration",1)

        unit=st.selectbox("Unit",["Days","Weeks","Months","Years"])

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

        risks=[base+i*3 for i in range(5)]

        st.session_state.risk=risks[-1]

        fig=plt.figure()

        plt.plot(years,risks,marker="o")

        st.pyplot(fig)

# --------------------------------------------------
# REPORT
# --------------------------------------------------

elif page=="📑 AI Medical Report":

    st.title("AI Medical Report")

    name=st.text_input("Patient Name")

    if st.button("Generate Report"):

        pred=st.session_state.get("predicted",[])

        symptoms=st.session_state.get("symptoms",[])

        risk=st.session_state.get("risk","Unknown")

        explanation=""

        for d in pred:

            explanation+=f"{d} predicted due to symptoms overlap.\n"

        text=f"""
Patient: {name}

Predicted Diseases: {pred}

Matched Symptoms: {symptoms}

Risk Score: {risk}

Explanation:
{explanation}

Recommended next steps:
Consult specialists and follow preventive care.
"""

        styles=getSampleStyleSheet()

        file=tempfile.NamedTemporaryFile(delete=False)

        doc=SimpleDocTemplate(file.name)

        story=[Paragraph("AI Medical Report",styles['Title']),
        Spacer(1,20),
        Paragraph(text,styles['BodyText'])]

        doc.build(story)

        with open(file.name,"rb") as f:
            st.download_button("Download Report",f,"AI_Report.pdf")

# --------------------------------------------------
# CHAT
# --------------------------------------------------

elif page=="💬 AI Medical Assistant":

    st.title("AI Medical Assistant")

    q=st.text_input("Ask a health question")

    if st.button("Ask"):

        st.info("Connect GPT API here")

# --------------------------------------------------
# DOCTOR RECOMMENDATION
# --------------------------------------------------

elif page=="👨‍⚕ Doctor Recommendation":

    st.title("Doctor Recommendation")

    disease=st.selectbox("Select Disease",list(DISEASE_DATABASE.keys()))

    if disease:

        data=DISEASE_DATABASE[disease]

        st.markdown(f"""
<div class="doctor-card">

<b>Consult:</b> {data["doctor"]}

<br><br>

<b>Advice:</b> {data["advice"]}

</div>
""",unsafe_allow_html=True)


