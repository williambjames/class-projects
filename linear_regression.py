# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AvpQPV9rXlOp9BBS941dBrS3RxBL8Fhu
"""

#RaspberryCanary
#Last edited: Oct 2, 2020
#Challenge 2
#Sources consulted: Course WIKI, https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style

df = pd.read_csv('/content/RaspberryCanary.csv')

filter = df.groupby('freq')[['ms','intensity']].corr().iloc[0::2,-1].to_frame(name='value').reset_index(level=1,drop=True)
filter = filter.loc[(filter['value'].abs() > .5)]
signals = df.loc[(df['freq'].isin(filter.index))]

colors = {1497:'#d62060',1543:'#9920d6',1535:'#45ad23',1605:'#e6df2e',1617:'#2e47e6'}

def lin_plot(xs,ys):
  for u in signals.freq:
    new = signals.loc[(signals['freq']==u)]

    #Slope = Correlation(x,y) * stdY/stdX
    m =  np.corrcoef(new.ms,new.intensity).item(1) * (np.std(new.intensity)/(np.std(new.ms)))
    #Using .item(1) allows me extract the non 1 value from the corr matrix
    b = np.mean(new.intensity) - m*np.mean(new.ms)
    regression_line = [(m*x)+b for x in new.ms]
    sns.scatterplot(x='ms',y='intensity',data=df,hue='freq',s=200,palette=colors,legend=False)
    sns.lineplot(x='ms',y= regression_line,data=new,color='r')

  

  # return m, b

def poly(xs,ys):
  for u in signals.freq:
    new = signals.loc[(signals['freq']==u)]
    coef = np.polyfit(new.ms,new.intensity,2)
    poly_line = [np.polyval(coef,x) for x in new.ms]
    sns.lineplot(x='ms',y= poly_line,data=new,color='b')

fig, ax = plt.subplots(figsize=(10,10))
style.use('fivethirtyeight')
plt.title('Challenge 2')
plt.xlabel('Time (ms)')
plt.ylabel('Signal Intensity')
lin_plot(signals.ms,signals.intensity)
poly(signals.ms,signals.intensity)