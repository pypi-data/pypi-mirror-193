import pandas as pd
import numpy as np
import io, gzip, hashlib, pickle
import time

from SharedData.Logger import Logger
logger = Logger(__file__,user='master')
from SharedData.SharedData import SharedData
from SharedData.Metadata import Metadata

md = Metadata('SCHEDULES/MASTER_TRADEBOT05')
md.save(True)

md = Metadata('BBG/FIRST_SERIES')
md.static
md.save(True)

keys = Metadata.list('BBG/FUT_CHAIN')
for key in keys:    
    print('saving '+key)
    md = Metadata(key)
    md.save(True)
print('DONE!')
        
# # load data
# shdata = SharedData('MarketData')
# feeder = shdata['BVMF/BVBG086']
# dt = pd.Timestamp('2023-01-11')
# df = feeder['D1'][dt]
# feeder['D1'].tags[dt].Write()

# _df = df.dropna(how='all',axis=0).dropna(how='all',axis=1)
# _df.index.names=['date']
# idx_cols_b = str.encode(','.join(_df.index.names),encoding='UTF-8',errors='ignore')
# _df = _df.reset_index()
# cols_b = str.encode(','.join(_df.columns),encoding='UTF-8',errors='ignore')
# header = np.array([len(idx_cols_b),len(cols_b)]).astype(np.int64)
# # allocate memory
# io_obj = io.BytesIO()
# io_obj.write(header)
# io_obj.write(idx_cols_b)
# io_obj.write(cols_b)

# np.save(io_obj,_df.values,allow_pickle=False)
# #calculate hash
# m = hashlib.md5(io_obj.getbuffer())
# md5hash_b = m.digest()
# io_obj.write(md5hash_b)


# io_obj.seek(0)
# _header = np.frombuffer(io_obj.read(16),dtype=np.int64)
# _idx_cols_b = io_obj.read(_header[0]).decode(encoding='UTF-8',errors='ignore')
# _cols_b = io_obj.read(_header[1]).decode(encoding='UTF-8',errors='ignore')
# _npy = np.load(io_obj)




# feeder.dataset_metadata.save()
# tini = time.time()
# feeder.load()
# print('total time %.2f' % (time.time()-tini))
# feeder['D1'].tags
# feeder.save()
# for md in shdata.metadata:
#     shdata.metadata[md].save()


# df = df.dropna(how='all',axis=0).dropna(how='all',axis=1)
# r, c = df.shape
# idx = (df.index.astype(np.int64))
# idx_b = idx.values.tobytes()
# cols = df.columns.values
# colscsv = ','.join(cols)
# colscsv_b = str.encode(colscsv,encoding='UTF-8',errors='ignore')
# nbidx = len(idx_b)
# nbcols = len(colscsv)
# data = np.ascontiguousarray(df.values.astype(np.float64))
# header = np.array([r,c,nbidx,nbcols,r*c*8]).astype(np.int64)
# #calculate hash
# m = hashlib.md5(idx_b)
# m.update(colscsv_b)
# m.update(data)
# md5hash_b = m.digest()
# # allocate memory
# io_obj = io.BytesIO()        
# io_obj.write(header)
# io_obj.write(idx_b)
# io_obj.write(colscsv_b)
# io_obj.write(data)
# io_obj.write(md5hash_b)

# gzip_io = io.BytesIO()
# gzip_obj = gzip.GzipFile(fileobj=gzip_io, mode='wb', compresslevel=1)
# gzip_obj.write(io_obj.getbuffer())
# gzip_obj.flush()
# len(gzip_io.getbuffer())

# gzip_io.seek(0)
# _gzip_obj = gzip.GzipFile(fileobj=gzip_io,mode='rb')
# _head_io = io.BytesIO()
# _head_io.write(gzip_obj.read())



# tini = time.time()
# # write ziped file in memory
# # create header
# r, c = df.shape
# idx = (df.index.astype(np.int64))
# idx_b = idx.values.tobytes()
# cols = df.columns.values
# colscsv = ','.join(cols)
# colscsv_b = str.encode(colscsv,encoding='UTF-8',errors='ignore')
# nbidx = len(idx_b)
# nbcols = len(colscsv)
# data = df.values.astype(np.float64)
# header = np.array([r,c,nbidx,nbcols,r*c*8]).astype(np.int64)
# #calculate hash
# m = hashlib.md5(idx_b)
# m.update(colscsv_b)
# m.update(data)
# md5hash_b = m.digest()
# # allocate memory
# io_obj = io.BytesIO()
# gzip_obj=gzip.GzipFile(fileobj=io_obj,mode='wb',compresslevel=1)
# gzip_obj.write(header)
# gzip_obj.write(idx_b)
# gzip_obj.write(colscsv_b)
# gzip_obj.write(data)
# gzip_obj.write(md5hash_b)
# gzip_obj.flush()
# print('total time %.2f' % (time.time()-tini))

# # write file to disk
# tini = time.time()
# f = open('m2m.bin.gz','wb')
# f.write(io_obj.getbuffer())
# f.flush()
# f.close()
# print('total time %.2f' % (time.time()-tini))

# # open file in memory
# # io_obj.seek(0)
# io_obj = open('m2m.bin.gz','rb')
# tini = time.time()
# _gzip_obj=gzip.GzipFile(fileobj=io_obj,mode='rb')
# _header = np.frombuffer(_gzip_obj.read(40),dtype=np.int64)
# _idx_b = _gzip_obj.read(int(_header[2]))
# _idx = pd.to_datetime(np.frombuffer(_idx_b,dtype=np.int64))
# _colscsv_b = _gzip_obj.read(int(_header[3]))
# _colscsv = _colscsv_b.decode(encoding='UTF-8',errors='ignore')
# _cols = _colscsv.split(',')
# _data = np.frombuffer(_gzip_obj.read(int(_header[4])),dtype=np.float64).reshape((_header[0],_header[1]))
# _df = pd.DataFrame(_data,index=_idx,columns=_cols)
# #calculate hash
# _m = hashlib.md5(_idx_b)
# _m.update(_colscsv_b)
# _m.update(_data)
# _md5hash_b = _m.digest()
# __md5hash_b = _gzip_obj.read(16)
# assert _md5hash_b==__md5hash_b
# print('total time %.2f' % (time.time()-tini))

# assert (_df.fillna(0)==df.fillna(0)).all().all()

