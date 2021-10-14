
import baostock as bs
import pandas as pd
import datetime

# code = "sz.002484" #查询的股票代码

# sh sz
code = "sh.000300"

datestart = '2019-07-01' #开始时间

datetoday = datetime.datetime.today().strftime("%Y-%m-%d")

ShowList ="date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST"

def ListToDf(rs):

    data_list = []

    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        print(result)

    return result

#### 登陆系统 ####

lg = bs.login()
print('login respond error_msg:'+lg.error_msg)

#### 获取沪深A股历史K线数据 ####

rs = bs.query_history_k_data_plus(code,ShowList,start_date=datestart, end_date=datetoday,frequency="d", adjustflag="3")
result = ListToDf(rs)
print('query_history_k_data_plus respond error_msg:'+rs.error_msg)

#### 结果集输出到csv文件 ####

result.to_excel('history_A_stock_k_' + code + '.xls', index=False)

#### 登出系统 ####

bs.logout()