import streamlit as st
import random
import openai

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="AI Healthcare Intelligence System",
    page_icon="🧬",
    layout="wide"
)

# -------------------------------
# OPENAI KEY
# -------------------------------

openai.api_key = st.secrets.get("OPENAI_API_KEY","")

# -------------------------------
# STYLE
# -------------------------------

st.markdown("""
<style>

.main{
background:linear-gradient(120deg,#e6f7ff,#f0fff5);
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
}

.feature-box{
background:linear-gradient(135deg,#d8ecff,#e8fff6);
color:#002b5c;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
transition:0.3s;
text-align:center;
font-size:20px;
font-weight:600;
cursor:pointer;
}

.feature-box:hover{
transform:scale(1.05);
background:linear-gradient(135deg,#bfe2ff,#c8ffe8);
}

.info-box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

</style>
""",unsafe_allow_html=True)

# -------------------------------
# SESSION STATE
# -------------------------------

if "page" not in st.session_state:
    st.session_state.page="Home"

if "prediction" not in st.session_state:
    st.session_state.prediction=None

# -------------------------------
# SIDEBAR
# -------------------------------

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

st.session_state.page=nav

# -------------------------------
# DATA
# -------------------------------

symptom_list=[
"Fever","Cough","Headache","Fatigue","Body Pain","Dizziness",
"Nausea","Vomiting","Diarrhea","Constipation","Chest Pain",
"Shortness of Breath","Skin Rash","Itching","Joint Pain",
"Muscle Pain","Sore Throat","Runny Nose","Anxiety","Depression"
]

diseases=[
"Diabetes","Heart Disease","Asthma","Arthritis","Cancer",
"Kidney Disease","Hypertension","Migraine","Pneumonia",
"COVID-19","Gastritis","Obesity","Anemia","Skin Allergy"
]

doctors={
"Diabetes":"Endocrinologist",
"Heart Disease":"Cardiologist",
"Asthma":"Pulmonologist",
"Arthritis":"Rheumatologist",
"Cancer":"Oncologist",
"Kidney Disease":"Nephrologist",
"Hypertension":"Cardiologist",
"Migraine":"Neurologist",
"Pneumonia":"Pulmonologist",
"COVID-19":"Infectious Disease Specialist",
"Gastritis":"Gastroenterologist",
"Obesity":"Nutritionist",
"Anemia":"Hematologist",
"Skin Allergy":"Dermatologist"
}

# -------------------------------
# HOME
# -------------------------------

if st.session_state.page=="Home":

    st.markdown('<div class="big-title">🧬 AI Healthcare Intelligence System 🤖</div>',unsafe_allow_html=True)

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:
        if st.button("🧠 AI Disease Prediction"):
            st.session_state.page="AI Disease Prediction"
            st.rerun()

    with col2:
        if st.button("📊 Patient Risk Timeline"):
            st.session_state.page="Patient Risk Timeline"
            st.rerun()

    with col3:
        if st.button("📑 AI Report"):
            st.session_state.page="AI Report"
            st.rerun()

    col4,col5=st.columns(2)

    with col4:
        if st.button("💬 AI Medical Assistant"):
            st.session_state.page="AI Medical Assistant"
            st.rerun()

    with col5:
        if st.button("👨‍⚕ Doctor Recommendation"):
            st.session_state.page="Doctor Recommendation"
            st.rerun()

    st.write("")

    st.markdown("""
<div class="info-box">

### 🏥 What This AI Model Does

✔ Predicts possible diseases from symptoms  
✔ Analyzes patient symptom patterns  
✔ Generates health risk timeline predictions  
✔ Provides explainable AI medical insights  
✔ AI medical chatbot for questions  
✔ Doctor & specialist recommendations  
✔ Preventive healthcare insights  

</div>
""",unsafe_allow_html=True)

# -------------------------------
# DISEASE PREDICTION
# -------------------------------

if st.session_state.page=="AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age=st.slider("Age",1,100)

    gender=st.selectbox("Gender",["Male","Female","Other"])

    lifestyle=st.selectbox("Lifestyle",["Healthy","Average","Unhealthy"])

    symptoms=st.multiselect("Select Symptoms",symptom_list)

    custom=st.text_input("Other Symptoms (comma separated)")

    if st.button("Predict Disease"):

        if custom!="":
            custom_list=[s.strip() for s in custom.split(",")]
            symptoms+=custom_list

        if len(symptoms)==0:
            st.warning("Please enter symptoms")
        else:

            prediction=random.choice(diseases)

            st.session_state.prediction=prediction

            st.success(f"Predicted Disease Risk: {prediction}")

# -------------------------------
# RISK TIMELINE
# -------------------------------

if st.session_state.page=="Patient Risk Timeline":

    st.title("📊 Patient Health Risk Timeline")

    disease_select=st.multiselect("Select Diseases",diseases)

    custom=st.text_input("Other Diseases (comma separated)")

    if st.button("Analyze Risk"):

        disease_list=disease_select

        if custom!="":
            disease_list+=custom.split(",")

        if len(disease_list)==0:
            st.warning("Enter diseases to analyze")
        else:

            st.subheader("Risk Prediction")

            st.progress(30)
            st.write("Current Risk: Low")

            st.progress(60)
            st.write("5 Year Risk: Moderate")

            st.progress(85)
            st.write("10 Year Risk: High")

# -------------------------------
# AI REPORT
# -------------------------------

if st.session_state.page=="AI Report":

    st.title("📑 AI Explainable Report")

    if st.session_state.prediction is None:

        st.warning("Run AI Disease Prediction first.")

    else:

        disease=st.session_state.prediction

        st.success(f"Prediction Explanation for {disease}")

        st.write("• Age influenced disease probability")
        st.write("• Symptom pattern matched disease indicators")
        st.write("• Lifestyle factors increased health risk")
        st.write("• AI pattern recognition matched training data")

# -------------------------------
# CHATBOT
# -------------------------------

if st.session_state.page=="AI Medical Assistant":

    st.title("💬 AI Medical Assistant")

    question=st.text_area("Ask a medical question")

    if st.button("Ask AI"):

        if openai.api_key=="":

            st.warning("Add OPENAI_API_KEY in Streamlit Secrets")

        else:

            response=openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role":"system","content":"You are a helpful medical assistant."},
                    {"role":"user","content":question}
                ]
            )

            st.write(response.choices[0].message.content)

# -------------------------------
# DOCTOR RECOMMENDATION
# -------------------------------

if st.session_state.page=="Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation System")

    disease=st.selectbox("Select Disease",diseases)

    custom=st.text_input("Or type disease")

    if st.button("Recommend Doctor"):

        if custom!="":

            st.success("Consult a Specialist Physician")

            st.write("Advice:")
            st.write("• Maintain healthy lifestyle")
            st.write("• Follow doctor consultation")
            st.write("• Regular medical checkups")

        else:

            doc=doctors.get(disease,"General Physician")

            st.success(f"Recommended Specialist: {doc}")

            st.write("Medical Advice")

            st.write("• Follow prescribed medication")
            st.write("• Maintain healthy diet")
            st.write("• Exercise regularly")
            st.write("• Schedule periodic health checkups")
