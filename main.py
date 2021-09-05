
import easyquotation

quotation = easyquotation.use('sina')

#all
#quotation.market_snapshot(prefix=True)
#print(quotation.market_snapshot(prefix=True))

#上证指数
#quotation.stocks(['sh000001', 'sz000001'], prefix=True)
#print(quotation.stocks(['sh000001'], prefix=True))

stocks_info = quotation.stocks(['sh000001'], prefix=True)

stocks_ones_info = stocks_info['sh000001']
print('='*30)
print('股票:'+stocks_ones_info['name'])
print('='*30)
print('今开:'+str(stocks_ones_info['open']))
print('昨收:'+str(stocks_ones_info['close']))
print('现价:'+str(stocks_ones_info['now']))
print('今日最高价:'+str(stocks_ones_info['high']))
print('今日最低价:'+str(stocks_ones_info['low']))
print('交易股数:'+str(stocks_ones_info['turnover']))
print('交易金额:'+str(stocks_ones_info['volume']))
'''
 {'sh000159': {'name': '国际实业', # 股票名
  'buy': 8.87, # 竞买价
  'sell': 8.88, # 竞卖价
  'now': 8.88, # 现价
  'open': 8.99, # 开盘价
  'close': 8.96, # 昨日收盘价
  'high': 9.15, # 今日最高价
  'low': 8.83, # 今日最低价
  'turnover': 22545048, # 交易股数
  'volume': 202704887.74， # 交易金额
  'ask1': 8.88, # 卖一价
  'ask1_volume': 111900, # 卖一量
  'ask2': 8.89,
  'ask2_volume': 54700,
  'bid1': 8.87, # 买一价
  'bid1_volume': 21800, # 买一量
  ...
  'bid2': 8.86, 
  'bid2_volume': 78400,
  'date': '2016-02-19',
  'time': '14:30:00',
'''