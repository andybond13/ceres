#!/usr/bin/python
#Andrew Stershic, 10/20/2014

def str2num(a):
    #remove comma from large numbers
    return float(a.replace(',',''))

import sys
import re
import mechanize

#set target url
url = 'http://commerce.nic.in/eidb/icomq.asp'
year = 2014
if len(sys.argv) > 1:
	year = sys.argv[1]
fruitcode = "0702"

br = mechanize.Browser()
br.open(url)

br.select_form(name="form1")

#set year
br["yy1"] = [str(year)]

#select tomato = "0702"
br["hscode"] = fruitcode

#submit
response = br.submit()

#save results
#f = open("tmp.htm","w")
#f.write(response.read())
#f.close()


#read results
from bs4 import BeautifulSoup

page = open('tmp.htm','r')
soup = BeautifulSoup(page)

allTR = soup.find_all('tr')
TR1 = []
TR2 = []
for i in range(0,len(allTR)):
    tr = allTR[i]
    tds = tr.find_all('td')
    for td in tds:
#        print td.text.strip()
        if (i == 1):
            TR1.append(str(td.text.strip()))
        if (i == 2):
            TR2.append(str(td.text.strip()))

#save results to variables
sNo = TR1[0]
HSCode = TR1[1]
Commodity = TR1[2]
QtyYear = str2num(TR1[3])
TotImportYear = str2num(TR2[3])
PctShareYear = str2num(TR1[4])
QtyCurrent = str2num(TR1[5])
TotImportCurrent = str2num(TR2[5])
PctShareCurrent = str2num(TR1[6])
PctGrowth = str2num(TR1[7])
TotImportPctGrowth = str2num(TR2[7])


line = "%s,%s,%s,%s,%f,%f,%f,%f,%f,%f,%f,%f\n" % (year,sNo,HSCode,Commodity,QtyYear,TotImportYear,PctShareYear,QtyCurrent,TotImportCurrent,PctShareCurrent,PctGrowth,TotImportPctGrowth)
header = "#year,sNo,HSCode,Commodity,QtyYear,TotImportYear,PctShareYear,QtyCurrent,TotImportCurrent,PctShareCurrent,PctGrowth,TotImportPctGrowth\n"

f = open("commerce_output.csv",'w')
f.write(header)
f.write(line)
f.close()


#results (commented)
#***---results---***
#sNo 1.
#HSCode 0702
#Commodity TOMATOES, FRESH OR CHILLED
#QtyYear 1.38
#TotImportYear 266916195.69
#PctShareYear 0.0
#QtyCurrent 1.78
#TotImportCurrent 271543390.74
#PctShareCurrent 0.0
#PctGrowth 29.17
#TotImportPctGrowth 1.73

