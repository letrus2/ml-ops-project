# Get started

## 1. Clone this repo
```bash
git clone https://github.com/letrus2/ml-ops-project-progress.git
```
Go to the project folder
```bash
cd ml-ops-project-progress
```

## 2. Set up the Environment
Make sure you have Python 3.12 installed. Set up the environment and install the packages.
```bash
py -3.12 -m venv venv
source venv/bin/activate # On Windows venv\Scripts\activate
pip install -r requirements.txt
```
## 3. Data Preparation
Train and production data are already present in the data folder.

## 4. Train the Model
'''bash
python main.py
'''
## 5. FastAPI
Run the FastAPI app by running:
```bash
cd credit-card-fraud-detection
uvicorn app.main:app --reload
```
## 6. Docker
To create contrainer run:
```bash
cd ..
docker build -t fastapi .
```
```bash
docker run -p 80:80 fastapi
```
Once your Docker image is built, you may push it to deployment on any cloud platform.

## 7. Monitor the Model
Monitor data drift and performance degradation via Evidently AI:
run \credit-card-fraud-detection\monitor.ipynb
