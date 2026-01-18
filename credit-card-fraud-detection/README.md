# Credit Card Fraud Detection — Random Forest & XGBoost

**Goal**: To build the best fraud detection model achieving the highest Private Score on the Kaggle competition leaderboard.  
**Data**: Open data set from the Kaggle competition with a highly imbalanced target class.  
**Results**: Random Forest (0.701 Private Score Leaderboard, 27/71 Rank on LeaderBoard) and XGB (0.708 Private Score Leaderboard, 24/71 Rank on LeaderBoard)  
**Date**: 2025-09-28  

## How to run
1. **Set up environment** for your project.
```bash    
    git clone https://github.com/letrus2/ml-ops.git
    cd ml-ops
    python -m venv venv
    source venv\Scripts\activate # On Linux:  venv/bin/activate 
    pip install -r credit-card-fraud-detection\app\requirements.txt
``` 
2. **Download data**: from [Kaggle Competition](https://www.kaggle.com/competitions/credit-card-fraud-prediction/data) and place it in './data/' folder of your project/environment. (Note: If you have cloned the Git repo, you can skip this step.)
3. **Open notebooks** and run sequentially:
    01_data_exploring.ipynb
    02_random_forest_undersample.ipynb
    03_xgb_full.ipynb

## Data & license
Dataset: [Kaggle Credit Card Prediction](https://www.kaggle.com/competitions/credit-card-fraud-prediction/overview) by Prayash Dash and VectorNd (2024).
License: Use governed the competition rules (non-commercial / educational).
This repo is for **educational and portfolio purposes only**.

## Reproducibility
Notebooks are already set up to reproduce the same results with fixed SEEDs (random_state=42), fixed stratified split, and undersampling.

## Method
1. Data validation: verified that there are no nulls and all features are on comparable scales.
2. Models:
    1. Random Forest (RF) — undersample 50%/50%
    2. XGBoost (XGB) — full data set
Both models used all the features.
3. Preprocessing:
    Undersampling was made in raw code.
    Scaling and modeling combined in a pipeline.
4. Reproducibility:
    Fixed SEED=42 across samplers, splitters, and models.
    Stratified train/test split.

## Results
### Random Forest
| Metric               | Value     | Notes                            |
| -------------------- | --------- | -------------------------------- |
| ROC-AUC              | 0.745     | 50/50 balanced dataset           |
| PR-AUC               | 0.751     | Evaluated on balanced validation |
| Kaggle Private Score | **0.701** | Rank 27/71, 2025-09-28           |

### XGBoost
| Metric               | Value     | Notes                            |
| -------------------- | --------- | -------------------------------- |
| ROC-AUC              | 0.816     | Full data, realistic imbalance   |
| PR-AUC               | 0.031     | Fraud rate ≈ 0.00179 → Lift ≈ ×17|
| Kaggle Private Score | **0.708** | Rank 24/71, 2025-09-28           |


## Repo map
```
├─ data/                  # train.csv, test.csv, sample_submission.csv
├─ notebooks/
│  ├─ 01_data_exploring.ipynb             # Exploring: null values, target class balance, feature scaling.
│  ├─ 02_random_forest_undersample.ipynb  # 50/50 undersample → RF → submission
│  └─ 03_xgb_full.ipynb                   # full data (no undersampling) → XGB → submission
└─ README.md  ← you are here
```
## Model Card (summary)
+ Task: Binary fraud classification.
+ Training: Random Forest (undersampled) and XGBoost (full data)
+ Evaluation metrics: ROC-AUC, PR-AUC, f1
+ Limitations: Trained on anonymized competition data; not production-ready; no real-world interpretability guarantees.

## Next steps

**Goal:** Build a public demo API and a full MLops pipeline using:
- Docker
- FastAPI
- Kafka     

**Planned improvements:**
1. Retrain on an open CC0 or ULB dataset for public MLOps deployment.
2. Add MLflow tracking and logging
3. Package the pipeline into a Dockerized FastApi endpoint.
4. Implement automatic threshold tuning (Precision@Recall or cost-based).
5. Add SHAP feature-importance analysis.
