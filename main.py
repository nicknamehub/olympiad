import json
from parse_class_1 import *
import requests

url = 'http://nicknameproject.pythonanywhere.com/update_db'
olimpiads = []
index = 0
i = 1
call = is_sub_exist(i)
while call != False:
    olimpiads.append(parse_sub(i))
    i += 1
    call = is_sub_exist(i)
#print(olimpiads)
for k in range(len(olimpiads)):
    for q in range(len(olimpiads[k])):
        olimpiads[k][q] = {'name': olimpiads[k][q].name, 'status': olimpiads[k][q].status,
                           'description': olimpiads[k][q].desc, 'class_start': olimpiads[k][q].class_start,
                           'class_stop': olimpiads[k][q].class_stop, 'date': olimpiads[k][q].date,
                           'link': olimpiads[k][q].link, 'subject': olimpiads[k][q].subject,
                           'id_sub': olimpiads[k][q].id_sub, 'rate': olimpiads[k][q].rate, 'id': olimpiads[k][q].id, 'real_link': olimpiads[k][q].real_link}
res = {'user': 'admin', 'password': open('password.txt').read().strip('\n'), 'data': olimpiads}
res_json = json.dumps(res, sort_keys=True)
res = requests.post(url, json=res)
print(res_json, res)
