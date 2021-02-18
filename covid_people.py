import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

pd.set_option("display.max_rows", 300)

df= pd.read_csv("covid_times.csv", encoding="Shift-jis")
df.loc[:,["time","Osaka"]]
df.loc[:,["time","Hokkaido"]]

Osaka_co = df.loc[:,["time","Osaka"]]
Hokkaido_co = df.loc[:,["time","Hokkaido"]]

fig = plt.figure( figsize=(20,10))
ax1 = fig.add_subplot(313)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(311)
ax1.bar(df["time"],df["Osaka"], color="blue")
ax1.set_title("大阪府のコロナ陽性者数の推移", fontsize = 20)
ax1.set_ylabel("陽性者数", size = 14, weight="light")
ax1.set_xlabel("日付", size = 14, weight = "light")
ax1.set_yticks([0,50,100,150,200,250])
ax1.set_xticks( [0, 29, 60, 90, 121, 151, 182, 213, 243, 274])
ax1.set_xticklabels(['2/1', '3/1', '4/1', '5/1', "6/1","7/1","8/1","9/1", "10/1", "11/1"], rotation=10, fontsize='10')
ax1.tick_params(direction = "inout", length = 10, colors = "black")

ax2.bar(df["time"],df["Hokkaido"], color="green")
ax2.set_title("北海道のコロナ陽性者数の推移", fontsize = 20)
ax2.set_ylabel("陽性者数", size = 14, weight="light")
ax2.set_yticks([0,50,100,150,200,250])
ax2.set_xticks( [0, 29, 60, 90, 121, 151, 182, 213, 243, 274])
ax2.set_xticklabels(['2/1', '3/1', '4/1', '5/1', "6/1","7/1","8/1","9/1", "10/1", "11/1"], rotation=10, fontsize='10')
ax2.tick_params(direction = "inout", length = 10, colors = "black")

ax3.bar(df["time"],df["All"], color="red")
ax3.set_title("国内のコロナ陽性者数の推移", fontsize = 20)
ax3.set_ylabel("陽性者数", size = 14, weight="light")
ax3.set_yticks([0,500,1000,1500,2000])
ax3.set_xticks( [0, 29, 60, 90, 121, 151, 182, 213, 243, 274])
ax3.set_xticklabels(['2/1', '3/1', '4/1', '5/1', "6/1","7/1","8/1","9/1", "10/1", "11/1"], rotation=10, fontsize='10')
ax3.tick_params(direction = "inout", length = 10, colors = "black")

plt.subplots_adjust(wspace=0.4, hspace=0.6)
plt.plot
