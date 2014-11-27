#!/usr/bin/python
#Andrew Stershic, 11/27/2014

def str2num(a):
    #remove comma from large numbers
    return float(a.replace(',',''))

def yearOfDate(date):
    hyp = date.rfind("-")
    date = date[hyp+1:]
    return int(date)

def monthOfDate(date):
    if "Jan" in date:
        return 1
    if "Feb" in date:
        return 2
    if "Mar" in date:
        return 3
    if "Apr" in date:
        return 4
    if "May" in date:
        return 5
    if "Jun" in date:
        return 6
    if "Jul" in date:
        return 7
    if "Aug" in date:
        return 8
    if "Sep" in date:
        return 9
    if "Oct" in date:
        return 10
    if "Nov" in date:
        return 11
    if "Dec" in date:
        return 12
    return -1

from bs4 import BeautifulSoup
import urllib2

#set target url
urlEx = 'https://www.zauba.com/export-tomato+puree-hs-code.html'
urlIm = 'https://www.zauba.com/export-tomato+puree-hs-code.html'

#export
page = urllib2.urlopen(urlEx)
soup = BeautifulSoup(page.read())

date = []
type = []
HScode = []
description = []
destOrigin = []
origin = []
port = []
unit = []
qty = []
value = []
valueperunit = []

allTR = soup.find_all('tr')
for i in range(0,len(allTR)):
    tr = allTR[i]
    tds = tr.find_all('td')
    
    if (len(tds) != 9):
        continue

    date.append(tds[0].text.strip())	
    type.append("Export")
    HScode.append(tds[1].text.strip())		
    description.append(tds[2].text.strip())		
    destOrigin.append(tds[3].text.strip())
    port.append(tds[4].text.strip())	
    unit.append(tds[5].text.strip())	
    qty.append(tds[6].text.strip())	
    value.append(tds[7].text.strip())		
    valueperunit.append(tds[8].text.strip())		

#import
page = urllib2.urlopen(urlIm)
soup = BeautifulSoup(page.read())

allTR = soup.find_all('tr')
for i in range(0,len(allTR)):
    tr = allTR[i]
    tds = tr.find_all('td')
    
    if (len(tds) != 9):
        continue

    date.append(tds[0].text.strip())
    type.append("Import")	
    HScode.append(tds[1].text.strip())		
    description.append(tds[2].text.strip())		
    destOrigin.append(tds[3].text.strip())
    port.append(tds[4].text.strip())	
    unit.append(tds[5].text.strip())	
    qty.append(tds[6].text.strip())	
    value.append(tds[7].text.strip())		
    valueperunit.append(tds[8].text.strip())		

month = []
year = []
for i in range(0,len(date)):
    month.append(monthOfDate(date[i]))
    year.append(yearOfDate(date[i]))

f = open("zauba_output.csv",'w')

header = "#type,date,month,year,HScode,description,destOrigin,port,unit,qty,value,valueperunit"
f.write(header)
for i in range(0,len(date)):
    line = "%s,%s,%u,%u,%u,%s,%s,%s,%s,%f,%f,%f\n" % (type[i],date[i],month[i],year[i],int(HScode[i]),description[i],destOrigin[i],port[i],unit[i],str2num(qty[i]),str2num(value[i]),str2num(valueperunit[i]))
    f.write(line)

f.close()
