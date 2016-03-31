import sqlite3
from lxml import etree
from lxml.etree import tostring
from lxml.builder import E
from mako.template import Template

from bottle import route, run, static_file,template,request

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



@route('/orderbook')
def home():
        args=request.query.decode()
        str1="select * from niftyfuture where "
        for key in args.iterkeys():
            if key=="quantity":
                if args[key].startswith('>') or args[key].startswith('<') or args[key].startswith('!'):
                    str1+="(mBuyQuantity1{0} or ".format(args[key])
                    str1+="mBuyQuantity2{0} or ".format(args[key])
                    str1+="mBuyQuantity3{0} or ".format(args[key])
                    str1+="mBuyQuantity4{0} or ".format(args[key])
                    str1+="mBuyQuantity5{0} or ".format(args[key])

                    str1+="mSellQuantity1{0} or ".format(args[key])
                    str1+="mSellQuantity2{0} or ".format(args[key])
                    str1+="mSellQuantity3{0} or ".format(args[key])
                    str1+="mSellQuantity4{0} or ".format(args[key])
                    str1+="mSellQuantity5{0}) and ".format(args[key])
                    
            if key=="date":
                if args[key].startswith('>') or args[key].startswith('<') or args[key].startswith('!'):
                    str1+="date1{0}date(\'{1}\') and ".format(args[key][0],args[key][1:])
                else:
                    str1+="date1=date(\'{0}\') and ".format(args[key])

        str1=(str1.strip()).rsplit(' ', 1)[0]
        str1=str1.replace("date1", "date(unixtime,'unixepoch')")
	str1+=" and mLastPrice !=\'-\'"
        q=str1
	print str1
        db=sqlite3.connect("test.db",isolation_level=None)
        cursor=db.cursor()
        cursor.execute(q)
        htmlfile=open("tmplhtml.html","w")
        mytemplate=Template(filename='tmpl12.txt')
        htmlfile.write(mytemplate.render(cursor=cursor))
	htmlfile.close()
        htmlfile=open("tmplhtml.html","r")
        var=htmlfile.read()
	htmlfile.close()
	return var
        return static_file("tmplhtml.html",root="")




run(host='vps70976.vps.ovh.ca',port=8080, debug=True)
