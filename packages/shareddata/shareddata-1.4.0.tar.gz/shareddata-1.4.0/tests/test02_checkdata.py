import numpy as np
import pandas as pd
import time

username = 'master'
from SharedData.Logger import Logger
logger = Logger(__file__,user=username)

from SharedData.SharedData import SharedData


if __name__ ==  '__main__':
    
    shdata = SharedData('MarketData')
    feeder = shdata['MASTER']
    
    tini = time.time()
    feeder.load()
    
    print('total time %f' % (time.time()-tini))
    
    feeder.dataset_scan()

    stats_tags = ['create_map','init_time',\
        'last_valid_index','last_update','first_update',\
        'data_size','memory_size',\
        'download_time','download_speed',\
        'index_count','columns_count',\
        'notnull_sum','notnull_index','notnull_columns',\
        'density_ratio','density_ratio_index','density_ratio_columns']
    ds = feeder.dataset_metadata.static.set_index('tag')
    idx = ds['density_ratio']>0.0
    ds.loc[idx,stats_tags]
    
    # tini = time.time()
    # feeder.load()
    # print('total time %f' % (time.time()-tini))

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