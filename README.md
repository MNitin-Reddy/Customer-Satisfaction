# End-to-End Customer Satisfaction Prediction: Pipeline Using ZenML and MLflow

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zenml)](https://pypi.org/project/zenml/)

**Problem statement**: For a given customer's historical data, we are tasked to predict the review score for the next order or purchase. We will be using the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). This dataset has information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow viewing charges from various dimensions: from order status, price, payment, freight performance to customer location, product attributes and finally, reviews written by customers. The objective here is to predict the customer satisfaction score for a given order based on features like order status, price, payment, etc. In order to achieve this in a real-world scenario, we will be using [ZenML](https://zenml.io/) to build a production-ready pipeline to predict the customer satisfaction score for the next order or purchase.


## Expected Outcomes
This project aims to demonstrate the following outcomes:

- **Customer Satisfaction Prediction**: Accurately forecast the satisfaction score for a customer's next order based on historical data, enabling businesses to tailor their services and improve customer experience.

- **End-to-End Pipeline**: Implement a complete machine learning pipeline using [ZenML](https://zenml.io/) that includes data ingestion, cleaning, model training, evaluation, and deployment.

- **Integration with MLflow**: Utilize [MLflow](https://mlflow.org/) for model tracking and management, allowing for easy monitoring of experiments and comparisons between different models and configurations.

- **Deployment Readiness**: Show how to deploy machine learning models in a production environment, ensuring they are readily available for real-time predictions.

- **Scalability**: Provide insights into how the pipeline can be scaled and adapted for various datasets and business needs, fostering a data-driven decision-making culture.


This project is a practical example for anyone interested in utilizing modern tools and frameworks to tackle real-world data science and machine learning challenges.

we are building an end-to-end pipeline to predict customer satisfaction scores for new orders using the Brazilian E-Commerce Public Dataset by Olist. Instead of training the model once, we implement continuous training, deployment, and tracking using ZenML and MLflow, and showcase the results via a Streamlit app.

The pipeline is designed to:

Scale to cloud deployments.
Track parameters, data inputs, and results.
Continuously deploy models based on evaluation criteria.

## Key Components:

### Training Pipeline
The training pipeline involves:

* __Ingesting data:__ Reads raw data into a DataFrame.
* **Data cleaning:** Prepares and cleans the data.
* **Model training:** Trains a machine learning model and logs metrics using MLflow.
* **Model evaluation:** Assesses the model's performance and stores the results.

### Deployment Pipeline
The deployment pipeline builds on the training pipeline by:

* **Deployment trigger:** Checks if the new model meets deployment criteria (e.g., RMSE threshold, R2_score).
* **Model deployment:** Deploys the model via MLflow if it meets the criteria.

Make sure you meet the requirements
```bash
pip install "zenml[server]"
pip install -r requirements.txt
zenml integration install mlflow -y
```

The project can only be executed with a ZenML stack that has an MLflow experiment tracker and model deployer as a component. Configuring a new stack with the two components are as follows:

```bash
zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow --flavor=mlflow
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
```






