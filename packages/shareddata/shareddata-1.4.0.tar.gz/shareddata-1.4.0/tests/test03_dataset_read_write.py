import numpy as np
import pandas as pd
import time

username = 'master'
from SharedData.Logger import Logger
logger = Logger(__file__,user=username)

from SharedData.Metadata import Metadata
from SharedData.SharedData import SharedData


if __name__ ==  '__main__':
    
    # md = Metadata('CSI/FUT_SERIES')
    # md.static

    # md = Metadata('CSI/FUT_SERIES_SYMBOLS')
    # md.static


    # shdata = SharedData('MarketData')
    # feeder = shdata['VOTER/FUT']

    # tini = time.time()
    # feeder.load()
    # print('total time %f' % (time.time()-tini))

    # tini = time.time()
    # feeder['D1']['m2m']
    # print('total time %f' % (time.time()-tini))

    # tini = time.time()
    # feeder['D1'].tags['m2m'].Write()
    # print('total time %f' % (time.time()-tini))
    
    # md = Metadata('BVMF/BDATUAL/FUT_CHAIN')
    # md.save()

    # feeder['D1'].tags
    # feeder['D1']['m2m'].loc[:feeder['D1']['m2m'].last_valid_index()]

    # tini = time.time()
    # feeder.save(startDate=pd.Timestamp('2000-01-01'))
    # print('total time %f' % (time.time()-tini))

    Logger.log.info('Reading test for %s done!' % (username))