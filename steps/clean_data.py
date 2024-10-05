import logging
import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from zenml import step
from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessing

from typing_extensions import Annotated
from typing import Tuple

@step
def data_clean(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "x_train"],
    Annotated[pd.DataFrame, "x_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],] :
    """

    """
    try:
        process_strategy = DataPreProcessing()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        process_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, process_strategy)
        X_train, X_test, y_train,y_test = data_cleaning.handle_data()

        logging.info('Data cleaning completed')

    except Exception as e:
        raise e