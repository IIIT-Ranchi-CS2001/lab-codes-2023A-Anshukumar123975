import pandas as pd
import numpy as np
import matplotlib as plt
df=pd.read_csv("AQI_Data.csv")

# 1(a)
print(df.head(5))

# 1(b)
print(df.tail(6))

# 1(c)
print(df.describe())

# 1(d)
print(df[['City','AQI','PM2.5','PM10']].groupby("City").mean())