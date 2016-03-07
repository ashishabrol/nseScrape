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

wiki="http://nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxFOGetQuoteJSON.jsp?underlying=NIFTY&instrument=FUTIDX&expiry=30JUL2015&type=SELECT&strike=SELECT"
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


#Now insert the data into DB (sqlite3)
db=sqlite3.connect("test.db",isolation_level=None)
#without isolation_level code was not able to insert data into mysql even though there
#were no errors thrown. Found the answer on stackoverflow
cursor=db.cursor()
try:
	cursor.execute("""INSERT INTO NIFTY (unixtime,mOpen,mHigh,mLow,mClose,mSymbol,mTbq,mTsq,mType,mLastPrice ) VALUES (?,?,?,?,?,?,?,?,?,?)""",(unixtime,sOpen,sHigh,sLow,sClose,sSymbol,sTBQ,sTSQ,sType,sLastPrice))
except sqlite3.IntegrityError:
	print "primary key violation"		
db.commit
db.close()
	
#'17-JUL-2015 15:30:31