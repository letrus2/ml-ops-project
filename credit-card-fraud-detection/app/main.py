from pathlib import Path
import os
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline

# fast API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- load artifacts once ---

# absolute relative paths
BASE_DIR = Path(__file__).resolve().parent # only for .py files
MODELS_DIR = (BASE_DIR.parent / 'models').resolve()

model_path =        Path(os.environ.get("model_path", MODELS_DIR / "xgb_model.joblib"))
preprocessor_path = Path(os.environ.get("preprocessor_path", MODELS_DIR / "xgb_preprocessor.joblib"))
features_path =     Path(os.environ.get("features_path", MODELS_DIR / "features.json"))
features_all_path = Path(os.environ.get("features_all_path", MODELS_DIR / "features_all.json"))

threshold = float(0.5) # fraud / non-fraud

model = joblib.load(model_path)
preprocessor = joblib.load(preprocessor_path)
feature_names_to_model = json.load(open(features_path, 'r'))
feature_names_all = json.load(open(features_all_path, 'r'))

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', model)
])

# --- requests/responce schema with pydantic classes ---

# if needed in reserve
class Transaction_all(BaseModel):
    id: int
    Time: float
    feat1: float
    feat2: float
    feat3: float
    feat4: float
    feat5: float
    feat6: float
    feat7: float
    feat8: float
    feat9: float
    feat10: float
    feat11: float
    feat12: float
    feat13: float
    feat14: float
    feat15: float
    feat16: float
    feat17: float
    feat18: float
    feat19: float
    feat20: float
    feat21: float
    feat22: float
    feat23: float
    feat24: float
    feat25: float
    feat26: float
    feat27: float
    feat28: float
    Transaction_Amount: float
    IsFraud : bool

class Transaction(BaseModel):
    feat1: float
    feat2: float
    feat3: float
    feat4: float
    feat5: float
    feat6: float
    feat7: float
    feat8: float
    feat9: float
    feat10: float
    feat11: float
    feat12: float
    feat13: float
    feat14: float
    feat15: float
    feat16: float
    feat17: float
    feat18: float
    feat19: float
    feat20: float
    feat21: float
    feat22: float
    feat23: float
    feat24: float
    feat25: float
    feat26: float
    feat27: float
    feat28: float
    Transaction_Amount: float

class InferenceRequest(BaseModel):
    records: list[Transaction] = Field(..., min_items=1, description='Transactions to score')

class InferenceResponse(BaseModel):
    probabilities: list[float]
    labels: list[int]


# --- FastAPI app & routes ---
app = FastAPI(title='Creadit Card Fraud Detector', version = '0.1.0')

@app.get('/health')
def health_check() -> dict[str, str]:
    return {'status': 'ok'}

@app.post('/predict/', response_model=InferenceResponse)
def predict(request: InferenceRequest) -> InferenceResponse:
    try:
        df = pd.DataFrame([record.model_dump() for record in request.records])
        df = df[feature_names_to_model] # ensure exact column order
    except KeyError as exc:
        missing = set(feature_names_to_model) - set(df.columns)
        raise HTTPException(status_code=422, detail=f'MIssing features: {missing}') from exc
    
    proba = pipeline.predict_proba(df)[:,1]
    labels = (proba >= threshold).astype(int)

    return InferenceResponse(probabilities=proba.tolist(), labels=labels.tolist())