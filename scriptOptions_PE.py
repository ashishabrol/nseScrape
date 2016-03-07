# Help Links
# python usage of Sqlite3 - http://www.pythoncentral.io/introduction-to-sqlite-in-python/
# Sqlite3
# BeautifulSoup - https://adesquared.wordpress.com/2013/06/16/using-python-beautifulsoup-to-scrape-a-wikipedia-table/
# bs4 installation - pip install BeautifulSoup4

# code to conver date to weekday name
# Help Links:
# 1) http://stackoverflow.com/questions/8380389/how-to-get-day-name-in-datetime-in-python
# 2) http://stackoverflow.com/questions/466345/converting-string-into-datetime
# from datetime import datetime
# dobj=datetime.strptime('14 nov 14', '%d %b %y')
# dobj.strftime("%A")
# unixtime is specially added to make sorting on date possible


# how to get weeknumber
# http://stackoverflow.com/questions/2600775/how-to-get-week-number-in-python
# geeting weekday name
# http://www.pythonexamples.org/2010/12/23/how-to-get-the-name-of-a-weekday-in-python/

from bs4 import BeautifulSoup
import urllib2
import sqlite3
from datetime import datetime
import time
import json
import arrow
strikes=[7500,7600,7700,7800,7900,8000,8100,8200,8300,8400,8500,8600,8700,8800,8900,9000]
expiry="27AUG2015"
for strike in strikes:
        wiki="http://nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxFOGetQuoteJSON.jsp?underlying=NIFTY&instrument=OPTIDX&expiry=%s&type=PE&strike=%s.00" % (expiry,strike)
        print wiki
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        req = urllib2.Request(wiki,headers=header)
        response=urllib2.urlopen(req)
        data=json.loads(str(response.read().strip()))
        #----------------------------------------------------------------------------------------------------------
        #print data["lastUpdateTime"]
        #print data["data"][0]["totalBuyQuantity"].replace(",","")
        #print data["data"][0]["totalSellQuantity"].replace(",","")
        #print data["data"][0]["highPrice"].replace(",","")
        #print data["data"][0]["lowPrice"].replace(",","")
        #print data["data"][0]["lastPrice"].replace(",","")
        #print data["data"][0]["closePrice"].replace(",","")
        #print data["data"][0]["openPrice"].replace(",","")
        #print data["data"][0]["prevClose"].replace(",","")
        #----------------------------------------------------------------------------------------------------------

        sDate= data["lastUpdateTime"] #date
        sDate=sDate + " +05:30"
        dt=arrow.get(sDate, 'DD-MMM-YYYY HH:mm:ss ZZ')
        ts=dt.timestamp

        unixtime=ts



        sOpen= data["data"][0]["openPrice"].replace(",","") #open
        sHigh= data["data"][0]["highPrice"].replace(",","") #high
        sLow= data["data"][0]["lowPrice"].replace(",","") #low
        sClose= data["data"][0]["closePrice"].replace(",","") #close
        sExpiryDate = data["data"][0]["expiryDate"]
        sSymbol=data["data"][0]["underlying"]
        sType=data["data"][0]["instrumentType"]
        sTBQ=data["data"][0]["totalBuyQuantity"].replace(",","")
        sTSQ=data["data"][0]["totalSellQuantity"].replace(",","")
        sLastPrice=data["data"][0]["lastPrice"].replace(",","")

        #__________NEW VALUES___________

        sSellPrice1 =data["data"][0]["sellPrice1"].replace(",","")
        sSellPrice2 =data["data"][0]["sellPrice2"].replace(",","")
        sSellPrice3 =data["data"][0]["sellPrice3"].replace(",","")
        sSellPrice4 =data["data"][0]["sellPrice4"].replace(",","")
        sSellPrice5 =data["data"][0]["sellPrice5"].replace(",","")

        sBuyPrice1  =data["data"][0]["buyPrice1"].replace(",","")
        sBuyPrice2  =data["data"][0]["buyPrice2"].replace(",","")
        sBuyPrice3  =data["data"][0]["buyPrice3"].replace(",","")
        sBuyPrice4  =data["data"][0]["buyPrice4"].replace(",","")
        sBuyPrice5  =data["data"][0]["buyPrice5"].replace(",","")

        sSellQuantity1  =data["data"][0]["sellQuantity1"].replace(",","")
        sSellQuantity2  =data["data"][0]["sellQuantity2"].replace(",","")
        sSellQuantity3  =data["data"][0]["sellQuantity3"].replace(",","")
        sSellQuantity4  =data["data"][0]["sellQuantity4"].replace(",","")
        sSellQuantity5  =data["data"][0]["sellQuantity5"].replace(",","")

        sBuyQuantity1   =data["data"][0]["buyQuantity1"].replace(",","")
        sBuyQuantity2  =data["data"][0]["buyQuantity2"].replace(",","")
        sBuyQuantity3  =data["data"][0]["buyQuantity3"].replace(",","")
        sBuyQuantity4  =data["data"][0]["buyQuantity4"].replace(",","")
        sBuyQuantity5  =data["data"][0]["buyQuantity5"].replace(",","")

        sVWAP=data["data"][0]["vwap"].replace(",","")
        sNumberOfContractsTraded =data["data"][0]["numberOfContractsTraded"].replace(",","")
        sOpenInterest  =data["data"][0]["openInterest"].replace(",","")
        sChangeinOpenInterest   =data["data"][0]["changeinOpenInterest"].replace(",","")
        sDailyVolatility    =data["data"][0]["dailyVolatility"].replace(",","")
        sExpiryDate     =data["data"][0]["expiryDate"].replace(",","")
        sTurnoverinRsLakhs      =data["data"][0]["turnoverinRsLakhs"].replace(",","")
        sPrevClose       =data["data"][0]["prevClose"].replace(",","")
        sPChange        =data["data"][0]["pChange"].replace(",","")
        sStrikePrice        =data["data"][0]["strikePrice"].replace(",","")
        sChange  =data["data"][0]["change"].replace(",","")
        sOptionType =data["data"][0]["optionType"].replace(",","")


        #Now insert the data into DB (sqlite3)
        db=sqlite3.connect("test.db",isolation_level=None)
        #without isolation_level code was not able to insert data into mysql even though there
        #were no errors thrown. Found the answer on stackoverflow
        cursor=db.cursor()
        try:
                cursor.execute("""INSERT INTO NIFTYOPTIONS (unixtime,mStrikePrice,mOpen,mHigh,mLow,mClose,mSymbol,mTbq,mTsq,mType,mLastPrice,mSellPrice1,mSellPrice2,mSellPrice3,mSellPrice4,mSellPrice5,mSellQuantity1,mSellQuantity2,mSellQuantity3,mSellQuantity4,mSellQuantity5,mBuyPrice1,mBuyPrice2,mBuyPrice3,mBuyPrice4,mBuyPrice5,mBuyQuantity1,mBuyQuantity2,mBuyQuantity3,mBuyQuantity4,mBuyQuantity5,mVWAP,mNumberOfContractsTraded,mOpenInterest,mChangeinOpenInterest,mDailyVolatility,mExpiryDate,mTurnoverinRsLakhs,mPrevClose,mPChange,mChange,mOptionType ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(unixtime,sStrikePrice,sOpen,sHigh,sLow,sClose,sSymbol,sTBQ,sTSQ,sType,sLastPrice,sSellPrice1,sSellPrice2,sSellPrice3,sSellPrice4,sSellPrice5,sSellQuantity1,sSellQuantity2,sSellQuantity3,sSellQuantity4,sSellQuantity5,sBuyPrice1,sBuyPrice2,sBuyPrice3,sBuyPrice4,sBuyPrice5,sBuyQuantity1,sBuyQuantity2,sBuyQuantity3,sBuyQuantity4,sBuyQuantity5,sVWAP,sNumberOfContractsTraded,sOpenInterest,sChangeinOpenInterest,sDailyVolatility,sExpiryDate,sTurnoverinRsLakhs,sPrevClose,sPChange,sChange,sOptionType))
        except sqlite3.IntegrityError:
                print "primary key violation"		
        db.commit
        db.close()
                
        #'17-JUL-2015 15:30:31




        

