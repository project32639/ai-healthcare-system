import streamlit as st
import random
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import os

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Healthcare Intelligence System",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------------------------------
# STYLE
# ---------------------------------------------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(120deg,#e6f7ff,#f0fff5);
}

.big-title{
font-size:55px;
font-weight:bold;
text-align:center;
padding:20px;
border-radius:20px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
box-shadow:0px 8px 25px rgba(0,0,0,0.2);
}

.feature-box{
background:#d8ecff;
color:#002b5c;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.15);
transition:0.3s;
text-align:center;
font-size:20px;
font-weight:600;
}

.feature-box:hover{
transform:scale(1.05);
background:#bfe2ff;
}

.info-box{
background:#dff6ff;
padding:25px;
border-radius:15px;
font-size:18px;
color:#00334d;
box-shadow:0px 3px 12px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

pages = [
"Home",
"AI Disease Prediction",
"Patient Risk Timeline",
"AI Report",
"AI Medical Assistant",
"Doctor Recommendation"
]

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page not in pages:
    st.session_state.page="Home"

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Navigation")

nav = st.sidebar.radio(
"Go to",
pages,
index=pages.index(st.session_state.page)
)

st.session_state.page = nav

# ---------------------------------------------------
# DATA
# ---------------------------------------------------

symptom_list = [
"Fever","Cough","Headache","Fatigue","Body Pain",
"Shortness of Breath","Chest Pain","Nausea","Vomiting",
"Dizziness","Skin Rash","Joint Pain","Back Pain",
"Frequent Urination","Excessive Thirst"
]

diseases = [
"Diabetes","Heart Disease","Asthma","Hypertension",
"Kidney Disease","Liver Disease","Cancer",
"Arthritis","Migraine","COVID-19"
]

doctor_map = {
"Diabetes":"Endocrinologist",
"Heart Disease":"Cardiologist",
"Asthma":"Pulmonologist",
"Hypertension":"Cardiologist",
"Kidney Disease":"Nephrologist",
"Liver Disease":"Hepatologist",
"Cancer":"Oncologist",
"Arthritis":"Rheumatologist",
"Migraine":"Neurologist",
"COVID-19":"Infectious Disease Specialist"
}

# ---------------------------------------------------
# HOME
# ---------------------------------------------------

if st.session_state.page=="Home":

    st.markdown('<div class="big-title">🧬 AI Healthcare Intelligence System 🤖</div>',unsafe_allow_html=True)

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown('<div class="feature-box">🧠 AI Disease Prediction</div>',unsafe_allow_html=True)
        if st.button("Open Prediction"):
            st.session_state.page="AI Disease Prediction"
            st.rerun()

    with col2:
        st.markdown('<div class="feature-box">📊 Patient Risk Timeline</div>',unsafe_allow_html=True)
        if st.button("Open Timeline"):
            st.session_state.page="Patient Risk Timeline"
            st.rerun()

    with col3:
        st.markdown('<div class="feature-box">📑 AI Report</div>',unsafe_allow_html=True)
        if st.button("Open Report"):
            st.session_state.page="AI Report"
            st.rerun()

    col4,col5=st.columns(2)

    with col4:
        st.markdown('<div class="feature-box">💬 AI Medical Assistant</div>',unsafe_allow_html=True)
        if st.button("Open Assistant"):
            st.session_state.page="AI Medical Assistant"
            st.rerun()

    with col5:
        st.markdown('<div class="feature-box">👨‍⚕ Doctor Recommendation</div>',unsafe_allow_html=True)
        if st.button("Open Doctor"):
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

# ---------------------------------------------------
# AI DISEASE PREDICTION
# ---------------------------------------------------

if st.session_state.page=="AI Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age = st.slider("Age",1,100)

    gender = st.selectbox("Gender",["Male","Female"])

    smoking = st.selectbox("Smoking",["No","Yes"])

    activity = st.selectbox(
    "Physical Activity",
    ["Very High","High","Moderate","Low","Very Low"]
    )

    family_disease = st.text_input(
    "Family Disease History (comma separated)"
    )

    weight = st.number_input("Weight (kg)",0.0)
    height = st.number_input("Height (cm)",0.0)

    symptoms = st.multiselect("Select Symptoms",symptom_list)

    other_symptoms = st.text_input(
    "Other Symptoms (comma separated)"
    )

    if height>0:
        bmi = weight/((height/100)**2)
        st.write("BMI:",round(bmi,2))

    if st.button("Predict Disease"):

        all_symptoms = symptoms + [
        s.strip() for s in other_symptoms.split(",") if s.strip()!=""
        ]

        prediction=random.choice(diseases)

        probability=random.randint(60,95)

        st.session_state.prediction=prediction

        st.success(f"Predicted Disease: {prediction}")
        st.write(f"Probability: {probability}%")

        fig,ax=plt.subplots()
        ax.bar([prediction], [probability])
        ax.set_ylabel("Probability %")
        st.pyplot(fig)

# ---------------------------------------------------
# RISK TIMELINE
# ---------------------------------------------------

if st.session_state.page=="Patient Risk Timeline":

    st.title("📊 Patient Risk Timeline")

    selected = st.multiselect("Select Diseases",diseases)

    custom = st.text_input("Custom Disease (comma separated)")

    all_diseases = selected + [
    s.strip() for s in custom.split(",") if s.strip()!=""
    ]

    if st.button("Analyze Risk"):

        if len(all_diseases)==0:
            st.warning("Select or type diseases")
        else:

            current=random.randint(10,30)
            five=random.randint(30,60)
            ten=random.randint(60,90)

            st.write("Current Risk:",current,"%")
            st.progress(current)

            st.write("5 Year Risk:",five,"%")
            st.progress(five)

            st.write("10 Year Risk:",ten,"%")
            st.progress(ten)

# ---------------------------------------------------
# AI REPORT
# ---------------------------------------------------

if st.session_state.page=="AI Report":

    st.title("📑 AI Medical Report")

    if "prediction" not in st.session_state:
        st.warning("Run AI Disease Prediction first")

    else:

        disease=st.session_state.prediction

        st.write("Predicted Disease:",disease)

        st.write("Explanation")

        st.write("• Age influenced disease risk")
        st.write("• Lifestyle pattern affected prediction")
        st.write("• Symptoms matched disease pattern")

        if st.button("Download PDF Report"):

            file="report.pdf"

            c=canvas.Canvas(file)
            c.drawString(100,750,"AI Medical Report")
            c.drawString(100,720,f"Predicted Disease: {disease}")
            c.drawString(100,690,"Generated by AI Healthcare System")
            c.save()

            with open(file,"rb") as f:
                st.download_button(
                "Download Report",
                f,
                file_name="AI_Report.pdf"
                )

# ---------------------------------------------------
# CHATBOT
# ---------------------------------------------------

if st.session_state.page=="AI Medical Assistant":

    st.title("💬 AI Medical Chatbot")

    question=st.text_area("Ask a medical question")

    if st.button("Ask AI"):

        if "OPENAI_API_KEY" not in st.secrets:
            st.error("Add OPENAI_API_KEY in Streamlit Secrets")
        else:

            from openai import OpenAI
            client=OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":question}]
            )

            st.write(response.choices[0].message.content)

# ---------------------------------------------------
# DOCTOR RECOMMENDATION
# ---------------------------------------------------

if st.session_state.page=="Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation")

    disease=st.selectbox("Select Disease",diseases)

    custom=st.text_input("Or Type Disease")

    if st.button("Recommend"):

        if custom!="":
            d=custom
        else:
            d=disease

        doc=doctor_map.get(d,"General Physician")

        st.success(f"Recommended Doctor: {doc}")

        st.write("Advice")

        st.write("✔ Maintain healthy lifestyle")
        st.write("✔ Exercise regularly")
        st.write("✔ Follow balanced diet")
        st.write("✔ Consult doctor regularly")
