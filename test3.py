import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
import warnings
warnings.filterwarnings("ignore")

#股票代码、起止日期可替换
caixin = ts.get_hist_data('600633', start='2017-07-01', end='2020-05-08') 

nanfang = ts.get_hist_data('601900',start='2017-07-01', end='2020-05-08')

#收盘价close
data = {'浙江传媒财新': caixin.close, '南方传媒':nanfang.close}
df = pd.DataFrame(data)

#排序
df.sort_values(by='date',ascending=True,inplace=True)

#pandas支持matplotlib的，直接使用df.plot(kind='line')画折线图
import matplotlib.pyplot as plt

df.plot(kind='line')
plt.xticks(rotation = '45')
plt.show()
