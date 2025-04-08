import pickle
import pandas as pd
import numpy as np
from flask import Flask,request,jsonify,render_template
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

with open('models/ridge_reg.pkl','rb') as file:
    ridge_model=pickle.load(file)

with open('models/scaler.pkl','rb') as file:
    standard_scaler=pickle.load(file)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict_data',methods=['GET','POST'])
def predict_data():
    if request.method=="POST":
        try:
            # Extract data from the form
            temp = float(request.form['temp'])
            rh = float(request.form['rh'])
            ws = float(request.form['ws'])
            rain = float(request.form['rain'])
            ffmc = float(request.form['ffmc'])
            dmc = float(request.form['dmc'])
            isi = float(request.form['isi'])
            classes = int(request.form['classes'])
            region = int(request.form['region'])

            input_data = np.array([[temp, rh, ws, rain, ffmc, dmc, isi, classes, region]])
 
            # Scale input data (if required)
            input_scaled = standard_scaler.transform(input_data)

            # Predict using Ridge Regression model
            prediction = ridge_model.predict(input_scaled)[0]

            # Render home.html with the prediction result
            return render_template('home.html', prediction=prediction)
        
        except Exception as e:
            return f"Error occurred: {str(e)}"

    else:
        return render_template('home.html')  


if __name__=="__main__":
    app.run()