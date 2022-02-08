import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

df = pd.read_csv("NYC_Bicycle_Counts_2016_Corrected.csv")

high = []
low = []
prep = []
total = []
temp = {}

highTemp = list(df["High Temp (°F)"])
for number in highTemp:
    high.append(int(number))

lowTemp = list(df["Low Temp (°F)"])
for number in lowTemp:
    low.append(int(number))

precipitation = list(df["Precipitation"])
for number in precipitation:
    number = number.replace("T", "0")
    number = number.replace("(S)", "")
    prep.append(int(float(number)))

totalRiders = list(df["Total"])
for number in totalRiders:
    number = number.replace(",", "")
    number = number.replace(" ", "")
    total.append(int(number))

temp["High Temp"] = high
temp["Low Temp"] = low
temp["Total"] = total

data = pd.DataFrame(temp, columns=["High Temp", "Low Temp", "Total"])

plt.scatter(data["High Temp"], data["Total"], color="red")
plt.title("Total Riders vs High Temp", fontsize=14)
plt.xlabel("High Temp", fontsize=14)
plt.ylabel("Total Riders", fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(data["Low Temp"], data["Total"], color="green")
plt.title("Total Riders vs Low Temp", fontsize=14)
plt.xlabel("Low Temp", fontsize=14)
plt.ylabel("Total Riders", fontsize=14)
plt.grid(True)
plt.show()

X1 = data[["High Temp", "Low Temp"]]
Y1 = data["Total"]

regr = linear_model.LinearRegression()
regr.fit(X1, Y1)

print("Intercept: \n", regr.intercept_)
print("Coefficients: \n", regr.coef_)

X2 = sm.add_constant(X1)
model = sm.OLS(Y1, X2).fit()
print(model.summary())