import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression
from tools import calculate_platelet_index, injury_risk_level, store_result, load_all_results
from ui import render_ui

# ----- Simulated ML model -----
def train_dummy_model():
    np.random.seed(42)
    X = np.random.rand(100, 4) * [60, 500000, 10, 5]
    y = (X[:, 1] > 200000) & (X[:, 2] > 4)
    model = LogisticRegression()
    model.fit(X, y.astype(int))
    return model

model = train_dummy_model()
