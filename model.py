from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import pandas as pd

carPrice = pd.read_csv("processes2.csv")
carPrice=carPrice.drop(columns=["*"])
carPrice=carPrice.drop(columns=["Mileage Unit"])
X = carPrice.drop("selling_price", axis=1)
y = carPrice["selling_price"]

categorical_cols = [
    "name", "fuel", "seller_type",
    "transmission", "owner"
]

numerical_cols = [
    "year", "km_driven", "seats",
    "max_power (in bph)", "Mileage", "Engine (CC)"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

gb_model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("regressor", GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.1,
            random_state=42
        ))
    ]
)

gb_model.fit(X, y)

with open("carPrice_model.pkl", "wb") as f:
    pickle.dump(gb_model, f)

print("Model trained and saved!")
