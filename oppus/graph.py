
#%%
## generate data
from datetime import timedelta,datetime
from os import replace
from random import randrange

today = datetime.today() # or datetime.now to use local timezone
today = datetime(year=today.year, month=today.month, day=today.day, hour=0, second=0)
start = today - timedelta(days=7)

rang = randrange(10000)
timestamp = [start + timedelta(seconds=randrange(7*86400)) for i in range(rang)]
packet_size = [randrange(4096) for i in range(rang)]


# analyse data
import pandas as pd
df = pd.DataFrame({"timestamp":timestamp,"packet_size":packet_size}).sample(frac=1)


df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# df.rename(columns={"packet_size":"sagedus"}).resample("5T").count().plot.bar()#("packet_size")
freq = df.sample(n=500,replace=True).resample("30T").count()
# freq["kuupaev"] = freq.index.strftime("%Y-%m-%d")
# freq.reset_index(drop=True, inplace=False)
ax = freq.plot.bar()#("packet_size")

for i, t in enumerate(ax.get_xticklabels()):
    if (i % 48) != 0:
        t.set_visible(False)
#%%
# TODO:
freq = df.sample(n=500,replace=True).resample("30T").count()
# freq.reset_index(drop=False, inplace=True)
ax2 = freq.plot.bar()#("packet_size")

for i, t in enumerate(ax2.get_xticklabels()):
    if (i % 48) != 0:
        t.set_visible(False)
# %%
