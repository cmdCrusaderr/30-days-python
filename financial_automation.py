#making a automation for financial stuff like
#specific topic equity mutual funds , and news from a website like moneycontrol
from notifypy import Notify
import requests
from notifypy import BaseNotifier
from bs4 import BeautifulSoup

#making a request using get function
#we can also define url here 
#url='link'

#making a list of the active and popular equity mutual funds , considering 6 here 
watchlist=['Quant Mid Cap Fund','Quant ELSS Tax Saver Fund','Quant Flexi Cap Fund','Motilal Oswal Midcap Fund','Quant Active Fund','Edelweiss Mid Cap Fund']



req=requests.get('https://www.etmoney.com/mutual-funds/equity')

#parsing the fetched url 
mutual_funds=BeautifulSoup(req.text,'html-parser')
#we need scheme name , expense ratio , 5y retun annualised

scheme_name=mutual_funds.find('div',{'class'})

print(scheme_name,e_ratio,five_year)
#now parsing and finding the elements by class


