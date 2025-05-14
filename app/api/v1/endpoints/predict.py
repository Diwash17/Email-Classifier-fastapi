from fastapi import APIRouter
from pydantic import BaseModel
import pickle
import os

router = APIRouter()

# Load your model and vectorizer from the /models directory
MODEL_PATH = os.getenv("MODEL_PATH", "models/spam_classifier_model1.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "models/count_vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

class EmailRequest(BaseModel):
    text: str

@router.post("/predict")
def predict_email(data: EmailRequest):
    transformed = vectorizer.transform([data.text])
    prediction = model.predict(transformed)
    return {"prediction": prediction[0]}