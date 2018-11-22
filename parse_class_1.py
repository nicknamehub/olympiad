import requests, time, datetime, re
from bs4 import BeautifulSoup
class Olympiad:
    name = ""
    status = ""
    desc = ""
    classes = []
    date = []  # {start, end, name}
    link = ""
    subject = ""
    id_sub = 0
    rate = 0

def time_edit(string,date_start):
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
    names = []
    status = []
    classes = []
    description = []
    date = []
    link = []
    rate = []
    kol_vo = 0
          #http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B24%                 5D=on&class=any&period_date=&period=year&cnow=7
    url = 'http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B' + str(id_sub) + '%5D=on&class=any&period_date=&period=year&cnow=0' + str(kol_vo)
    s = requests.get(url)
    b = BeautifulSoup(s.text, "html.parser")
    if b.find('', {'class': 'fav_olimp olimpiada new_data_fav'}) != None:
        block = b.find('div', {'class': 'fav_olimp olimpiada new_data_fav'})
    else:
        block = b.find('div', {'class': 'fav_olimp olimpiada '})
    while block != None:
        names.append(block.find('span',{'class':'headline'}).text)
        href_block = block.find('a',{'class':'none_a black'})
        href_block = str(href_block)
        href = 'https://olimpiada.ru' + href_block[href_block.index('href="')+6:href_block.index('" style')]
        link.append(href)
        rate_str = block.find('span', {'class': 'pl_rating'}).text
        rate_str = list(rate_str)
        rate_str[1] = '.'
        rate_str = ''.join(rate_str)
        rate.append(float(rate_str))
        date.append([])
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
                date[kol_vo].append({'start':date_start, 'stop':date_stop, 'name':date_name})
        if block.find('span', {'class': 'headline red'}) != None:
            status.append(block.find('span', {'class': 'headline red'}).text)
        else:
            status.append('')
        classes.append(block.find('span', {'class': 'classes_dop'}).text)
        if block.find('span', {'class': 'headline red'}) != None:
            description.append(block.find('a', {'class': 'none_a black olimp_desc'}).text)
        else:
            description.append('')
        print(names[kol_vo], kol_vo)# status[kol_vo], description[kol_vo], rate[kol_vo], classes[kol_vo], link[kol_vo], date[kol_vo], kol_vo)
        kol_vo += 1
        url = 'http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B' + str(id_sub) + '%5D=on&class=any&period_date=&period=year&cnow=0' + str(kol_vo)
        s = requests.get(url)
        b = BeautifulSoup(s.text, "html.parser")
        block = b.find('div', {'class':'fav_olimp olimpiada '})
    for i in range (kol_vo):
        x = Olympiad()
        olimpiads.append(x)
    print(len(names), len(status), len(classes), len(description))
start_time = time.time()
parse_sub(24)
#print(time_edit('18 янв','2018-09-30'))
print("--- %s seconds ---" % (time.time() - start_time))
#http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B24%5D=on&class=any&period_date=&period=year&cnow=6
#http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B24%5D=on&class=any&period_date=&period=year&cnow=7
#http://olimpiada.ru/include/activity/megalist.php?type=any&subject%5B24%5D=on&class=any&period_date=&period=year&cnow=8
