#!/usr/bin/python


# def printControls(br):
    # for control in br.form.controls:
        # print control
        # print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

import re, mechanize, time
from mechanize import Browser,Item
from datetime import datetime, timedelta
from BeautifulSoup import  BeautifulSoup, SoupStrainer, NavigableString
import cookielib

#set target url
url = 'http://www.nhb.gov.in/onlineclient/misdailyreport.aspx'
#url = 'file:///Users/andrewstershic/Code/tomato/tomato.html'

#set date DD/MM/YYYY
day = str(14)
month = str(10)
year = str(2014)

if (len(day) == 1):
	day = "0"+day
if (len(month) == 1):
	month = "0"+month
assert(len(day) == 2)
assert(len(month) == 2)

date = day+"/"+month+"/"+year
print date


# --------------------------------

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.open('http://nhb.gov.in/OnlineClient/categorywiseallvarietyreport.aspx')

date_used=datetime(datetime.now().year, datetime.now().month, datetime.now().day) - timedelta(days=1)
print date_used
data_date=str(date_used)[0:10]
print data_date
datevar=str(date_used)[8:10]+'/'+str(date_used)[5:7]+'/'+str(date_used)[0:4]
print datevar

br.select_form(nr=0)
br['txtdate'] = datevar
br['drpCategoryName'] = ['2 ']
br['LsboxCenterList'] = ['1','2','3','4','5','6','7','8','9','10','11','12','14','15','16','17','18','19','20','22','23','24','25','26','28','29','32','33','34','35','36','39','40']
time.sleep(5)
br.submit('btnSearch')
time.sleep(30)
html = br.response().read()
soup = BeautifulSoup(html)
soup.prettify()


f = open("tmp.htm","w")
f.write(html)
f.close()
