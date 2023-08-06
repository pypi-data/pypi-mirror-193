import numpy as np
import pandas as pd
import time

username = 'master'
from SharedData.Logger import Logger
logger = Logger(__file__,user=username)

from SharedData.SharedData import SharedData


if __name__ ==  '__main__':
    
    shdata = SharedData('MarketData')
    feeder = shdata['BVMF/FUT']
    
    tini = time.time()
    feeder.load()
    print('total time %f' % (time.time()-tini))


    # tini = time.time()
    # for tag in feeder.dataset['tag']:
    #     feeder['D1'][tag]
    # print('total time %f' % (time.time()-tini))

    # tini = time.time()
    # feeder = shdata['TEST']
    # feeder.default_collections='MASTER/FUT,MASTER/STOCK'
    # feeder.load_dataset(tags=['test1','test2'])
    # print('total time %f' % (time.time()-tini))


    mktdata=feeder['D1']
    mktdata.tags
    mktdata['ret'].loc[:mktdata['ret'].last_valid_index()]
    mktdata['m2m'].loc[:mktdata['m2m'].last_valid_index()]
    
    Logger.log.info('Reading test for %s done!' % (username))