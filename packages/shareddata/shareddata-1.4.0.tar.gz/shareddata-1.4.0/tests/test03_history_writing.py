username = 'guest'
from SharedData.Logger import Logger
from SharedData.Metadata import Metadata
logger = Logger(__file__,user=username)

from SharedData.Metadata import Metadata
from SharedData.SharedData import SharedData
import numpy as np
import pandas as pd

shdata = SharedData('MarketData')
shdata.dataset
mktdata = shdata['MASTER']['D1']
df = mktdata['m2m']
df['ES_S01@XCME'].dropna()

_shdata = SharedData('MarketData',user=username)
_shdata.dataset = shdata.dataset
_shdata.dataset_metadata.static = shdata.dataset_metadata.static
_shdata.dataset_metadata.save()

md = Metadata('MASTER/FUT')
_md = Metadata('MASTER/FUT',user='guest')
_md.static=md.static
_md.save()

md = Metadata('MASTER/STOCK')
_md = Metadata('MASTER/STOCK',user='guest')
_md.static=md.static
_md.save()

_mktdata = _shdata['MASTER']['D1']
_mktdata['m2m'] = mktdata['m2m']
_df = _mktdata['m2m']
_df['ES_S01@XCME'].dropna()
_mktdata.tags['m2m'].Write()


Logger.log.info('Writing test for %s done!' % (username))