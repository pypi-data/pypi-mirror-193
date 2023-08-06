import pandas as pd
import time

from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedData import SharedData

shdata = SharedData('MarketData')
feeder = 'CSI'
period = 'D1'

# send shareddataframe
tag = pd.Timestamp('2022-03-04')
data = shdata[feeder][period]
df = data[tag]
data.tags[tag].Broadcast(
    idx=['01_202203@XKFE','01_202206@XKFE'],
    col=['open','high'])

# send timeseries
tag = 'close'
data = shdata[feeder][period]
df = data[tag]
idx = df.index[-2:].values
col=['01_S01@XKFE','01_S02@XKFE']
df.loc[idx,col]
data.tags[tag].Broadcast(idx = idx,col=col)