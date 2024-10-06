import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from zenml import pipeline
from steps.data_ingestion import ingest_data
from steps.clean_data import data_clean
from steps.evaluate import evaluate_model
from steps.model_train import train_model



@pipeline()          # ** imp enable_cache=False
def train_pipeline(data_path: str):
    df = ingest_data(data_path)
    X_train,X_test,y_train,y_test = data_clean(df)
    model = train_model(X_train,X_test,y_train,y_test)
    r2_score, rmse = evaluate_model(model, X_test, y_test)