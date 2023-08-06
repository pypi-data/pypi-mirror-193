import pandas as pd
import time

from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedData import SharedData

shdata = SharedData('MarketData')
wd = shdata['MASTER/watchdog']['D1']
today = pd.Timestamp(pd.Timestamp.now().date())
dfwatchdog = wd[today]
if dfwatchdog.empty:
    df = pd.DataFrame(
        0,
        index = [shdata.database],
        columns = ['watchdog']
    )
    wd[today] = df

