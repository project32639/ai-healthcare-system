import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
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
font-size:40px;
font-weight:bold;
color:#00c3ff;
text-align:center;
animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow{
from{ text-shadow:0 0 10px #00c3ff;}
to{ text-shadow:0 0 25px #00c3ff;}
}

.card{
padding:20px;
border-radius:15px;
background:#111;
box-shadow:0px 0px 20px rgba(0,255,255,0.3);
transition:0.3s;
}

.card:hover{
transform:scale(1.03);
box-shadow:0px 0px 40px rgba(0,255,255,0.6);
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

    st.markdown('<p class="main-title">AI Healthcare Intelligence System</p>', unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1581595219315-a187dd40c322", use_column_width=True)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🧠 AI Disease Prediction</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📊 Risk Analysis Dashboard</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">🤖 Medical AI Assistant</div>', unsafe_allow_html=True)

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

    if st.button("Predict Disease"):

        pred = model.predict(input_data)
        disease = le.inverse_transform(pred)[0]

        st.success(f"Predicted Disease: {disease}")

        prob = model.predict_proba(input_data)[0]

        df = pd.DataFrame({
            "Disease":le.classes_,
            "Probability":prob
        })

        fig = px.bar(df,x="Disease",y="Probability",color="Probability")

        st.plotly_chart(fig,use_container_width=True)

# ---------------------------
# RISK ANALYTICS
# ---------------------------

elif menu == "📊 Risk Analytics":

    st.title("📊 10-Year Risk Prediction")

    years = list(range(1,11))
    risk = np.random.randint(10,90,10)

    df = pd.DataFrame({
        "Year":years,
        "Risk %":risk
    })

    fig = px.line(df,x="Year",y="Risk %",markers=True)

    st.plotly_chart(fig,use_container_width=True)

# ---------------------------
# EXPLAINABLE AI
# ---------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI")

    features = ["Age","BMI","Glucose","Blood Pressure"]
    importance = np.random.rand(4)

    df = pd.DataFrame({
        "Feature":features,
        "Importance":importance
    })

    fig = px.bar(df,x="Feature",y="Importance",color="Importance")

    st.plotly_chart(fig,use_container_width=True)

    st.info("This graph shows which patient features influenced the prediction.")

# ---------------------------
# AI CHATBOT
# ---------------------------

elif menu == "🤖 AI Chatbot":

    st.title("🤖 Medical AI Assistant")

    user_input = st.text_input("Describe your symptoms")

    if st.button("Ask AI"):

        prompt = f"Patient symptoms: {user_input}. Give medical advice."

        try:
            r = requests.post(
                "https://api-inference.huggingface.co/models/google/flan-t5-base",
                json={"inputs":prompt}
            )

            result = r.json()[0]["generated_text"]

            st.success(result)

        except:
            st.error("Chatbot API limit reached.")

# ---------------------------
# DOCTOR RECOMMENDATION
# ---------------------------

elif menu == "👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Find Specialist")

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

    st.image("https://images.unsplash.com/photo-1576091160550-2173dba999ef")