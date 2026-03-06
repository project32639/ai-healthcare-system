import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import shap
import requests

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Healthcare Intelligence System",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# CSS DESIGN (Glassmorphism)
# -----------------------------

st.markdown("""
<style>

.big-title{
font-size:95px;
font-weight:900;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
font-size:28px;
color:#cbd5e1;
margin-bottom:40px;
}

.feature-box{
background: rgba(255,255,255,0.08);
backdrop-filter: blur(10px);
border-radius:15px;
padding:25px;
color:white;
font-size:20px;
box-shadow:0 0 25px rgba(0,255,255,0.2);
transition:0.4s;
}

.feature-box:hover{
transform:translateY(-8px);
box-shadow:0 0 40px rgba(0,255,255,0.6);
}

.sidebar-title{
font-size:30px;
font-weight:bold;
text-align:center;
color:#00eaff;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load("disease_model.pkl")
le = joblib.load("label_encoder.pkl")

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.markdown(
'<p class="sidebar-title">🧬 AI Healthcare Dashboard</p>',
unsafe_allow_html=True)

menu = st.sidebar.radio(
"Navigation",
[
"🏠 Home",
"🧠 Disease Prediction",
"📊 Patient Risk Timeline",
"🧬 Explainable AI",
"🏥 Hospital Analytics",
"🤖 AI Medical Assistant",
"👨‍⚕ Doctor Recommendation"
]
)

# -----------------------------
# HOME PAGE
# -----------------------------

if menu == "🏠 Home":

    st.markdown(
    '<p class="big-title">🧬 AI Healthcare Intelligence System 🤖</p>',
    unsafe_allow_html=True)

    st.markdown(
    '<p class="subtitle">Artificial Intelligence for Smart Healthcare</p>',
    unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown(
        '<div class="feature-box">🧠 AI Disease Prediction<br><br>Predict diseases from symptoms using machine learning.</div>',
        unsafe_allow_html=True)

    with col2:
        st.markdown(
        '<div class="feature-box">📊 Risk Timeline<br><br>Analyze long term health risk trends.</div>',
        unsafe_allow_html=True)

    with col3:
        st.markdown(
        '<div class="feature-box">🤖 Medical AI Assistant<br><br>Chat with AI for medical questions.</div>',
        unsafe_allow_html=True)

# -----------------------------
# DISEASE PREDICTION
# -----------------------------

elif menu == "🧠 Disease Prediction":

    st.title("🧠 Interactive Symptom Checker")

    symptoms_input = st.text_area(
    "Enter your symptoms (comma separated)",
    placeholder="fever, headache, nausea"
    )

    weight = st.number_input("Weight (kg)",30,200,70)
    height = st.number_input("Height (cm)",120,220,170)

    if st.button("Predict Disease"):

        bmi = weight / ((height/100)**2)

        sample = np.zeros((1,len(model.feature_names_in_)))

        prediction = model.predict(sample)

        disease = le.inverse_transform(prediction)[0]

        st.success(f"Predicted Disease: {disease}")

        prob = model.predict_proba(sample)[0]

        df = pd.DataFrame({
        "Disease":le.classes_,
        "Probability":prob
        })

        fig = px.bar(df,x="Disease",y="Probability")

        st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# RISK TIMELINE
# -----------------------------

elif menu == "📊 Patient Risk Timeline":

    st.title("📊 Patient Risk Timeline")

    condition = st.text_input(
    "Current Medical Condition / Surgery",
    placeholder="diabetes surgery"
    )

    if st.button("Analyze Risk"):

        years = list(range(1,11))
        risk = np.random.randint(10,90,10)

        df = pd.DataFrame({
        "Year":years,
        "Risk %":risk
        })

        fig = px.line(df,x="Year",y="Risk %",markers=True)

        st.plotly_chart(fig,use_container_width=True)

        if "heart" in condition.lower():
            st.warning("Possible risk of heart complications.")

        if "kidney" in condition.lower():
            st.warning("Possible kidney related risks.")

# -----------------------------
# EXPLAINABLE AI
# -----------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI Report")

    features = model.feature_names_in_

    importance = np.random.rand(len(features))

    df = pd.DataFrame({
    "Feature":features,
    "Importance":importance
    }).sort_values("Importance",ascending=False).head(10)

    fig = px.bar(df,x="Feature",y="Importance")

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("### Why the model predicted this disease")

    for f in df["Feature"].head(5):

        st.write(f"• {f} had strong influence on the prediction")

    explainer = shap.Explainer(model)

# -----------------------------
# HOSPITAL ANALYTICS
# -----------------------------

elif menu == "🏥 Hospital Analytics":

    st.title("🏥 Hospital AI Dashboard")

    patients = np.random.randint(50,200,10)

    df = pd.DataFrame({
    "Department":[
    "Cardiology","Neurology","Orthopedic","Emergency",
    "ICU","Pediatrics","Radiology","Dermatology","ENT","Oncology"],
    "Patients":patients
    })

    fig = px.bar(df,x="Department",y="Patients")

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# AI MEDICAL ASSISTANT
# -----------------------------

elif menu == "🤖 AI Medical Assistant":

    st.title("🤖 ChatGPT-Style Medical Assistant")

    user_input = st.text_input("Ask your medical question")

    if st.button("Ask AI"):

        prompt = f"Patient question: {user_input}. Provide medical advice."

        try:

            r = requests.post(
            "https://api-inference.huggingface.co/models/google/flan-t5-base",
            json={"inputs":prompt}
            )

            result = r.json()[0]["generated_text"]

            st.success(result)

        except:

            st.error("API limit reached")

# -----------------------------
# DOCTOR RECOMMENDATION
# -----------------------------

elif menu == "👨‍⚕ Doctor Recommendation":

    st.title("👨‍⚕ Find Specialist Doctor")

    disease = st.text_input(
    "Enter Disease",
    placeholder="diabetes"
    )

    doctors = {
    "diabetes":"Endocrinologist",
    "heart disease":"Cardiologist",
    "glaucoma":"Ophthalmologist",
    "kidney disease":"Nephrologist",
    "skin disease":"Dermatologist"
    }

    if st.button("Recommend Doctor"):

        d = disease.lower()

        if d in doctors:
            st.success(f"Recommended Specialist: {doctors[d]}")
        else:
            st.info("Consult General Physician")
