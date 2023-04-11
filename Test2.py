import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('titanic.csv')
df = pd.DataFrame(data)

x = df["Survived"]
y = df["Age"]

x2 = df["Survived"]
y2 = df["Fare"]

plt.plot(x2,y2,color="blue")
plt.scatter(x,y,color="green")

plt.title("Titanic")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()