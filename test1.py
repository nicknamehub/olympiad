from selenium import webdriver
driver = webdriver.Chrome()
subject = []
url_start = 'https://olimpiada.ru/activities?type=any&subject%5B'
url_end = '%5D=on&class=any&period_date=&period=year'
for i in range(34):
    driver.get(url_start + str(i) + url_end)
    string = driver.find_element_by_id('megatitle').text
driver.close()
