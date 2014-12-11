#!/usr/bin/python

def brnl(elem):
    text = ''
    for e in elem.recursiveChildGenerator():
        if isinstance(e, basestring):
            text += e.strip()
        elif e.name == 'br':
            text += ','
    return text

import re, mechanize, time
from mechanize import Browser,Item
from datetime import datetime, timedelta
from bs4 import  BeautifulSoup, SoupStrainer, NavigableString
import cookielib

#set date DD/MM/YYYY
#day = str(14)
#month = str(10)
#year = str(2014)

#if (len(day) == 1):
#	day = "0"+day
#if (len(month) == 1):
#	month = "0"+month
#assert(len(day) == 2)
#assert(len(month) == 2)

#date = day+"/"+month+"/"+year
#print date


# --------------------------------

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.open('http://nhb.gov.in/OnlineClient/categorywiseallvarietyreport.aspx')

date_used=datetime(datetime.now().year, datetime.now().month, datetime.now().day) - timedelta(days=1)
data_date=str(date_used)[0:10]
datevar=str(date_used)[8:10]+'/'+str(date_used)[5:7]+'/'+str(date_used)[0:4]
day = str(date_used)[8:10]
month = str(date_used)[5:7]
year = str(date_used)[0:4]
print "date: dd/mm/yyyy",datevar

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


br.select_form(nr=0)
br.submit('btnExcel')
time.sleep(30)
html = br.response().read()
soup = BeautifulSoup(html)
soup.prettify()

#f = open("try.html","w")
#f.write(html)
#f.close()

center = []
variety = []
minPrice = []
maxPrice = []
modelPrice = []
retailPrice = []
arrivalQty = []

trs = soup.find_all('tr')
for i in range(0,len(trs)):
    if (i == 0):
        continue
    tr = trs[i]
    tds = tr.find_all('td')
    
    for j in range(0,len(tds)):
        td = tds[j]
        #list = [0,1,15,16]
        list = [0,15,16]
        #(0): center/state
        #(1): headers: MinPrice,MaxPrice,ModelPrice,RetailPrice,ArrivalQty
        #(15): tomato_hybrid 
        #(16): tomato_local
        if j not in list: 
            continue
        line = brnl(td)
        if (len(line) == 0):
            assert(j == 15 or j ==16)
            #print "j = ",j,": N/A"
            if (j == 15):
                variety.append("Tomato Hybrid")
                minPrice.append("N/A")
                maxPrice.append("N/A")
                modelPrice.append("N/A")
                retailPrice.append("N/A")
                arrivalQty.append("N/A")
            if (j == 16):
                variety.append("Tomato Local")
                minPrice.append("N/A")
                maxPrice.append("N/A")
                modelPrice.append("N/A")
                retailPrice.append("N/A")
                arrivalQty.append("N/A")
            continue 
        if (line[-1] == ","):
            line = line[:-1]
        line = line.split(',')
        if (j == 0):
            assert(len(line) >= 1)
            #print "State:",line[0]
            center.append(line[0])
            center.append(line[0])
        if (j == 15):
            variety.append("Tomato Hybrid")
            if (len(line) >= 5):
                #print "Tomato Hybrid:",line[0:4]
                minPrice.append(float(line[0]))
                maxPrice.append(float(line[1]))
                modelPrice.append(float(line[2]))
                retailPrice.append(float(line[3]))
                arrivalQty.append(float(line[4]))
            else:
                #print "N/A"
                minPrice.append("N/A")
                maxPrice.append("N/A")
                modelPrice.append("N/A")
                retailPrice.append("N/A")
                arrivalQty.append("N/A")

        if (j == 16):
            variety.append("Tomato Local")
            if (len(line) >= 5):
                #print "Tomato Local:",line[0:4]
                minPrice.append(float(line[0]))
                maxPrice.append(float(line[1]))
                modelPrice.append(float(line[2]))
                retailPrice.append(float(line[3]))
                arrivalQty.append(float(line[4]))
            else:
                #print "N/A"
                minPrice.append("N/A")
                maxPrice.append("N/A")
                modelPrice.append("N/A")
                retailPrice.append("N/A")
                arrivalQty.append("N/A")

assert(len(center) == len(variety))
assert(len(center) == len(minPrice))
assert(len(center) == len(maxPrice))
assert(len(center) == len(modelPrice))
assert(len(center) == len(retailPrice))
assert(len(center) == len(arrivalQty))

#save to file

f = open("nhb_output.csv",'w')
 
header = "#date,month,day,year,center,variety,minPrice,maxPrice,modelPrice,retailPrice,arrivalQty\n"
f.write(header)
for i in range(0,len(center)):
    line = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (datevar,month,day,year,center[i],variety[i],minPrice[i],maxPrice[i],modelPrice[i],retailPrice[i],arrivalQty[i])
    f.write(line)
f.close()
