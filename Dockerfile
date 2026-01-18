# c:\Users\tinew\VScode\ml-ops\Dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY credit-card-fraud-detection/app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY credit-card-fraud-detection/app ./app
COPY credit-card-fraud-detection/models ./models

ENV model_path=models/xgb_model.joblib \
    preprocessor_path=models/xgb_preprocessor.joblib \
    features_path=models/features.json \
    features_all_path=models/features_all.json \
    PORT=8080 \
    threshold=0.5

EXPOSE 8080
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080"]
