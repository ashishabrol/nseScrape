import sqlite3 as lite
import sys

db=lite.connect('test.db')
cursor=db.cursor()
month="2016-03-03"
cursor.execute("select * from niftyfuture  where date(unixtime,'unixepoch')=?",(month,))
print "time    BuyQuanity    BuyPrice      SellQuantity SellPrice"
for row in cursor:
    print "%s|    %s|     %s|    %s|     %s|" %(row[0],row[28],row[23],row[13],row[18])
    print "%s|    %s|     %s|    %s|     %s|" %(row[0],row[29],row[24],row[14],row[19])
    print "%s|    %s|     %s|    %s|     %s|" %(row[0],row[30],row[25],row[15],row[20])
    print "%s|    %s|     %s|    %s|     %s|" %(row[0],row[31],row[26],row[16],row[21])
    print "%s|    %s|     %s|    %s|     %s|" %(row[0],row[32],row[27],row[17],row[22])
db.close()
