from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import time
now = datetime.now() # current date and time

DATE = now.strftime("%d.%m.%Y")
login_url = 'https://www.comdirect.de/'
DATA = pd.read_csv("wertpapiere.txt")
OUTPUT = []

for NUMBER in (DATA['ISIN'].values):
	VALUE = {"SEARCH_VALUE":NUMBER}
	with requests.Session() as s:    
		response = requests.post("https://www.comdirect.de/inf/search/all.html", VALUE)		
		soup = BeautifulSoup(response.text, 'html.parser')
		print(soup.title)
		#KURS = soup.find(class_= "realtime-indicator--value text-size--xxlarge text-weight--medium").getText()
		KURS = soup.find(class_= "text-size--xxlarge").getText()
		print (KURS,NUMBER,DATE)
		OUTPUT.append((KURS,NUMBER,DATE))		
		time.sleep(1)
print (OUTPUT)
df = pd.DataFrame (OUTPUT)
print (df)
df.to_csv('output.csv',sep=',', index = False, header = False)

#https://www.comdirect.de/inf/search/all.html?SEARCH_VALUE=fielmann
### 01.03.2020: funktioniert so, man beachte den _ bei class, nötig da class bereits in python definiert ist 
### Ergebnis muss noch aufgehübscht werden