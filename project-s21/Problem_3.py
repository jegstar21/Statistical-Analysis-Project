import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

temp = {}
df = pd.read_csv("NYC_Bicycle_Counts_2016_Corrected.csv")

total = []
prep = []

totalRiders = list(df["Total"])
for num in totalRiders:
    number = number.replace(",", "")
    number = number.replace(" ", "")
    total.append(int(number))

precipitation = list(df["Precipitation"])
for number in precipitation:
    number = number.replace("T", "0")
    number = number.replace("(S)", "")
    prep.append(float(number))

temp["Total"] = total
temp["Precipitation"] = prep

data = DataFrame(temp, columns=["Precipitation", "Total"])

plt.scatter(data["Total"], data["Precipitation"], color="blue")
plt.title("Precipitation vs Total Riders", fontsize=14)
plt.xlabel("Total Riders", fontsize=14)
plt.ylabel("Precipitation", fontsize=14)
plt.grid(True)
plt.show()

X1 = np.array(prep).reshape(-1, 1)
Y1 = np.array(total)

regr = linear_model.LinearRegression()
regr.fit(X1, Y1)

print("Intercept: \n", regr.intercept_)
print("Coefficients: \n", regr.coef_)

X2 = sm.add_constant(X1)
model = sm.OLS(Y1, X2).fit()
print(model.summary())
