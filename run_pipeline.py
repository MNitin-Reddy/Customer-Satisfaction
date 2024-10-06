# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))


from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__=='__main__':
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path=r"data\olist_customers_dataset.csv")

