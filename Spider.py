import requests
import bs4 as bs
url = (input('Enter link: '))
#url = 'http://www.urbanhome.ch/suchen/2499910-4-5-zimmer-wohnung'
r = requests.get(url)
soup = bs.BeautifulSoup(r.text,'lxml')
#print(soup)
#<span class="db" itemprop="streetAddress">Aeckerwiesenstrasse 24</span>
for equi in soup.find_all('small',class_='cb'):
    print(equi.text)

adress = soup.find('span', class_='db', attrs={'itemprop':'address'})
street = adress.find('span',class_='db',attrs={'itemprop':'streetAddress'})
print(street.text)
postalcode = adress.find('span',attrs={'itemprop':'postalCode'})
print(postalcode.text)


print("KEK")
#http://www.urbanhome.ch/Search/DoSearch - ROWS!
#payload - #skip: 0-25,+16+22+16+22, position:0-16 + 16...
