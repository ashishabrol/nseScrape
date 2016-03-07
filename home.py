import sqlite3
from lxml import etree
from lxml.etree import tostring
from lxml.builder import E
from mako.template import Template

from bottle import route, run, static_file,template

@route('/home')
def home():
    db=sqlite3.connect("test.db",isolation_level=None)
    cursor=db.cursor()
    cursor.execute("select unixtime,mLastPrice,mBuyQuantity1, mSellQuantity1  from niftyfuture")
    htmlfile=open("tmplhtml.html","w")
    mytemplate=Template(filename='tmpl1.txt')
    htmlfile.write(mytemplate.render(cursor=cursor))
    htmlfile.close()
    return static_file("tmplhtml.html",root="")

@route('/contract/<month>')
def contract(month):
    db=sqlite3.connect("test.db",isolation_level=None)
    cursor=db.cursor()
    cursor.execute("select unixtime,mLastPrice,mBuyQuantity1, mSellQuantity1  from niftyfuture where date(unixtime,'unixepoch')=?",(month,))
    htmlfile=open("tmplhtml.html","w")
    mytemplate=Template(filename='tmpl1.txt')
    htmlfile.write(mytemplate.render(cursor=cursor))
    htmlfile.close()
    return static_file("tmplhtml.html",root="")		

@route('/orderbook/<month>')
def orderbook(month):
    db=sqlite3.connect("test.db",isolation_level=None)
    cursor=db.cursor()
    cursor.execute("select * from niftyfuture  where date(unixtime,'unixepoch')=?",(month,))
    htmlfile=open("tmplhtml_orderbook.html","w")
    mytemplate=Template(filename='tmpl1_orderbook.txt')
    htmlfile.write(mytemplate.render(cursor=cursor))
    htmlfile.close()
    return static_file("tmplhtml_orderbook.html",root="")

run(host='vps70976.vps.ovh.ca',port=8080, debug=True)
