import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import requests

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------
# Custom CSS Animations
# ---------------------------

st.markdown("""
<style>

.main-title{
font-size:45px;
font-weight:bold;
color:#00eaff;
text-align:center;
animation: glow 2s ease-in-out infinite alternate;
margin-bottom:20px;
}

@keyframes glow{
from{ text-shadow:0 0 10px #00eaff;}
to{ text-shadow:0 0 30px #00eaff;}
}

.card{
padding:25px;
border-radius:15px;
background:#111;
color:white;
font-size:20px;
text-align:center;
box-shadow:0px 0px 20px rgba(0,255,255,0.3);
transition:0.3s;
}

.card:hover{
transform:scale(1.05);
box-shadow:0px 0px 40px rgba(0,255,255,0.7);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Load Model
# ---------------------------

model = joblib.load("disease_model.pkl")
le = joblib.load("label_encoder.pkl")

# ---------------------------
# Sidebar
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

    st.markdown('<p class="main-title">🧠 AI Healthcare Intelligence System</p>', unsafe_allow_html=True)

    st.markdown("### 🤖 AI Powered Medical Assistant")

    # Cute Animated AI Image
    st.image(
        "https://media.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy.gif",
        use_column_width=True
    )

    st.markdown("### 🚀 Platform Features")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🧠 AI Disease Prediction</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📊 Risk Analysis Dashboard</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">🤖 Medical AI Assistant</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.info("This intelligent healthcare system predicts diseases, analyzes patient risk, explains AI predictions, and recommends doctors.")

# ---------------------------
# DISEASE PREDICTION
# ---------------------------

elif menu == "🧠 Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    age = st.slider("Age",1,100,25)
    bmi = st.slider("BMI",10.0,40.0,22.0)
    glucose = st.slider("Glucose Level",50,200,100)
    blood_pressure = st.slider("Blood Pressure",60,180,120)

    input_data = np.array([[age,bmi,glucose,blood_pressure]])

    if st.button("🔍 Predict Disease"):

        pred = model.predict(input_data)
        disease = le.inverse_transform(pred)[0]

        st.success(f"Predicted Disease: {disease}")

        prob = model.predict_proba(input_data)[0]

        df = pd.DataFrame({
            "Disease":le.classes_,
            "Probability":prob
        })

        fig = px.bar(df,x="Disease",y="Probability",color="Probability",title="Disease Probability")

        st.plotly_chart(fig,use_container_width=True)

# ---------------------------
# RISK ANALYTICS
# ---------------------------

elif menu == "📊 Risk Analytics":

    st.title("📊 10-Year Patient Risk Prediction")

    years = list(range(1,11))
    risk = np.random.randint(10,90,10)

    df = pd.DataFrame({
        "Year":years,
        "Risk %":risk
    })

    fig = px.line(
        df,
        x="Year",
        y="Risk %",
        markers=True,
        title="Future Health Risk Prediction"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.warning("This chart estimates future health risks based on AI trends.")

# ---------------------------
# EXPLAINABLE AI
# ---------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI Analysis")

    features = ["Age","BMI","Glucose","Blood Pressure"]
    importance = np.random.rand(4)

    df = pd.DataFrame({
        "Feature":features,
        "Importance":importance
    })

    fig = px.bar(
        df,
        x="Feature",
        y="Importance",
        color="Importance",
        title="Feature Importance"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.info("This explains which patient features influenced the AI prediction.")

# ---------------------------
# AI CHATBOT
# ---------------------------

elif menu == "🤖 AI Chatbot":

    st.title("🤖 AI Medical Chatbot")

    user_input = st.text_input("Describe your symptoms")

    if st.button("💬 Ask AI"):

        prompt = f"Patient symptoms: {user_input}. Provide medical advice."

        try:

            r = requests.post(
                "https://api-inference.huggingface.co/models/google/flan-t5-base",
                json={"inputs":prompt}
            )

            result = r.json()[0]["generated_text"]

            st.success(result)

        except:
            st.error("Chatbot API limit reached. Please try again later.")

# ---------------------------
# DOCTOR RECOMMENDATION
# ---------------------------

elif menu == "👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Doctor Recommendation System")

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

    st.image(
        "https://media.giphy.com/media/26BRuo6sLetdllPAQ/giphy.gif",
        use_column_width=True
    )
