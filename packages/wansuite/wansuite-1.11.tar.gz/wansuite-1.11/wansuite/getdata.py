import numpy as np
import pandas as pd
import ib_insync
from ib_insync import *
import sqlite3
import wansuite as ws






def downloadstock(sql,table,enddate,duration):
    """
    enddate=2023"+"0210"+" 19:00:00"
    duration="60 D"
    """
    

    util.startLoop()
    ib = IB()
    ib.connect('localhost', 7496, clientId=np.random.randint(10000))
    conn=sqlite3.connect(sql,timeout=10)
    cursor=conn.cursor()
    stocklist=ws.wsql.getPossibleValue(sql,table,"ticker")
    misslist=[]
    for n in range(len(stocklist)): # #for stock in 
        if n%500==0:
            print(n)
        try: 
            stock=stocklist[n]
            st=Stock(stock,"SMART","USD")
            bars = ib.reqHistoricalData(st, 
                            endDateTime=endate,
                            durationStr=duration,
                            barSizeSetting="5 mins",
                            whatToShow="TRADES", #TRADES
                            useRTH=0,
                            keepUpToDate=False,                    
                            formatDate=1)
            for dt in bars:
                cursor.execute(""" 
                    INSERT INTO equity (datetime,ticker, open, close, high, low, volume, barsize ) 
                    VALUES(?,?,?,?,?,?,?,?)""",(str(dt.date),stock,dt.open,dt.close,dt.high,dt.low,dt.volume,dt.barCount))
        except:
            print("cannot download",st)
            misslist.append(stock)
    return misslist
    conn.commit()
    conn.close()