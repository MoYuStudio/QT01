
import baostock as bs
import pandas as pd

lg = bs.login()

rs = bs.query_history_k_data("000001.SH", "date,close,pctChg",start_date='2010-01-01', end_date='2019-12-31', frequency="d", adjustflag="3")

data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())

print(data_list[1])

result = pd.DataFrame(data_list, columns=rs.fields)

