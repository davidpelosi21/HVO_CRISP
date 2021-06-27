import pandas as pd
#import csv

file1 = open('/var/www/html/SSN/DTXT/SSN_Monthly_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]
err=[]


for i  in range(len(Lines)-5):
    Lines2 = Lines[i+5].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(insert[0])
    ssn.append(insert[1])
    err.append(insert[2])
    
dati = pd.DataFrame({'Date': date, 'SSN monthly': ssn,'Err': err})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati = dati.set_index('Date')
dati.to_csv('ssn_monthly.csv')
dati.head() 
