import logging
import pandas as pd

from zenml import step

@step
def train_model(df: pd.DataFrame) -> None:
    """
    Trains the model on given data

    Args:
        df: the ingested data
        
    """

    pass
