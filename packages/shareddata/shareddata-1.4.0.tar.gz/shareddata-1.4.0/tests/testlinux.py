# import sys
# sys.path.append('/home/jcooloj/src/SharedData/src')
# print(sys.path[0])

import os

from SharedData.Logger import Logger
logger = Logger(__file__,user='master')
from SharedData.Metadata import Metadata
from SharedData.SharedData import SharedData

Logger.log.info('Running on %s!' % (os.name))

# md = Metadata('MASTER/FUT_HEAD')
# md.mergeUpdate(Metadata('MASTER/FUT_TAIL').static)
# md.static

# md = Metadata('VOTER/FUT_HEAD')
# md.mergeUpdate(Metadata('VOTER/FUT_TAIL').static)
# md.static

# md = Metadata('CSI/FUT_HEAD')
# md.mergeUpdate(Metadata('CSI/FUT_TAIL').static)
# md.static

shdata = SharedData('MarketData')
master = shdata['MASTER']['D1']
master['m2m'].dropna(how='all')

import pandas as pd
shdata = SharedData('MarketData')
bvbg = shdata['BVMF/BVBG086']['D1']
df = bvbg[pd.Timestamp('2023-02-16')]
df = df.sort_values('tradqty',ascending=False)

bvbg = shdata['BVMF/BVBG086']['D1']

cme_fut = Metadata('CME/FUT_HEAD')
cme_fut.mergeUpdate(Metadata('CME/FUT_TAIL').static)

fut = Metadata('VOTER/FUT_HEAD')
fut.mergeUpdate(Metadata('VOTER/FUT_TAIL').static)
fut.static.loc['2023-02-14','ES_202303@XCME']

cme_fut.static.loc['2023-02-13','ES_202303@XCME']
cme_fut.static.loc['2023-02-16','MES_202303@XCME']