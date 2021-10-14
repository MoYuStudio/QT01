
# -*- coding: utf-8 -*-

import baostock as bs
import pandas as pd
import datetime
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

stock = "sh.000300"

start_date= '2000-01-01'
end_date= datetime.datetime.today().strftime("%Y-%m-%d")

lg = bs.login()

rs = bs.query_history_k_data(stock, "date,close,pctChg",start_date, end_date, frequency="d", adjustflag="3")

data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[1, len(data_list)], ylim=[1, 100000], title='sh.000300 沪深300 [默认投资] 本金10000元 历史收益', ylabel='元', xlabel='交易日')

money = 10000

x = []
y = []

for i in range(len(data_list)):

    money += (money*float(data_list[i][2])/100)
    x.append(i)
    y.append(money)

ax.plot(x,y)
plt.show()