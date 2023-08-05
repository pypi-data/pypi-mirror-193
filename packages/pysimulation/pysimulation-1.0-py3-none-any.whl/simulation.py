import os
import pandas as pd
import datetime
import pytz
from decimal import *

class order:
    def __init__(self, account) :
        self.account = account
        self.order = []
    
    def place_order(self, bidask, action, octype):
        if action == 'Buy':
             
            print('Order(\ncode:\t%s\naction:\t%s\noctype:\t%s\nprice:\t%s\nfee:\t%s\ntax:\t%s\nts:\t%s\n)'%(bidask['code'], action, octype, str(bidask['ask_price'][0]), '50', str(round(bidask['ask_price'][0] * 200 * 2 / 100000)), str(datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')),'%Y-%m-%d %H:%M:%S'))))
            self.order.append({
                'code': bidask['code'],
                'action': action,
                'octype': octype,
                'price': round(bidask['ask_price'][0]),
                'fee': 50,
                'tax': round(bidask['ask_price'][0] * 200 * 2 / 100000),
                'ts': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')),'%Y-%m-%d %H:%M:%S')
            })
            update_order(self.account, (self.order)[-1])
        elif action == 'Sell':
            
            print('Order(\ncode:\t%s\naction:\t%s\noctype:\t%s\nprice:\t%s\nfee:\t%s\ntax:\t%s\nts:\t%s\n)'%(bidask['code'], action, octype, str(bidask['bid_price'][0]), '50', str(round(bidask['bid_price'][0] * 200 * 2 / 100000)), str(datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')),'%Y-%m-%d %H:%M:%S'))))
            self.order.append({
                'code': bidask['code'],
                'action': action,
                'octype': octype,
                'price': round(bidask['bid_price'][0]),
                'fee': 50,
                'tax': round(bidask['bid_price'][0] * 200 * 2 / 100000),
                'ts': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')),'%Y-%m-%d %H:%M:%S')
            })
            update_order(self.account, (self.order)[-1])
    
    def list_trades(self):
        return self.order
        
def update_order(account, order):
    df = pd.DataFrame(order, index=[0])
    df.set_index('ts', inplace=True)
    if os.path.isfile('%s_order.csv'%account):
        df = pd.concat([pd.read_csv('%s_order.csv'%account, index_col='ts'), df], axis=0)
        df.to_csv('%s_order.csv'%account)
    else:
        df.to_csv('%s_order.csv'%account)