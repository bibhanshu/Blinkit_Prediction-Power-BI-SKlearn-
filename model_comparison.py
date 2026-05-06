##“Which model performs better?”
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
df = pd.read_excel(r"D:\blinkit\Blinkit Data\BlinkIT Grocery Data.xlsx")

# Target
y = df["Sales"]

# Features
x = df.drop(columns=["Sales", "Item Identifier"])

# Missing values
x["Item Weight"] = x["Item Weight"].fillna(0)

# Encode
x_encoded = pd.get_dummies(x, drop_first=True)

# Split
x_train, x_test, y_train, y_test = train_test_split(
    x_encoded, y, test_size=0.2, random_state=42
)

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)
lr_pred = lr_model.predict(x_test)

# Random Forest
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(x_train, y_train)
rf_pred = rf_model.predict(x_test)

# Results table
dataset = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R2 Score": [
        r2_score(y_test, lr_pred),
        r2_score(y_test, rf_pred)
    ],
    "RMSE": [
        np.sqrt(mean_squared_error(y_test, lr_pred)),
        np.sqrt(mean_squared_error(y_test, rf_pred))
    ]
})

##print(dataset)