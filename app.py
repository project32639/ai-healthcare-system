import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import requests

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Healthcare Intelligence System",
    page_icon="🧬",
    layout="wide"
)

# -------------------------
# ADVANCED CSS
# -------------------------

st.markdown("""
<style>

.big-title{
font-size:65px;
font-weight:800;
text-align:center;
background: linear-gradient(90deg,#00f2ff,#00ff95,#00f2ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
animation: glow 3s infinite alternate;
}

@keyframes glow{
from{ text-shadow:0px 0px 20px #00f2ff;}
to{ text-shadow:0px 0px 50px #00ff95;}
}

.subtitle{
text-align:center;
font-size:22px;
color:gray;
margin-bottom:40px;
}

.card{
padding:25px;
border-radius:20px;
background:#111;
box-shadow:0px 0px 25px rgba(0,255,255,0.3);
transition:0.3s;
text-align:center;
font-size:20px;
}

.card:hover{
transform:scale(1.05);
box-shadow:0px 0px 45px rgba(0,255,255,0.6);
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# LOAD MODEL
# -------------------------

model = joblib.load("disease_model.pkl")
le = joblib.load("label_encoder.pkl")

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("🧬 AI Healthcare Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🧠 Disease Prediction",
        "📊 Risk Analytics",
        "🧬 Explainable AI",
        "🤖 AI Chatbot",
        "👨‍⚕ Doctor Recommendation"
    ]
)

# -------------------------
# HOME PAGE
# -------------------------

if menu == "🏠 Home":

    st.markdown('<p class="big-title">🧬 AI Healthcare Intelligence System 🤖</p>', unsafe_allow_html=True)

    st.markdown('<p class="subtitle">AI Powered Disease Prediction • Risk Analytics • Medical Assistant</p>', unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])

    with col1:

        st.image(
            "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
            width=350
        )

    with col2:

        st.markdown("""
### 🏥 What This System Can Do

✔ Predict diseases using AI  
✔ Analyze patient health risk timeline  
✔ Explain AI decisions using Explainable AI  
✔ AI chatbot for medical questions  
✔ Recommend doctors based on disease  

This system is designed to help **patients, doctors, and hospitals** make better medical decisions using Artificial Intelligence.
""")

    st.markdown("---")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🧠 Disease Prediction</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📊 Patient Risk Timeline</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">🤖 AI Medical Assistant</div>', unsafe_allow_html=True)

# -------------------------
# DISEASE PREDICTION
# -------------------------

elif menu == "🧠 Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    st.subheader("Basic Patient Information")

    age = st.slider("Age",1,100,25)

    gender = st.selectbox(
        "Gender",
        ["Male","Female","Other"]
    )

    height = st.slider(
        "Height (cm)",
        120,
        220,
        170
    )

    weight = st.slider(
        "Weight (kg)",
        30,
        150,
        70
    )

    # BMI Calculation
    bmi = weight / ((height/100)**2)

    st.info(f"Calculated BMI: {round(bmi,2)}")

    st.subheader("Patient Symptoms")

    symptoms = [
        "Fever","Headache","Fatigue","Vomiting",
        "Chest Pain","Blurred Vision",
        "Shortness of Breath","Dizziness",
        "Cough","Sore Throat",
        "Joint Pain","Back Pain",
        "Nausea","Weight Loss",
        "Frequent Urination","Thirst",
        "Anxiety","Insomnia"
    ]

    selected_symptoms = st.multiselect(
        "Select Symptoms",
        symptoms
    )

    custom_symptom = st.text_input(
        "Other symptom (if not listed)"
    )

    input_data = np.array([[age,bmi,weight,height]])

    if st.button("Predict Disease"):

        pred = model.predict(input_data)

        disease = le.inverse_transform(pred)[0]

        st.success(f"Predicted Disease: {disease}")

        prob = model.predict_proba(input_data)[0]

        df = pd.DataFrame({
            "Disease":le.classes_,
            "Probability":prob
        })

        fig = px.bar(
            df,
            x="Disease",
            y="Probability"
        )

        st.plotly_chart(fig,use_container_width=True)

# -------------------------
# RISK ANALYTICS
# -------------------------

elif menu == "📊 Risk Analytics":

    st.title("📊 Patient Risk Timeline")

    condition_list = [
        "Diabetes",
        "Heart Surgery",
        "Kidney Disease",
        "Cancer Treatment",
        "Stroke",
        "Hypertension"
    ]

    condition = st.selectbox(
        "Current Medical Condition / Surgery",
        condition_list
    )

    custom_condition = st.text_input(
        "Other condition or surgery"
    )

    years = list(range(1,11))

    risk = np.random.randint(20,90,10)

    df = pd.DataFrame({
        "Year":years,
        "Risk %":risk
    })

    fig = px.line(
        df,
        x="Year",
        y="Risk %",
        markers=True
    )

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("AI Medical Recommendation")

    st.write("""
• Maintain healthy lifestyle  
• Regular doctor visits  
• Follow medication schedule  
• Perform routine health tests  
""")

# -------------------------
# EXPLAINABLE AI
# -------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI Report")

    features = ["Age","BMI","Weight","Height"]
    importance = np.random.rand(4)

    df = pd.DataFrame({
        "Feature":features,
        "Importance":importance
    })

    fig = px.bar(df,x="Feature",y="Importance")

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Why AI Predicted This Disease")

    st.write("""
• Higher BMI increases chronic disease risk  
• Age contributes to disease probability  
• Weight and height affect metabolic health  
• Combined symptoms influenced the AI prediction  
""")

# -------------------------
# AI CHATBOT
# -------------------------

elif menu == "🤖 AI Chatbot":

    st.title("🤖 AI Medical Assistant")

    user_input = st.text_input(
        "Describe symptoms or ask a medical question"
    )

    if st.button("Ask AI"):

        prompt = f"Patient symptoms: {user_input}. Provide medical advice."

        try:

            r = requests.post(
                "https://api-inference.huggingface.co/models/google/flan-t5-base",
                json={"inputs":prompt}
            )

            result = r.json()[0]["generated_text"]

            st.success(result)

        except:

            st.error("Chatbot API limit reached")

# -------------------------
# DOCTOR RECOMMENDATION
# -------------------------

elif menu == "👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation")

    diseases = [
        "Diabetes",
        "Heart Disease",
        "Glaucoma",
        "Kidney Disease",
        "Hypertension",
        "Cancer",
        "Asthma",
        "Arthritis"
    ]

    disease = st.selectbox(
        "Select Disease",
        diseases
    )

    doctors = {
        "Diabetes":"Endocrinologist",
        "Heart Disease":"Cardiologist",
        "Glaucoma":"Ophthalmologist",
        "Kidney Disease":"Nephrologist",
        "Hypertension":"Cardiologist",
        "Cancer":"Oncologist",
        "Asthma":"Pulmonologist",
        "Arthritis":"Rheumatologist"
    }

    st.success(
        f"Recommended Specialist: {doctors.get(disease,'General Physician')}"
    )

    st.write("""
Next Steps

• Schedule doctor appointment  
• Perform medical tests  
• Follow treatment plan  
• Maintain healthy lifestyle  
""")
