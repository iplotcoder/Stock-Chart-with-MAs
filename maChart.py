from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyEX
import os
# from os.path import join, dirname
import dotenv

dotenv.load_dotenv()
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)


API = os.getenv('API')

p = pyEX.Client(API)
ticker = 'NKLA'
timeframe = '6m'

df = p.chartDF(ticker, timeframe) # retrieve ticker data as a dataframe and store as df
df = df[['close']] # want chart to be based off close price
df.reset_index(level=0, inplace=True)
df.columns=['ds','pri']

plt.plot(df.ds, df.pri)
plt.show()





# # prints key stats about the ticker
# stats = p.keyStats(ticker)
# for i in stats:
#     print(i, ": ", stats[i], sep="")
