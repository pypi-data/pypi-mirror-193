username = 'master'
from SharedData.Logger import Logger
logger = Logger(__file__,user=username)

from SharedData.SharedData import SharedData
import numpy as np
import pandas as pd

shdata = SharedData('MarketData')
feeder = shdata['MASTER']
mktdata = feeder['D1']
df = mktdata['m2m']
df['ES_S0001@XCME'].dropna()

_shdata = SharedData('MarketData',user='ahmaabd')
_mktdata = _shdata['MASTER']['D1']
_df = _mktdata['m2m']
_df['ES_S01@XCME'].dropna()
Logger.log.info('Reading test for %s done!' % (username))