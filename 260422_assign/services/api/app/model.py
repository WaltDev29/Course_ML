import joblib
import numpy as np
import os

# 모델 로드
class Model:
    def __init__(self):
        MODEL_PATH = os.environ.get("MODEL_PATH", "model/svm_cancer_model.pkl")
        SCALER_PATH = os.environ.get("SCALER_PATH", "model/scaler.pkl")
        print(f"Loading model from {MODEL_PATH} ...")

        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)

model_wrapper = Model()
model = model_wrapper.model
scaler = model_wrapper.scaler