import pandas as pd
import numpy as np
from multiprocessing import shared_memory
import time
from numba import njit,prange

from SharedData.Logger import Logger
logger = Logger(__file__,user='master')
from SharedData.Metadata import Metadata


md = Metadata('MASTER/FUT_HEAD')
md.mergeUpdate(Metadata('MASTER/FUT_TAIL').static)

df = md.static.reset_index()
dtypes = df.dtypes.reset_index()
dtypes.columns = ['tag','dtype']

tags_obj =  dtypes['tag'][dtypes['dtype']=='object'].values
tag = tags_obj[0]
for tag in tags_obj:
    df[tag] = df[tag].astype('|S')

dtypes = df.dtypes.reset_index()
dtypes.columns = ['tag','dtype']
# dtypes['dtype'] = dtypes['dtype'].astype(str)
# dtypes = dtypes.sort_values(['dtype','tag'])
# df = df[dtypes['tag']].copy()

_df = df.to_records(index=False)
_df[-1]




shm = shared_memory.SharedMemory(name = 'test',create=True, size=_df.size * _df.itemsize)
shmarr = np.ndarray(_df.shape,dtype=_df.dtype, buffer=shm.buf)
shmarr[:] = _df[:]

# save dtype to a string
arr = _df.__array_interface__['descr']
arr[0][1]
_dtype = np.dtype(_df.__array_interface__['descr'])

_shm = shared_memory.SharedMemory(name = 'test',create=False)
_shmarr = np.ndarray(_df.shape,dtype=_df.dtype, buffer=_shm.buf)
_shmarr[0]['m2m']=0
shmarr[0]['m2m']


tini = time.time()
for i in range(shmarr.shape[0]):
    if shmarr[i]['serie']=='DOL_S0001@BVMF':
        pass
print(time.time()-tini)

__df = pd.DataFrame(_shmarr, copy=False)

__df._data
__df.loc[0,'m2m']=2
df.dtypes

@njit(parallel=True)
def test(shmarr):    
    for i in prange(shmarr.shape[0]):
        if shmarr[i]['serie']=='DOL_S0001@BVMF':
            shmarr[i]['m2m_notional']=shmarr[i]['m2m']*shmarr[i]['multiplier']

@njit(parallel=True)
def testloop(shmarr):
    for j in range(1000000):
        test(shmarr)

tini = time.time()
testloop(shmarr)
print(time.time()-tini)


