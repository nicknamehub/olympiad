import requests, datetime, re
from bs4 import BeautifulSoup
class Olympiad: #создание класса олимпиады
    name = ""
    status = ""
    desc = ""
    class_start = 0
    class_stop = 0
    date = []  # {start, end, name}
    link = ""
    subject = ""
    id_sub = 0
    rate = 0
    id = 0

def subject_name(id_sub):
    url = 'https://olimpiada.ru/include/activity/megatitle.php?type=any&subject%5B' + str(id_sub) + '%5D=on&class=any&period_date=&period=year'
    s = requests.get(url)
    b = BeautifulSoup(s.text,"html.parser")
    sub_str = str(b)
    sub_str = sub_str[sub_str.find('   ')+4:]
    sub_str = sub_str[sub_str.find(' ')+2:]
    sub_str = sub_str[sub_str.find(' ')+1:]
    print(sub_str)

def is_sub_exist(id_sub):
    kol_vo = 0
    url = 'http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B' + str(id_sub) + '%5D=on&class=any&period_date=&period=year&cnow=' + str(kol_vo)
    s = requests.get(url)
    b = BeautifulSoup(s.text, "html.parser")
    if str(b) == 'stop':
        return False
    else:
        return True

def time_edit(string,date_start):
    """Функция, изменяющая формат строку даты в нужный нам формат"""
    if string != None:
        string = re.sub('\xa0', ' ',string)
        if string.find('<') != -1:
            pop_index = string.find('<')
            string = list(string)
            string.pop(pop_index)
            string = ''.join(string)
        months = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек', 'янв']
        month_start = date_start[date_start.index('-')+1:date_start.rindex('-')]
        day = string[:string.index(' ')]
        if string[string.index(' ')+1:].find(' ') != -1:
            month = months.index(string[string.index(' ')+1:string.rindex(' ')]) + 1
        else:
            month = months.index(string[string.index(' ')+1:]) + 1
        d = datetime.date.today()
        if month < int(month_start):
            year = str(d.year + 1)
        else:
            year = str(d.year)
        if len(str(month)) == 1:
            month = '0' + str(month)
        if len(day) == 1:
            day = '0' + day
        date = year + '-' + str(month) + '-' + day
    else:
        date = None
    return date

def parse_sub(id_sub):
    olimpiads = []
    kol_vo = 0
    url = 'http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B' + str(id_sub) + '%5D=on&class=any&period_date=&period=year&cnow=' + str(kol_vo)
    s = requests.get(url)
    b = BeautifulSoup(s.text, "html.parser")
    #print(b)
    if str(b) == 'stop':
        return False
    if b.find('div', {'class': 'fav_olimp olimpiada new_data_fav'}) != None:
        block = b.find('div', {'class': 'fav_olimp olimpiada new_data_fav'})
    else:
        block = b.find('div', {'class': 'fav_olimp olimpiada '})
    while block != None:
        x = Olympiad()
        x.name = block.find('span',{'class':'headline'}).text
        href_block = block.find('a',{'class':'none_a black'})
        href_block = str(href_block)
        href = 'https://olimpiada.ru' + href_block[href_block.index('href="')+6:href_block.index('" style')]
        x.link = href
        #print(href)
        x.id = int(href[href.find('ity/')+4:])
        #print(x.id)
        rate_str = block.find('span', {'class': 'pl_rating'}).text
        rate_str = list(rate_str)
        rate_str[1] = '.'
        rate_str = ''.join(rate_str)
        x.rate = float(rate_str)
        x.date = []
        if block.find('div', {'class':'timeline'}) != None:
            timeline = block.find('div', {'class':'timeline'})
            dates = timeline.findAll('div')
            for i in range (len(dates)):
                date_name = dates[i].find('font', {'style': 'font-weight: normal;'}).text
                date_name = str(date_name)
                date_name = re.sub('\xa0', ' ',date_name)
                dates[i] = str(dates[i])
                date_start = dates[i][dates[i].index('date="')+6:dates[i].index('" ev_act=')]
                if dates[i].find('...') != -1:
                    date_stop = dates[i][dates[i].find('...')+3:dates[i].find('...')+9]
                else:
                    date_stop = None
                date_stop = time_edit(date_stop,dates[i][dates[i].index('date="')+6:dates[i].index('" ev_act=')])
                x.date.append({'start':date_start, 'stop':date_stop, 'name':date_name})
        if block.find('span', {'class': 'headline red'}) != None:
            x.status = (block.find('span', {'class': 'headline red'}).text)
        else:
            x.status = ''
        classes = block.find('span', {'class': 'classes_dop'}).text
        if classes.find('–') != -1:
            x.class_start = int(classes[:classes.find('–')])
            x.class_stop = int(classes[classes.find('–')+1:classes.find(' ')])
        else:
            if (classes.find(' ') != -1) and (classes.find(',') == -1):
                x.class_start = int(classes[:classes.find(' ')])
                x.class_stop = int(classes[:classes.find(' ')])
            elif classes.find(',') == -1:
                x.class_start = 1
                x.class_stop = 11
        if block.find('span', {'class': 'headline red'}) != None:
            x.desc = block.find('a', {'class': 'none_a black olimp_desc'}).text
        else:
            x.desc = ''
        x.id_sub = id_sub
        x.subject = subject_name(id_sub)
        olimpiads.append(x)
        #print(olimpiads[kol_vo].name, olimpiads[kol_vo].status, olimpiads[kol_vo].desc, olimpiads[kol_vo].class_start, olimpiads[kol_vo].class_stop, olimpiads[kol_vo].rate, olimpiads[kol_vo].date)
        #print(olimpiads[kol_vo].date)
        print(olimpiads[kol_vo].subject)
        kol_vo += 1
        url = 'http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B' + str(id_sub) + '%5D=on&class=any&period_date=&period=year&cnow=' + str(kol_vo)
        s = requests.get(url)
        b = BeautifulSoup(s.text, "html.parser")
        block = b.find('div', {'class':'fav_olimp olimpiada '})
        #print(x.name,':',len(x.date))
    #print(len(olimpiads))
    return olimpiads
#start_time = time.time() #нужно для замера времени работы программы
parse_sub(24)
#print(time_edit('18 янв','2018-09-30'))
#print(find_olimpiad_id('https://olimpiada.ru/activity/39'))
#print("--- %s seconds ---" % (time.time() - start_time))
#subject_name(27)
