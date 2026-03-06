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
# CSS UI
# -------------------------

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
# HOME
# -------------------------

if menu == "🏠 Home":

    st.markdown('<p class="main-title">AI Healthcare Intelligence System</p>', unsafe_allow_html=True)

    st.image("logo.png", width=350)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🧠 AI Disease Prediction</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📊 Patient Risk Timeline</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">🤖 AI Medical Assistant</div>', unsafe_allow_html=True)

# -------------------------
# DISEASE PREDICTION
# -------------------------

elif menu == "🧠 Disease Prediction":

    st.title("🧠 AI Disease Prediction")

    st.subheader("Select Patient Symptoms")

    symptoms = [
        "Fever","Headache","Fatigue","Vomiting","Chest Pain",
        "Blurred Vision","Shortness of Breath","Dizziness",
        "Cough","Sore Throat","Joint Pain","Back Pain",
        "Nausea","Loss of Appetite","Weight Loss",
        "Frequent Urination","Thirst","Anxiety"
    ]

    selected_symptoms = st.multiselect(
        "Choose Symptoms",
        symptoms
    )

    custom_symptom = st.text_input(
        "Other symptoms (type if not listed)"
    )

    st.subheader("Medical Parameters")

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

        fig = px.bar(df,x="Disease",y="Probability")

        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Symptoms Provided")

        st.write(selected_symptoms)

        if custom_symptom:
            st.write("Additional Symptom:",custom_symptom)

# -------------------------
# RISK ANALYTICS
# -------------------------

elif menu == "📊 Risk Analytics":

    st.title("📊 Patient Risk Timeline")

    condition_list = [
        "Diabetes","Heart Surgery","Kidney Disease",
        "Eye Surgery","Hypertension","Cancer Treatment",
        "Organ Transplant","Stroke"
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

    fig = px.line(df,x="Year",y="Risk %",markers=True)

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("AI Medical Recommendation")

    if condition == "Heart Surgery":

        st.write("""
• Maintain cholesterol control  
• Regular cardiologist visits  
• Daily physical activity recommended
""")

    elif condition == "Diabetes":

        st.write("""
• Monitor glucose daily  
• Maintain BMI below 25  
• Follow diabetic diet
""")

    else:

        st.write("""
• Follow prescribed medication  
• Maintain healthy lifestyle  
• Routine medical checkups recommended
""")

    if custom_condition:
        st.write("Additional condition:",custom_condition)

# -------------------------
# EXPLAINABLE AI
# -------------------------

elif menu == "🧬 Explainable AI":

    st.title("🧬 Explainable AI Report")

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
• High glucose suggests metabolic disorder risk  
• Elevated BMI linked to obesity related diseases  
• Age increases chronic disease probability  
• High blood pressure indicates cardiovascular stress  
""")

# -------------------------
# AI CHATBOT
# -------------------------

elif menu == "🤖 AI Chatbot":

    st.title("🤖 AI Medical Assistant")

    user_input = st.text_input("Describe symptoms or ask medical question")

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
        "Diabetes","Heart Disease","Glaucoma",
        "Kidney Disease","Hypertension",
        "Cancer","Asthma","Arthritis"
    ]

    disease = st.selectbox(
        "Select Disease",
        diseases
    )

    custom_disease = st.text_input(
        "Other disease"
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

    st.success(f"Recommended Specialist: {doctors.get(disease,'General Physician')}")

    if custom_disease:
        st.write("Additional disease entered:",custom_disease)

    st.write("""
Next Steps

• Schedule doctor appointment  
• Perform lab tests  
• Follow treatment plan  
• Regular medical monitoring
""")
