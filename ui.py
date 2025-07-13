import streamlit as st
import numpy as np
from datetime import datetime
from tools import calculate_platelet_index, injury_risk_level

def render_ui(model, store_result, load_all_results):
    st.set_page_config(page_title="PRP Diagnosis Dashboard", layout="wide")

    st.sidebar.image("assets/logo.png", use_column_width=True)
    st.sidebar.title("🔬 PRP Dashboard")
    nav = st.sidebar.radio("Navigation", ["Home", "Dashboard (Results)"])

    if nav == "Home":
        st.title("🧠 PRP Diagnosis Assistant (AI-Powered)")
        st.markdown("Use this assistant to assess patient suitability for **PRP injection therapy**.")

        with st.form("prp_form"):
            col1, col2 = st.columns(2)
            with col1:
                age = st.slider("Patient Age", 18, 70, 30)
                platelets = st.number_input("Platelet Count (per μL)", value=250000, step=5000)
            with col2:
                injury = st.slider("MRI Injury Score", 0.0, 10.0, 5.0)
                inflammation = st.slider("Inflammation Level", 0.0, 5.0, 2.5)
            submitted = st.form_submit_button("🔍 Predict PRP Suitability")

            if submitted:
                features = np.array([[age, platelets, injury, inflammation]])
                prediction = model.predict(features)[0]
                index = calculate_platelet_index(platelets)
                risk = injury_risk_level(injury)
                decision = "Suitable" if prediction else "Not Suitable"

                st.markdown(f"### 🧾 Patient Summary")
                st.markdown(f"- **Platelet Index:** {index:.2f}")
                st.markdown(f"- **Injury Risk:** {risk}")

                if prediction:
                    st.success("✅ PRP is likely to be effective for this patient.")
                    st.balloons()
                else:
                    st.warning("❌ PRP may not be suitable. Consider alternatives.")

                # Save result
                store_result({
                    "datetime": datetime.now().isoformat(),
                    "age": age,
                    "platelets": platelets,
                    "injury": injury,
                    "inflammation": inflammation,
                    "index": index,
                    "risk": risk,
                    "prediction": decision
                })

    elif nav == "Dashboard (Results)":
        st.title("📊 Patient PRP Predictions Dashboard")
        data = load_all_results()
        if data:
            st.dataframe(data[::-1])  # show latest first
        else:
            st.info("No results stored yet.")
