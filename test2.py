import requests
from bs4 import BeautifulSoup
subject = [''] * 34
url_start = 'https://olimpiada.ru/activities?type=any&subject%5B'
url_end = '%5D=on&class=any&period_date=&period=year'
for i in range(34):
    s = requests.get(url_start + str(i) + url_end)
    #string = driver.find_element_by_id('megatitle').text
    b = BeautifulSoup(s.text, "html.parser")
    string = str(b.find('div', {'id': 'filter_fixed'}).find('font'))
    index = string.index('</span> ')
    index2 = string.index('</font>')
    subject[i] = string[index+8:index2]
    print(i, ': ',subject[i]) 
#driver.close()
