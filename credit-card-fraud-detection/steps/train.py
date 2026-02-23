import os
import joblib
import yaml
import pandas as pd

# Classifier
import xgboost as xgb

# Metrics
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import RocCurveDisplay, PrecisionRecallDisplay
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve, roc_curve, auc

# Pipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import RobustScaler

class Trainer:
    def __init__(self):
        self.config = self.load_config()
        self.seed = self.config['train']['random_state']
        self.model_path = self.config['model']['store_path']
        self.test_size = self.config['train']['test_size']
        self.pipeline = self.create_pipeline()

    def load_config(self):
        with open('config.yml', 'r') as config_file:
            return yaml.safe_load(config_file)

    def create_pipeline(self):
        preprocessor = ColumnTransformer([
            ('robust_scale', RobustScaler(), ['Transaction_Amount'])
        ], remainder = 'passthrough')

        model = xgb.XGBClassifier(tree_method='hist',
                                # predictor='gpu_predictor',
                                # gpu_id=0,
                                # device='cuda',
                                n_jobs=1,
                                subsample= 0.5, n_estimators = 400, min_child_weight = 5, max_depth = 3, learning_rate = 0.01, gamma = 0.2, colsample_bytree = 0.7,
                                random_state=self.seed)
        
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('model', model)
        ])

        return pipeline
    
    def sample_preparator(self, data):
        X = data.iloc[:, :-1]
        y = data.iloc[:,-1]
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=self.test_size, stratify=y, random_state=self.seed)
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def save_model(self):
        model_file_path = os.path.join(self.model_path, 'model.pkl')
        joblib.dump(self.pipeline, model_file_path)
    
