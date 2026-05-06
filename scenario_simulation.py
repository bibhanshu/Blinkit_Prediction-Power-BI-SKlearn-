##“What happens if product conditions change?”
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

# Scenario products
scenarios = pd.DataFrame([
    {
        "Item Fat Content": "Regular",
        "Item Type": "Snack Foods",
        "Outlet Establishment Year": 2015,
        "Outlet Identifier": "OUT017",
        "Outlet Location Type": "Tier 2",
        "Outlet Size": "Medium",
        "Outlet Type": "Supermarket Type3",
        "Item Visibility": 0.35,
        "Item Weight": 12,
        "Rating": 4.5
    },
    {
        "Item Fat Content": "Regular",
        "Item Type": "Snack Foods",
        "Outlet Establishment Year": 2015,
        "Outlet Identifier": "OUT017",
        "Outlet Location Type": "Tier 2",
        "Outlet Size": "Medium",
        "Outlet Type": "Supermarket Type3",
        "Item Visibility": 0.10,
        "Item Weight": 12,
        "Rating": 4.5
    }
])

# Drop identifier
scenarios = scenarios.drop(columns=["Outlet Identifier"])

# Encode
scenarios_encoded = pd.get_dummies(scenarios, drop_first=True)

# Match training columns
scenarios_encoded = scenarios_encoded.reindex(
    columns=x_encoded.columns,
    fill_value=0
)

# Predict
scenarios["Predicted Sales"] = model.predict(scenarios_encoded)

# Final output
dataset = pd.DataFrame({
    "Scenario": ["High Visibility", "Low Visibility"],
    "Predicted Sales": scenarios["Predicted Sales"]
})

##print(dataset)