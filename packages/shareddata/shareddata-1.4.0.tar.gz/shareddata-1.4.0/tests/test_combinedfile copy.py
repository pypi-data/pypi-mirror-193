import pandas as pd
import numpy as np
import gzip
import time

from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedData import SharedData

shdata = SharedData('MarketData')
feeder = shdata['MASTER']
mktdata = feeder['D1']
df = mktdata['m2m']
r, c = df.shape
idx = (df.index.astype(np.int64)/10**9)
idx_b = idx.values.tobytes()
cols = df.columns.values
colscsv = ','.join(cols)
colscsv_b = str.encode(colscsv,encoding='UTF-8',errors='ignore')
nbidx = len(idx_b)
nbcols = len(colscsv)

tini = time.time()
f=gzip.open('m2m.gz', 'wb',compresslevel=1)
#f=open('m2m.npy', 'wb')
f.write(np.float64(r))
f.write(np.float64(c))
f.write(str.encode(headercsv)+b'\n')
f.write(idx.values.tobytes())
np.save(f,df.values.astype(np.float64))
f.flush()
f.close()
print('total time %.2f' % (time.time()-tini))


tini = time.time()
f=gzip.open('m2m.gz', 'rb')
# f=open('m2m.npy', 'rb')
shape = np.frombuffer(f.read(16))
colscsv = f.readline()[:-1]
cols = str.split(colscsv.decode(),',')
idx = np.frombuffer(f.read(int(8*shape[0])))
index = pd.to_datetime(idx*10**9)
arr = np.load(f)
_df = pd.DataFrame(arr,index=index,columns=cols)
print('total time %.2f' % (time.time()-tini))

assert (_df.fillna(0)==df.fillna(0)).all().all()
