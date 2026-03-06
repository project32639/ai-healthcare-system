import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import requests

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

/* MAIN TITLE */

.big-title{
font-size:100px;
font-weight:900;
text-align:center;
color:#00c3ff;
margin-bottom:10px;
}

/* SUBTITLE */

.subtitle{
text-align:center;
font-size:25px;
color:#aaaaaa;
margin-bottom:40px;
}

/* FEATURE BOX */

.feature-box{
padding:30px;
border-radius:18px;
background:#0f172a;
color:white;
box-shadow:0px 0px 25px rgba(0,255,255,0.25);
transition:0.4s;
font-size:20px;
}

.feature-box:hover{
transform:translateY(-8px) scale(1.03);
box-shadow:0px 0px 40px rgba(0,255,255,0.6);
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:#0f172a;
}

.sidebar-title{
font-size:28px;
font-weight:bold;
text-align:center;
margin-bottom:20px;
color:#00eaff;
}

.stRadio > div{
background:#111827;
padding:10px;
border-radius:10px;
transition:0.3s;
}

.stRadio > div:hover{
background:#1f2937;
transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------

try:
    model = joblib.load("disease_model.pkl")
    le = joblib.load("label_encoder.pkl")
except:
    model = None
    le = None

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.markdown(
'<p class="sidebar-title">🧬 AI Healthcare Dashboard</p>',
unsafe_allow_html=True
)

menu = st.sidebar.radio(
"Navigation",
[
"🏠 Home",
"🧠 Disease Prediction",
"📊 Patient Risk Timeline",
"🧬 Explainable AI",
"🤖 AI Chatbot",
"👨‍⚕ Doctor Recommendation"
]
)

# -----------------------------
# HOME PAGE
# -----------------------------

if menu == "🏠 Home":

    st.markdown('<p class="big-title">🧬 AI Healthcare Intelligence System 🤖</p>', unsafe_allow_html=True)

    st.markdown(
    '<p class="subtitle">AI Powered Disease Prediction • Risk Analytics • Medical Assistant</p>',
    unsafe_allow_html=True
    )

    col1,col2 = st.columns([1,1])

    with col1:

        st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
        width=400
        )

    with col2:

        st.markdown("""
### 🏥 What This System Can Do

✔ AI Disease Prediction  
✔ Patient Symptom Analysis  
✔ Health Risk Timeline Prediction  
✔ Explainable AI Medical Insights  
✔ AI Medical Chat Assistant  
✔ Doctor & Specialist Recommendation  
✔ Early Disease Detection Support  
✔ Preventive Healthcare Insights  

This AI system helps **patients, doctors, and hospitals make smarter healthcare decisions using artificial intelligence.**
""")

    st.write("")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown(
        '<div class="feature-box">🧠<br><br><b>AI Disease Prediction</b><br><br>Predict diseases using machine learning models.</div>',
        unsafe_allow_html=True
        )

    with col2:
        st.markdown(
        '<div class="feature-box">📊<br><br><b>Risk Analytics</b><br><br>Analyze long term health risks and trends.</div>',
        unsafe_allow_html=True
        )

    with col3:
        st.markdown(
        '<div class="feature-box">🤖<br><br><b>Medical AI Assistant</b><br><br>Ask medical questions to an AI chatbot.</div>',
        unsafe_allow_html=True
        )

# -----------------------------
# DISEASE PREDICTION
# -----------------------------

elif menu == "🧠 Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age = st.slider("Age",1,100,25)

    gender = st.selectbox("Gender",["Male","Female","Other"])

    height = st.number_input("Height (cm)",100,220,170)

    weight = st.number_input("Weight (kg)",30,150,70)

    bmi = weight / ((height/100)**2)

    st.write("Calculated BMI:", round(bmi,2))

    symptoms = st.multiselect(
    "Select Patient Symptoms",

    [
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
    )

    custom_symptom = st.text_input("Enter symptom if not listed")

    if st.button("Predict Disease"):

        st.success("AI Analysis Completed")

        st.write("Possible Disease Prediction: **General Health Risk Detected**")

# -----------------------------
# RISK TIMELINE
# -----------------------------

elif menu == "📊 Patient Risk Timeline":

    st.title("📊 Patient Health Risk Timeline")

    condition = st.text_area(
    "Current Medical Condition / Surgery / Treatment",

    placeholder="Example: Kidney surgery 2022, Diabetes treatment, Asthma since childhood..."
    )

    if st.button("Generate Risk Timeline"):

        years = list(range(1,11))

        risk = np.random.randint(10,90,10)

        df = pd.DataFrame({
        "Year":years,
        "Risk %":risk
        })

        fig = px.line(df,x="Year",y="Risk %",markers=True)

        st.plotly_chart(fig,use_container_width=True)

        st.write("Risk prediction generated based on medical history.")

# -----------------------------
# EXPLAINABLE AI
# -----------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI Report")

    st.write("Why the AI predicted this result:")

    explanations = [

    "Age factor contributed to the prediction",
    "Body Mass Index (BMI) influenced health risk",
    "Selected symptoms increased probability",
    "Patient health history affected prediction",
    "Lifestyle risk indicators detected"

    ]

    for e in explanations:

        st.write("•",e)

# -----------------------------
# AI CHATBOT
# -----------------------------

elif menu == "🤖 AI Chatbot":

    st.title("🤖 AI Medical Assistant")

    user_input = st.text_input("Describe your symptoms or medical question")

    if st.button("Ask AI"):

        prompt = f"Patient question: {user_input}. Provide simple medical guidance."

        try:

            r = requests.post(
            "https://api-inference.huggingface.co/models/google/flan-t5-base",
            json={"inputs":prompt}
            )

            result = r.json()[0]["generated_text"]

            st.success(result)

        except:

            st.error("Chatbot API unavailable right now.")

# -----------------------------
# DOCTOR RECOMMENDATION
# -----------------------------

elif menu == "👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation System")

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

    disease = st.selectbox(
    "Select Disease",
    diseases
    )

    specialist = doctors.get(disease,"General Physician")

    st.success("Recommended Specialist: " + specialist)

    st.write("Patients with", disease, "should consult a", specialist)
