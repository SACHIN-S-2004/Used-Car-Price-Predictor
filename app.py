from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("carPrice_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":
        try:
            input_data = {
                "name": request.form["name"],
                "year": int(request.form["year"]),
                "km_driven": int(request.form["km_driven"]),
                "fuel": request.form["fuel"],
                "seller_type": request.form["seller_type"],
                "transmission": request.form["transmission"],
                "owner": request.form["owner"],
                "seats": int(request.form["seats"]),
                "Engine (CC)": int(request.form["engine_cc"]),
                "max_power (in bph)": float(request.form["max_power"]),
                "Mileage": float(request.form["mileage"])
            }

            input_df = pd.DataFrame([input_data])

            predicted_price = model.predict(input_df)[0]

            prediction = round(predicted_price, 2)

        except Exception as e:
            print("Prediction error:", e)
            prediction = "Error"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
