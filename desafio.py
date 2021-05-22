import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from findErrors import find_errors_and_format
from sumTickers import sum_tickers_and_create_result

with open('gotham_op.txt') as f:
    lines = f.readlines()

df,dic_errors = find_errors_and_format(lines)
df = sum_tickers_and_create_result(df)

open('results.txt', 'w').close()
df.to_csv(r'results.txt', sep=';', mode='a')
print(df)
print('\n')
for i in dic_errors:
    print(i,str(dic_errors[i]))
with open("results.txt", 'a') as results:
    for i in dic_errors:
        results.write('\n')
        results.write(i+' '+str(dic_errors[i]))
    results.close()