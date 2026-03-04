# Getting started

## 1. Clone this repo
```bash
git clone https://github.com/letrus2/ml-ops-project-progress.git
cd ml-ops-project-progress
```
## 2. Set up the environment
Make sure you have Python 3.12 installed. Set up the environment and install the packages.
```bash
py -3.12 -m venv venv
source venv/bin/activate # On Windows venv\Scripts\activate
pip install -r requirements.txt
```
## 3. Data preparation
Train and production data are already present in the data folder.

## 4. Train the Model
```bash
python main.py
```
## 5. Run the FastAPI app
Run the FastAPI app by running:
```bash
cd credit-card-fraud-detection
uvicorn app.main:app --reload
```
## 6. Create Docker image
To create container run:
```bash
cd ..
docker build -t fastapi .
```
```bash
docker run -p 80:80 fastapi
```
Once the image is built, you may push it and deploy to any cloud platform.

## 7. Monitor the Model
Monitor data drift and performance degradation with Evidently AI using:
``\credit-card-fraud-detection\monitor.ipynb``
