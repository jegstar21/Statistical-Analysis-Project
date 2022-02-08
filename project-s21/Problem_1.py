import pandas as pd
from matplotlib import pyplot as plt
import numpy
import statistics

df = pd.read_csv("NYC_Bicycle_Counts_2016_Corrected.csv")

brook = []
manhat = []
will = []
queen = []

# reads column and pushes into a list & converts data frame to numbers for all bridges
brooklyn = list(df["Brooklyn Bridge"])
for number in brooklyn:
    number = number.replace(",", "")
    brook.append(int(number))

manhattan = list(df["Manhattan Bridge"])
for number in manhattan:
    number = number.replace(",", "")
    manhat.append(int(number))

wills = list(df["Williamsburg Bridge"])
for number in wills:
    number = number.replace(",", "")
    will.append(int(number))

queens = list(df["Queensboro Bridge"])
for number in queens:
    number = number.replace(",", "")
    queen.append(int(number))

x_vars = [0] * 214
for i in range(len(x_vars)):
    x_vars[i] = i + 1

fig, axs = plt.subplots(2, 2)
fig.suptitle("Bike Data Across All Bridges")
axs[0, 0].plot(x_vars, brook, "tab:red", label="Brooklyn")
axs[0, 0].legend(loc="upper right")

axs[0, 1].plot(x_vars, manhat, "tab:orange", label="Manhattan")
axs[0, 1].legend(loc="upper right")

axs[1, 0].plot(x_vars, will, "tab:green", label="Williamsburg")
axs[1, 0].legend(loc="upper right")

axs[1, 1].plot(x_vars, queen, "tab:blue", label="Queensboro")
axs[1, 1].legend(loc="upper right")

for ax in axs.flat:
    ax.set(xlabel="Day Number", ylabel="Num of Bikes")

plt.show()