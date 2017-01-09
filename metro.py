#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
from datetime import datetime
report = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
url = 'http://www.metrosantiago.cl/'
#Usare la version mobile para recolectar datos del sitio, definiendo y realizando los ajustes en headers.
header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522+ (KHTML, like Gecko) Safari/419.3",
        "Content-Type": "text/html; charset=utf-8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
web = requests.get(url, headers=header)
html = BeautifulSoup(web.text,"lxml")
tabla = html.find_all("div", attrs={"class":"ui-body ui-body-c"}, limit=1)
incidente = []

for col in tabla:
    for small in col.find_all("small"):
         small1 = small.getText().encode('latin-1')
         incidente.append(small1)

print '\t  Metro de Santiago'
print 'Estado de red:',
for i in range(len(incidente)):print incidente[i]

print 'Reporte consultado:',report
