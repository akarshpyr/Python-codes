from flask import Flask,render_template,request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

mul_reg = open("Profit_predictor.pkl", "rb")
ml_model = joblib.load(mul_reg)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            Administration = float(request.form['Administration'])
            MRRD = float(request.form['MRRD'])
            pred_args = [Administration, MRRD]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
            return "Please check for the incorrect values"
    return render_template('predict.html', prediction = model_prediction)


if __name__ == "__main__":
    app.run(debug=True)
