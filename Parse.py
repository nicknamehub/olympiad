import requests, re
from bs4 import BeautifulSoup
import time

def parse_subjects_list():  
    subject = [''] * 5
    url_start = 'https://olimpiada.ru/activities?type=any&subject%5B'
    url_end = '%5D=on&class=any&period_date=&period=year'
    for i in range(5):
        s = requests.get(url_start + str(i) + url_end)
        #string = driver.find_element_by_id('megatitle').text
        b = BeautifulSoup(s.text, "html.parser")
        string = str(b.find('div', {'id': 'filter_fixed'}).find('font'))
        index = string.index('</span> ')
        index2 = string.index('</font>')
        subject[i] = string[index+8:index2]
        subject[i] = re.sub('\t','',subject[i])
        subject[i] = re.sub('\xa0', ' ',subject[i])
        #print(i, ': ',subject[i])
    #driver.close()
    return subject

def parse():
    subjects = parse_subjects_list()
    main_url_start = 'https://olimpiada.ru/activities?type=any&subject%5B'
    main_url_end = '%5D=on&class=any&period_date=&period=year'
    kol_vo_olimpiads = [0] * len(subjects)
    blocks = [0] * len(subjects)
    names = []
    classes = []
    rate = []
    description = []
    for i in range(len(subjects)):
        s = requests.get(main_url_start + str(i) + main_url_end)
        soup = BeautifulSoup(s.text, "html.parser")
        string = str(soup.find('h1').text)
        string = string[:string.index(' ')]
        #print(string)
        kol_vo_olimpiads[i] = int(string)
        if kol_vo_olimpiads[i] != 0:
            blocks[i] = (kol_vo_olimpiads[i] // 20) + 1
        else:
            blocks[i] = 0
        names.append([])
        classes.append([])
        rate.append([])
        description.append([])
        if blocks[i] != 0:
            for k in range(blocks[i]):
                step = (20 * k)
                url = 'http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B' + str(i) + '%5D=on&class=any&period_date=&period=year&cnow=' + str(step)
                site = requests.get(url)
                soups = BeautifulSoup(site.text,'html.parser')
                #print(soups)
                names[i].extend(soups.findAll('span', {'class':'headline'}))
                classes[i].extend(soups.findAll('span', {'class':'classes_dop'}))
                rate[i].extend(soups.findAll('span', {'class':'class="pl_rating"'}))
                description[i].extend(soups.findAll('span', {'class':'headline red'}))
            for q in range (len(names[i])):
                names[i][q] = str(names[i][q])
                #print(type(names[i][q]))
                names[i][q] = names[i][q][names[i][q].index('style="">')+9:names[i][q].index('</span>')]
            for q in range (len(description[i])):
                description[i][q] = str(description[i][q])
                description[i][q] = description[i][q][description[i][q].index('>')+1:description[i][q].index('</span>')]
                names[i].remove(description[i][q])
            for w in range (len(classes[i])):
                classes[i][w] = str(classes[i][w])
                #if classes[i][w] != None:
                classes[i][w] = classes[i][w][classes[i][w].index('>')+1:classes[i][w].rindex('<')]
    #print(names, classes, rate,sep = "\n")    
        #print(subjects[i], ':', kol_vo_olimpiads[i])
    for i in range(len(subjects)):
        print(subjects[i],':','\n', names[i],len(names[i]),'\n', classes[i],len(classes[i]),'\n',description[i])
    
start_time = time.time()
parse()
print("--- %s seconds ---" % (time.time() - start_time))
