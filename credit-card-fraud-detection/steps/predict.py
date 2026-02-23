import os
import joblib
from sklearn.metrics import RocCurveDisplay, PrecisionRecallDisplay
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, precision_recall_curve, roc_curve, auc

class Predictor:
    def __init__(self):
        self.model_path = self.load_config()['model']['store_path']
        self.pipeline = self.load_model()

    def load_config(self):
        import yaml
        with open('config.yml', 'r') as config_file:
            return yaml.safe_load(config_file)
        
    def load_model(self):
        model_file_path = os.path.join(self.model_path, 'model.pkl')
        return joblib.load(model_file_path)  
    
    def feature_target_separator(self, data):
        X = data.iloc[:,:-1]
        y = data.iloc[:,-1]
        return X, y
    
    def evaluate_model(self, X_test, y_test):
        y_pred = self.pipeline.predict(X_test)
        y_proba = self.pipeline.predict_proba(X_test)[:,1]
        accuracy = accuracy_score(y_test, y_pred)
        class_report = classification_report(y_test, y_pred, zero_division=0)
        roc_auc = roc_auc_score(y_test, y_proba)
        return accuracy, class_report, roc_auc