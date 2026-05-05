## - SALES PREDICTION (REGRESSION)
## - Given details of an item + store, what will its Sales be?
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor

df = pd.read_excel(r"D:\blinkit\Blinkit Data\BlinkIT Grocery Data.xlsx")

##print("Shape:", df.shape)
##print("\nColumns:\n", df.columns)
##print("\nMissing values:\n", df.isnull().sum())
y = df["Sales"]
##print(y.head()) ## Sales our Y value Sales
x = df.drop(columns=["Sales", "Item Identifier"]) #here we added all column to X except !
##print(x.columns) ## all without Sales and Item Identifier
x["Item Weight"] = x["Item Weight"].fillna(0) ## replace null with zero we can also remove the same
##print(x.isnull().sum()) ##confirming no missing values

## Convert categorical columns to numbers##
x_encoded = pd.get_dummies(x,drop_first=True)
##print(x_encoded.shape)
##print(x_encoded.columns)
x_encoded_train,x_encoded_test,y_train,y_test = train_test_split(x_encoded,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(x_encoded_train, y_train)
pred = model.predict(x_encoded_test)
##print(pred)
print("Actual:", y_test[:10].values)
print("Predicted:", pred[:10])
r2 = r2_score(y_test, pred) ## y test its the actual result , Pred is what i predicted .
print("R2 Score:", r2) ## - R2 Score: 0.014365362630749834
##R² ≈ 0 → model ≈ average guess.
MSE = mean_squared_error(y_test, pred)
RMSE = np.sqrt(MSE)
print("MSE:", MSE,"RMSE:", RMSE)
##MSE: 3904.498194894506 RMSE: 62.48598398756721- “On average, my prediction is off by ₹62.”
##Compare RMSE to average target value ,Suppose average Sales ≈ ₹140
##RMSE = 62
##62 / 140 ≈ 44%
## Your average prediction error is ~44% of average sales. That’s poor.
##So what is “good”?  ----  Not “close to zero” necessarily — but small relative to Sales.
## - Linear Regression fail - Linear Regression is too simple for the kind of patterns hidden in your BlinkIT data.
##so we willl use random forest which will decrease the RMSE from - 62 to 44
## We will Try random Forest we already have xtrain and test we dont need to write it extra
model_Random_forest = RandomForestRegressor(random_state=42) ##“Create a Random Forest regression model object.” we are
# not training here we are just saying we want to use random forest - we can also use n_estimators=500 to increase the tree
model_Random_forest.fit(x_encoded_train, y_train) ## this is real Learning Stage
pred = model_Random_forest.predict(x_encoded_test)
model_Random_forest.fit(x_encoded_train, y_train)
pred = model_Random_forest.predict(x_encoded_test)
r2_Random_forest = r2_score(y_test, pred)
print("R2 Score(Random Forest):", r2_Random_forest)
MSE_Random_Forest = mean_squared_error(y_test, pred)
RMSE_Random_forest = np.sqrt(MSE_Random_Forest)
print("MSE(Random Forest):", MSE_Random_Forest,"RMSE(Random Forest):", RMSE_Random_forest)

##Your model currently predicts Sales for any given product + outlet setup.













##Feature Importance ##What truly drives Sales?
importance = model_Random_forest.feature_importances_
feature_names = x_encoded.columns
feature_importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})
feature_importance_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=False
)
print(feature_importance_df.head(10))










