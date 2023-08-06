import os
import boto3
from botocore.utils import fix_s3_host
from datetime import datetime
import time
import pandas as pd
import numpy as np

from SharedData.Logger import Logger
logger = Logger(__file__,user='master')
from SharedData.MultiProc import io_bound_process
from SharedData.Metadata import Metadata
from SharedData.SharedData import SharedData
from SharedData.SharedDataAWSS3 import S3Download

shdata = SharedData('Signals')
tini = time.time()

shdata['FUTROLL']['D1']['level_delta']
shdata['FUTROLL'].load()
print(time.time()-tini)

# tini = time.time()
# shdata['CSI/FUT'].save()
# print(time.time()-tini)


# # def S3DownloadThread(iteration, args):
# #     return [S3Download(iteration,check_if_exists=False)]
# tini = time.time()
# shm_name = 'master/MarketData/CSI/FUT/D1/m2m'
# bucket_name = os.environ['S3_BUCKET'].replace('s3://','')
# session = boto3.Session()
# s3 = session.resource('s3')
# print(time.time()-tini)
# bucket = s3.Bucket(bucket_name)
# success=True
# dbfolder = os.environ['DATABASE_FOLDER']
# files = np.array([dbfolder+'\\'+obj_s.key.replace('/','\\')\
#     for obj_s in bucket.objects.filter(Prefix=shm_name+'/')])
# tini = time.time()    
# result = io_bound_process(S3DownloadThread,files,None)
# print(time.time()-tini)



# shdata = SharedData('MarketData')
# dt= pd.Timestamp('2022-12-02')
# df = shdata['BVMF/BVBG086']['D1'][dt]

# md = Metadata('test')
# md.static.loc['test','test'] = 'test'
# md.save()
# md = Metadata('test')

# local_path = r'C:\Users\jcooloj\DB\master\Metadata\CSI\FUT_SERIES.pkl'
# bucket_name = os.environ['S3_BUCKET'].replace('s3://','')
# s3_path = str(local_path).replace(os.environ['DATABASE_FOLDER'],'').replace('\\','/')[1:]
# session = boto3.Session()
# s3 = session.resource('s3')
# # obj exists
# bucket = s3.Bucket(bucket_name)
# if len(list(bucket.objects.filter(Prefix=s3_path)))>0:
#     # load obj
#     obj = s3.Object(bucket_name, s3_path)
#     # remote mtime size
#     remote_mtime = obj.last_modified.timestamp()
#     if 'mtime' in obj.metadata:
#         remote_mtime = float(obj.metadata['mtime'])
#     remote_size = obj.content_length
#     # local mtime size
#     local_mtime = datetime.utcfromtimestamp(os.path.getmtime(local_path)).timestamp()
#     local_size = os.path.getsize(local_path)
#     #compare
#     isnewer = remote_mtime>local_mtime
#     ischg = remote_size!=local_size
#     if isnewer or ischg:
#         obj.download_file(local_path)
#         # update modification time
#         remote_mtime_dt = datetime.fromtimestamp(remote_mtime)
#         offset =  remote_mtime_dt - datetime.utcfromtimestamp(remote_mtime)        
#         remote_mtime_local_tz = remote_mtime_dt+offset
#         remote_mtime_local_tz_ts = remote_mtime_local_tz.timestamp()
#         os.utime(local_path, (remote_mtime_local_tz_ts, remote_mtime_local_tz_ts))


# datetime.fromtimestamp(float(obj.metadata['mtime']))
# datetime.utcfromtimestamp(float(obj.metadata['mtime']))

# local_path = 'C:/Users/jcooloj/DB/master/Metadata/test.pkl'
# mtime = int(os.path.getmtime(local_path))
# datetime.utcfromtimestamp(mtime).timestamp()
# mtime_str = str(mtime)


# session = boto3.Session()
# s3 = session.resource('s3',\
#     endpoint_url='http://192.168.0.199:9000',\
#     aws_access_key_id = 'sBj6y99xpZWXHUFZ',\
#     aws_secret_access_key = 'bcKeTVlqacT8t5TiKqWytsOOSvcL2idy')

# s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)
# bucket_name = os.environ['S3_BUCKET'].replace('s3://','')
# bucket = s3.Bucket(bucket_name)

# tini = time.time()
# keys = [obj_s.key for obj_s in bucket.objects.filter(Prefix='master')]
# print('elapsed %.2f' % (time.time()-tini))
# len(keys)


# tini = time.time()
# for obj_s in bucket.objects.filter(Prefix='master'):
#     obj = s3.Object(bucket_name, obj_s.key)
#     #print(obj_s.key,obj_s.size,obj_s.last_modified)
# print('elapsed %.2f' % (time.time()-tini))
    
# local_path = 'C:/Users/jcooloj/DB/master/Metadata/CSI/FIRST_SERIES.pkl'
# mtime = int(os.path.getmtime(local_path))
# mtime_str = str(mtime)

# obj_s = s3.ObjectSummary(bucket_name, 'master/Metadata/CSI/FIRST_SERIES.pkl')
# obj = s3.Object(bucket_name, 'master/Metadata/CSI/FIRST_SERIES.pkl')
# obj_s.last_modified
# datetime.fromtimestamp(float(obj.metadata['mtime']))
