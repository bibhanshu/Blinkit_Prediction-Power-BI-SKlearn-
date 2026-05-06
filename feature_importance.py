##“What truly drives BlinkIT sales?”
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

# Encode categorical variables
x_encoded = pd.get_dummies(x, drop_first=True)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x_encoded, y, test_size=0.2, random_state=42
)

# Random Forest model
model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

# Feature Importance
importance = model.feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": x_encoded.columns,
    "Importance": importance
})

# Sort highest first
feature_importance_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=False
)

# Top 10 only
dataset = feature_importance_df.head(10)

##print(dataset)