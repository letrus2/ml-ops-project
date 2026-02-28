# Get started

## 1. Clone this repo
```bash
git clone https://github.com/letrus2/ml-ops-project-progress.git
```
Go to the project folder
```bash
``cd ml-ops-project-progress
```

## 2. Set up the Environment
Make sure you have Python 3.9+ installed. Set up the environment and install the packages.
```bash
python -m venv venv
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
uvicorn app:app --re;pad
```
## 6. Docker
To create contrainer run:
```bash
docker build -t fastapi .
```
```bash
docker run -p 80:80 fastapi
```
Once your Docker image is built, you may push it to deployment on any cload platform.

## 7. Monitor the Model
Monitor data drift and performance degradation via Evidently AI:
```bash
run monitor.ipynb file
```
