import requests
import shutil
import os
from DECIMAL import decimal_year
import time
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from import2  import simple_get


url = simple_get("http://wso.stanford.edu/Polar.html")
html = BeautifulSoup(url, 'html.parser')
f = open('/var/www/html/Wilcox_SFS/SFS.txt', "w")
for i, pre in enumerate(html.select('pre')):
    f.write("%s" %(pre.text))

lines1 = tuple(open('/var/www/html/Wilcox_SFS/SFS.txt', "r"))
with open(time.strftime('/var/www/html/Wilcox_SFS/SFS.txt'), "w") as file:
 for i in range(len(lines1)):
    if i > 2:
        file.write(lines1[i])


lines1 = tuple(open(time.strftime('/var/www/html/Wilcox_SFS/SFS.txt'), "r"))
fileN = open(time.strftime('/var/www/html/Wilcox_SFS/SFSNorth.txt'), "w")
fileS =  open(time.strftime('/var/www/html/Wilcox_SFS/SFSSouth.txt'), "w")
fileA =  open(time.strftime('/var/www/html/Wilcox_SFS/SFSAvg.txt'), "w")
fileNf = open(time.strftime('/var/www/html/Wilcox_SFS/SFSNf.txt'), "w")
fileSf =  open(time.strftime('/var/www/html/Wilcox_SFS/SFSSf.txt'), "w")
fileAf =  open(time.strftime('/var/www/html/Wilcox_SFS/SFSAvgf.txt'), "w")


for j in range(len(lines1)):
 if( len(lines1[j]) > 1):
   year  = int(lines1[j][0]+lines1[j][1]+lines1[j][2]+lines1[j][3])
   month = int(lines1[j][5]+lines1[j][6])
   day   = int(lines1[j][8]+lines1[j][9])
   sline = lines1[j].split()
   sline[1] = sline[1].replace("N","")
   #sline[2] = sline[2].replace(sline[2][len(sline[2])-1],"")                   
   sline[2] = sline[2].replace("S","")
   sline[3] = sline[3].replace("A","")
   sline[3] = sline[3].replace("v","")
   sline[3] = sline[3].replace("g","")
#grafico filtrato 20nhz                                                         
   sline[6] = sline[6].replace("N","")
   sline[6] = sline[6].replace("f","")
   sline[7] = sline[7].replace("S","")
   sline[7] = sline[7].replace("f","")
   sline[8] = sline[8].replace("A","")
   sline[8] = sline[8].replace("v","")
   sline[8] = sline[8].replace("g","")
   sline[8] = sline[8].replace("f","")
   #print(str(decimal_year(year,month,day)))
   a = str(decimal_year(year,month,day))
   fileN.write(a + "  " + sline[1] + "\n")
   fileA.write(a  + "  " + sline[3] + "\n")
   fileS.write(a  + "  " + sline[2] + "\n")
   fileNf.write(a + "  " + sline[6] + "\n")
   fileAf.write(a  + "  " + sline[8] + "\n")
   fileSf.write(a  + "  " + sline[7] + "\n")
