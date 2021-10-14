
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

fig, axes = plt.subplots(nrows=3, ncols=1)
axes[0].set(xlim=[1, len(data_list)], ylim=[1, 150000], title='sh.000300 沪深300 [默认投资] 本金10000元 历史收益', ylabel='元', xlabel='交易日')
axes[1].set(xlim=[1, len(data_list)], ylim=[1, 150000], title='sh.000300 沪深300 [投资方案1 稳固] 本金10000元 历史收益', ylabel='元', xlabel='交易日')
axes[2].set(xlim=[1, len(data_list)], ylim=[1, 150000], title='sh.000300 沪深300 [投资方案2 平均] 本金10000元 历史收益', ylabel='元', xlabel='交易日')

money = 10000

money0 = money
money1 = money
money2 = money

x0 = []
y0 = []

x1 = []
y1 = []

x2 = []
y2 = []

money1_buy = 0
money1_buy_point = 0

money2_buy = 0

for i in range(len(data_list)-1):

    money0 += (money0*float(data_list[i+1][2])/100)
    x0.append(i)
    y0.append(money0)

    if float(data_list[i][2]) <= -0.1:
        money1_buy_point += 1
    if float(data_list[i][2]) >= 0.1:
        money1_buy_point -= 1

    if money1_buy_point == 3:
        money1_buy += 3000
    if money1_buy_point == -3:
        money1_buy -= 3000

    if money1_buy <= 0:
        money1_buy = 0
    if money1_buy >= money1:
        money1_buy = money1
    
    else:
        money1_buy = money1_buy

    money1 = money1 + (money1_buy*float(data_list[i+1][2])/100)

    x1.append(i)
    y1.append(money1)

    if float(data_list[i][1]) <= 2000:
        money2_buy += 100

    if float(data_list[i][1]) >= 4000:
        money2_buy -= 10

    money2 = money2 + (money2_buy*float(data_list[i+1][2])/100)

    x2.append(i)
    y2.append(money2)

axes[0].plot(x0,y0)
axes[1].plot(x1,y1)
axes[2].plot(x2,y2)

axes[0].set(title='sh.000300 沪深300 [默认投资] 本金10000元 历史收益'+str(money0))
axes[1].set(title='sh.000300 沪深300 [投资方案1 稳固] 本金10000元 历史收益'+str(money1))
axes[2].set(title='sh.000300 沪深300 [投资方案2 平均] 本金10000元 历史收益'+str(money2))

plt.show()
