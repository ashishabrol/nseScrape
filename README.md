# nseScrape
Scraping NSE Website for TBQ and TSQ
Script.py is the main source code file. It carries a variable "wiki" which points to a weblink which shows current price and various
properties of the nifty contract. NSE updates this link every 2 minutes during market hours

urllib2 is used to fetch response (ajax) from the wiki link.
json package is used to analye response. 
arrow package is used for time conversion.
sqlite is db.

How to run script.py as cron job
* * * * * root PYTHONPATH=/usr/local/lib/python2.7/site-packages; export PYTHONPATH; /usr/local/bin/python2.7 /root/nseScrape/scriptOptions_CE.py
* * * * * root PYTHONPATH=/usr/local/lib/python2.7/site-packages; export PYTHONPATH; /usr/local/bin/python2.7 /root/nseScrape/scriptOptions_PE.py
* * * * * root PYTHONPATH=/usr/local/lib/python2.7/site-packages; export PYTHONPATH; /usr/local/bin/python2.7 /root/nseScrape/scriptFuture.py



Note:
script.py and scriptoptions.py are obsolete and are not needed.

Commands to search based on unxtime values

SELECT strftime('%d-%m-%Y', datetime(unixtime,'unixepoch')) FROM niftyfuture;
select date(unixtime,'unixepoch') from niftyfuture where date(unixtime,'unixepoch')="2015-08-04";
