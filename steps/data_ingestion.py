import logging

import pandas as pd 
from zenml import steps


class IngestData:
    """
    Ingesting data from tha data_path

    """
    def __init__(self, data_path:str):
        """
            Instantiates the data path

            Args:
                data_path: path to the data
                
        """
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_data(data_path : str) -> pd.DataFrame:
    """
    Ingesting the data from the specified path

    Args:
        data_path: Path of the data

    Returns:
        pd.DataFrame: the ingested data

    """
    try:
        ingest_data= IngestData(data_path)
        df = ingest_data.get_data()
        return df

    except Exception as e:
        logging.error(f'Error while ingesting the data: {e}')
        raise e
    