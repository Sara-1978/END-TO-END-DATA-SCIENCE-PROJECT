# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: COTECH IT SOLUTIONS

*NAME*: R.S.PRIYADHARSHINI

*INTERN ID*: CTO4DR2648

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION 

Project: Iris Flower Classification Using Flask API

Task-3 of the CODTECH internship required building a complete end-to-end data science project. The main objective of this task was to collect a dataset, preprocess the data, build a machine learning model, and deploy the model using a web framework like Flask or FastAPI. This task helped me understand the complete lifecycle of a data science project—from beginning to end—similar to how projects are done in real companies.

#OUTPUT

<img width="1033" height="238" alt="Image" src="https://github.com/user-attachments/assets/e7c1926d-441f-4cdc-89b5-2768cc9dc2a5" />

1. Introduction

In this project, I developed a machine learning model that can classify iris flowers into three species: Setosa, Versicolor, and Virginica. I used the popular Iris dataset, which contains measurements of sepal length, sepal width, petal length, and petal width. Using these inputs, the model predicts the correct flower type.

The entire project follows all stages of a real end-to-end data science workflow, including data collection, preprocessing, model training, saving the model, and deploying it as an API.

2. Data Collection

For this task, I used the built-in Iris dataset from sklearn.datasets.
This dataset contains:

150 samples

4 features

3 output classes

The dataset is very clean and is commonly used for classification tasks. It is an excellent choice for demonstrating deployment.

3. Data Preprocessing

Before training the model, preprocessing is very important.
I applied the following steps:

Scaling the Features:
I used StandardScaler() to standardize the values so that all features have equal importance.

Train-Test Split:
The dataset was divided into training data (80%) and testing data (20%) to evaluate the model properly.

This preprocessing ensures that the model learns correctly and performs well on new unseen data.

4. Model Training

For training the model, I used the Logistic Regression algorithm from sklearn.
This algorithm is simple, fast, and works very well for classification problems.

Steps:

Fit the model using training data

Evaluate the model using test data

Model achieved high accuracy

Once the training was completed, I saved the model as model.pkl and the scaler as scaler.pkl using the pickle library. Saving these files allows us to use the model anytime without retraining.

5. Model Deployment Using Flask

The most important part of this task was deploying the model as a web API.

I used Flask, a lightweight Python web framework.

The Flask app includes:

Loading the saved model and scaler

Creating a /predict API endpoint

6. Conclusion

This task helped me understand the complete flow of a data science project from data collection to deployment. I learned how to preprocess data, train a model, save it, and deploy it using Flask. Building the API gave me hands-on experience in converting a machine learning model into a real-world usable application.

The final deliverable of this task is a working Flask API that predicts the iris flower species accurately.

Accepting JSON input from the user

Processing the input and returning the predicted flower name
