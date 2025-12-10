# CODTECH Internship - Task 3
# End-to-End Data Science Project
# Example Project: Iris Flower Classification API using Flask

###############################################
# STEP 1: IMPORT LIBRARIES
###############################################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle
from flask import Flask, request, jsonify

###############################################
# STEP 2: DATA COLLECTION
###############################################
# Load dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

###############################################
# STEP 3: DATA PREPROCESSING
###############################################
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

###############################################
# STEP 4: TRAIN / TEST SPLIT
###############################################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

###############################################
# STEP 5: MODEL TRAINING
###############################################
model = LogisticRegression()
model.fit(X_train, y_train)

###############################################
# STEP 6: SAVE MODEL & SCALER
###############################################
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

###############################################
# STEP 7: BUILD FLASK API
###############################################
app = Flask(__name__)
loaded_model = pickle.load(open("model.pkl", "rb"))
loaded_scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    values = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    scaled = loaded_scaler.transform([values])
    prediction = loaded_model.predict(scaled)[0]

    return jsonify({"prediction": iris.target_names[prediction]})

###############################################
# STEP 8: RUN APP
###############################################
if __name__ == '__main__':
    app.run(debug=True)
