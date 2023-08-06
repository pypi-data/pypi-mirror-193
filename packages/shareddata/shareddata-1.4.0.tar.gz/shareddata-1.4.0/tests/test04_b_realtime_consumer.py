import time

from SharedData.Logger import Logger
from SharedData.SharedDataAWSKinesis import KinesisStreamConsumer

streamname = 'deepportfolio-real-time-marketdata'

logger = Logger(__file__)
Logger.log.info('Starting Kinesis Stream Consumer Loop')
consumer = KinesisStreamConsumer(streamname)

while True:
    consumer.consume()
    for record in consumer.stream_buffer:
        print(record)
    consumer.stream_buffer = []
    time.sleep(1)

    