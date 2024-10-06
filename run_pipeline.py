# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))


from pipelines.training_pipeline import train_pipeline



if __name__=='__main__':
    train_pipeline(data_path=r"data\olist_customers_dataset.csv")