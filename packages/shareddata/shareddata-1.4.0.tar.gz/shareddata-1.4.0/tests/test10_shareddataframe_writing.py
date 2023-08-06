import pandas as pd


from SharedData.Logger import Logger
logger = Logger(__file__)

from SharedData.Metadata import Metadata
from SharedData.SharedData import SharedData

futchain = Metadata('BBG/FUT_CHAIN')
futseries = Metadata('BBG/FUT_SERIES')
lvidx = futseries.symbols.last_valid_index()
activefuts = futseries.symbols.loc[lvidx].dropna()
activefuts = activefuts[[s in futchain.static.index for s in activefuts.values]]
activefuts = pd.DataFrame(activefuts)
activefuts.columns=['symbol']
activefuts['bloombergsymbol'] = futchain.static.loc[activefuts['symbol']]['bloombergsymbol'].values
tickers = activefuts['bloombergsymbol'].values
# tickers = ['XBTUSD CURNCY']
columns = ['bid','ask','last_price','volume']
df = pd.DataFrame(index=tickers,columns=columns,dtype=float)

shdata = SharedData('MarketData','w')
feeder = shdata['BBG/RT']['D1']
dt = pd.Timestamp(pd.Timestamp.now().date())
feeder[dt] = df
feeder.tags[dt].Write()