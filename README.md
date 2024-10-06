# End-to-End Customer Satisfaction Prediction: Pipeline Using ZenML and MLflow

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)  ![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)    ![ZenML](https://img.shields.io/badge/zenml-%234CAF50.svg?style=for-the-badge&logo=zenml&logoColor=white)     ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)  




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

In the deployment pipeline, ZenML's MLflow tracking integration is used for logging the hyperparameter values and the trained model itself and the model evaluation metrics -- as MLflow experiment tracking artifacts -- into the local MLflow backend. This pipeline also launches a local MLflow deployment server to serve the latest MLflow model if its accuracy is above a configured threshold.

The MLflow deployment server runs locally as a daemon process(this daemon isn't supported on Windows systems usage of WSL or docker environments is recommended) that will continue to run in the background after the example execution is complete. When a new pipeline is run which produces a model that passes the accuracy threshold validation, the pipeline automatically updates the currently running MLflow deployment server to serve the new model instead of the old one.

To round it off, we deploy a Streamlit application that consumes the latest model service asynchronously from the pipeline logic. This can be done easily with ZenML within the Streamlit code:

```python
service = prediction_service_loader(
   pipeline_name="continuous_deployment_pipeline",
   pipeline_step_name="mlflow_model_deployer_step",
   running=False,
)
...
service.predict(...)  # Predict on incoming data from the application
```

If you are running the `run_deployment.py` script, you will also need to install some integrations using ZenML:

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

## :notebook: Diving into the code

You can run two pipelines as follows:

- Training pipeline:

```bash
python run_pipeline.py
```

- The continuous deployment pipeline:

```bash
python run_deployment.py
```

## 🕹 Demo Streamlit App

There is a live demo of this project using Streamlit. It takes some input features for the product and predicts the customer satisfaction rate using the latest trained models. If you want to run this Streamlit app in your local system, you can run the following command:-

```bash
streamlit run streamlit_app.py
```






