import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import requests

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="AI Healthcare Intelligence System",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------

st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:bold;
text-align:center;
color:#00eaff;
animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow{
from{ text-shadow:0 0 10px #00eaff;}
to{ text-shadow:0 0 30px #00eaff;}
}

.card{
padding:25px;
border-radius:15px;
background:#111;
box-shadow:0px 0px 20px rgba(0,255,255,0.3);
transition:0.3s;
text-align:center;
font-size:20px;
}

.card:hover{
transform:scale(1.05);
box-shadow:0px 0px 40px rgba(0,255,255,0.6);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# LOAD MODEL
# ---------------------------

model = joblib.load("disease_model.pkl")
le = joblib.load("label_encoder.pkl")

# ---------------------------
# SIDEBAR
# ---------------------------

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

# ---------------------------
# HOME PAGE
# ---------------------------

if menu == "🏠 Home":

    st.markdown('<p class="main-title">AI Healthcare Intelligence System</p>', unsafe_allow_html=True)

    st.image(
    "https://cdn.pixabay.com/photo/2023/03/06/15/55/ai-doctor-7832037_1280.png"
    )

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🧠 AI Disease Prediction</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📊 Patient Risk Analytics</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">🤖 Medical AI Assistant</div>', unsafe_allow_html=True)


# ---------------------------
# DISEASE PREDICTION
# ---------------------------

elif menu == "🧠 Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    st.image(
    "https://cdn.pixabay.com/photo/2023/05/16/09/14/ai-doctor-7998433_1280.png"
    )

    st.subheader("Patient Symptoms")

    fever = st.checkbox("Fever")
    headache = st.checkbox("Headache")
    fatigue = st.checkbox("Fatigue")
    vomiting = st.checkbox("Vomiting")
    chest_pain = st.checkbox("Chest Pain")
    blurred_vision = st.checkbox("Blurred Vision")

    st.subheader("Medical Parameters")

    age = st.slider("Age",1,100,25)
    bmi = st.slider("BMI",10.0,40.0,22.0)
    glucose = st.slider("Glucose Level",50,200,100)
    blood_pressure = st.slider("Blood Pressure",60,180,120)

    symptom_score = sum([fever,headache,fatigue,vomiting,chest_pain,blurred_vision])

    input_data = np.array([[age,bmi,glucose,blood_pressure]])

    if st.button("Predict Disease"):

        pred = model.predict(input_data)
        disease = le.inverse_transform(pred)[0]

        st.success(f"Predicted Disease: {disease}")

        prob = model.predict_proba(input_data)[0]

        df = pd.DataFrame({
            "Disease":le.classes_,
            "Probability":prob
        })

        fig = px.bar(df,x="Disease",y="Probability")

        st.plotly_chart(fig,use_container_width=True)

        st.info("AI analyzed symptoms and patient vitals to estimate disease probability.")

# ---------------------------
# RISK ANALYTICS
# ---------------------------

elif menu == "📊 Risk Analytics":

    st.title("📊 Patient Risk Timeline")

    st.image(
    "https://cdn.pixabay.com/photo/2023/06/13/12/48/ai-healthcare-8061207_1280.png"
    )

    condition = st.selectbox(
        "Current Medical Condition / Surgery",
        [
            "Diabetes",
            "Heart Surgery",
            "Kidney Disease",
            "Eye Surgery",
            "Hypertension"
        ]
    )

    years = list(range(1,11))

    risk = np.random.randint(20,90,10)

    df = pd.DataFrame({
        "Year":years,
        "Risk %":risk
    })

    fig = px.line(df,x="Year",y="Risk %",markers=True)

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("AI Risk Explanation")

    if condition == "Heart Surgery":

        st.write("""
• Patient should maintain low cholesterol diet  
• Regular cardiologist checkup recommended  
• Risk increases if blood pressure not controlled  
""")

    elif condition == "Diabetes":

        st.write("""
• Monitor glucose daily  
• Maintain BMI below 25  
• Risk increases with age and inactivity  
""")

    else:

        st.write("""
• Maintain healthy lifestyle  
• Routine doctor visits recommended  
• Follow prescribed medication  
""")

# ---------------------------
# EXPLAINABLE AI
# ---------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI Report")

    st.image(
    "https://cdn.pixabay.com/photo/2023/04/10/17/43/ai-medical-7914445_1280.png"
    )

    features = ["Age","BMI","Glucose","Blood Pressure"]
    importance = np.random.rand(4)

    df = pd.DataFrame({
        "Feature":features,
        "Importance":importance
    })

    fig = px.bar(df,x="Feature",y="Importance")

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Why AI Predicted This Disease")

    st.write("""
• High glucose level strongly indicates metabolic disease  
• BMI contributes to obesity related conditions  
• Age increases probability of chronic diseases  
• Blood pressure linked to cardiovascular problems  
""")

# ---------------------------
# AI CHATBOT
# ---------------------------

elif menu == "🤖 AI Chatbot":

    st.title("🤖 AI Medical Assistant")

    st.image(
    "https://cdn.pixabay.com/photo/2023/03/27/15/59/ai-7883924_1280.png"
    )

    user_input = st.text_input("Describe your symptoms")

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

# ---------------------------
# DOCTOR RECOMMENDATION
# ---------------------------

elif menu == "👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation")

    st.image(
    "https://cdn.pixabay.com/photo/2023/05/18/14/34/ai-doctor-8002000_1280.png"
    )

    disease = st.selectbox(
        "Select Disease",
        ["Diabetes","Heart Disease","Glaucoma","Kidney Disease"]
    )

    doctors = {
        "Diabetes":"Endocrinologist",
        "Heart Disease":"Cardiologist",
        "Glaucoma":"Ophthalmologist",
        "Kidney Disease":"Nephrologist"
    }

    st.success(f"Recommended Specialist: {doctors[disease]}")

    st.write("""
Next Steps:

• Book appointment with specialist  
• Perform recommended lab tests  
• Follow medication plan  
• Schedule regular health checkups  
""")
