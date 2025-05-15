from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import pickle
import os

router = APIRouter()

# Load model and vectorizer
MODEL_PATH = os.getenv("MODEL_PATH", "models/spam_classifier_model1.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "models/count_vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

# Request models
class EmailRequest(BaseModel):
    text: str

class EmailsRequest(BaseModel):
    texts: List[str]

# Single prediction endpoint
@router.post("/predict", tags=["Prediction"])
def predict(input: EmailRequest):
    features = vectorizer.transform([input.text])
    prediction = model.predict(features)[0]
    label = "spam" if prediction == 1 else "ham"
    return {
        "prediction": int(prediction),
        "label": label
    }


# Batch prediction endpoint
@router.post("/predictions", tags=["Prediction"])
def predictions(inputs: EmailsRequest):
    features = vectorizer.transform(inputs.texts)
    preds = model.predict(features)
    results = []

    for text, pred in zip(inputs.texts, preds):
        label = "spam" if pred == 1 else "ham"
        results.append({
            "text": text,
            "prediction": int(pred),
            "label": label
        })

    return {"results": results}