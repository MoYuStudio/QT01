
import baostock as bs
import pandas as pd
import datetime

code = "sh.000300"

datestart = '2000-01-01'

datetoday = datetime.datetime.today().strftime("%Y-%m-%d")

"date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST"
ShowList ="date,close,pctChg"

def ListToDf(rs):

    data_list = []

    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        
    return result

lg = bs.login()
print('login respond error_msg:'+lg.error_msg)

rs = bs.query_history_k_data_plus(code,ShowList,start_date=datestart, end_date=datetoday,frequency="d", adjustflag="3")
result = ListToDf(rs)
print('query_history_k_data_plus respond error_msg:'+rs.error_msg)

print(result)

result.to_excel('history_A_stock_k_' + code + '.xls', index=False)

bs.logout()