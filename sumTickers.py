import pandas as pd
import numpy as np

def sum_tickers_and_create_result(df):
    df.QTY = df.SIDE*df.QTY
    df2 = df.groupby(['TICKER']).sum()
    df2.rename(columns={'SIDE': 'SIDE_RESULT'}, inplace = True)
    return df2