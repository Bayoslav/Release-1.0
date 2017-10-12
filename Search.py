import requests
import json
import bs4 as bs
import re
#http://www.urbanhome.ch/Search/DoSearch
payload = {
  "settings": {
    "MainTypeGroup": "1",
    "Category": "1",
    "AdvancedSearchOpen": "false",
    "MailID": "",
    "PayType": "1",
    "Type": "0",
    "RoomsMin": "0",
    "RoomsMax": "0",
    "PriceMin": "0",
    "PriceMax": "0",
    "Regions": [
      "188542"
    ],
    "SubTypes": [
      "0"
    ],
    "SizeMin": "0",
    "SizeMax": "0",
    "Available": "",
    "NoAgreement": "false",
    "FloorRange": "0",
    "RentalPeriod": "0",
    "equipmentgroups": [],
    "Email": "",
    "Interval": "0",
    "SubscriptionType1": "true",
    "SubscriptionType2": "true",
    "SubscriptionType4": "true",
    "SubscriptionType8": "true",
    "SubscriptionType128": "true",
    "SubscriptionType512": "true",
    "Sort": "0"
  },
  "manual": 'false',
  "skip": 25,
  "reset": 'false',
  "position": 16,
  "iframe": 0,
  "defaultTitle": 'true',
  "saveSettings": 'false'
}
r=requests.post('http://www.urbanhome.ch/Search/DoSearch',json=payload)
src = r.text
json = json.loads(r.content)
rows = (json.get('Rows'))
#print(type(rows))
#print(rows)
rows=rows.encode('latin1').decode('unicode-escape')
#print(rows)
soup = bs.BeautifulSoup(rows,'lxml')
#print(soup)

for ad in soup.find_all('div', class_='a ax'):
    url = (ad.find('a').get('href'))
    title =  (ad.find('a').text)
    adress = (ad.find('div', class_='a ay'))
    street = (adress.find('p',class_='pt15').text)
    pcode = (adress.find('p',class_='').text)
    equipment = []
    for equi in ad.find_all('span', class_='fl pr6'):
        equipment.append(equi.text)
    print(street)
    print(pcode)
    print("TITLE: " + title + "\nURL: " + url + "\n Adress: " + street + " " + pcode + "\nEquipment: " + str(equipment))




#print(unicoded)
