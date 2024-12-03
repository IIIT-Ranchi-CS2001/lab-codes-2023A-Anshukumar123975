import pandas as pd
import numpy as np
import matplotlib as plt
df=pd.read_csv("AQI_Data.csv")


# Q4(a)

ds = df[['City','AQI']].groupby("City").mean()
print(ds)

# Q4(b)
dp = df[['City','PM10']].groupby("City").max()
print(dp)

ds.to_csv("Citywise_AQI.csv")
dp.to_csv("Citywise_AQI.csv")