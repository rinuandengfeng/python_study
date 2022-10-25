# -*- coding:utf-8 -*-
import requests
import json
import os
import time

start = time.time()

respond = requests.get('http://pvp.qq.com/web201605/js/herolist.json')

respond = respond.read()
respond = respond.encode('utf-8')[3:].decode('utf-8')
json_hero = json.loads(respond)

x = 0
hero_dir = 'D:\img\\'
if not os.path.exists(hero_dir):
    os.mkdir(hero_dir)

for m in range(len(hero_dir)):
    save_file_name = (hero_dir + str(json))
    x = x + 1
    print("正在下载....第" + str(x) + "张")

end = time.time()
time_second = end - start
print("共下载" + str(x) + "张，共耗时" + str(time_second) + "秒")

# ename = json_hero[m]['ename']
#     cname = json_hero[m]['cname']
#     skinName = json_hero[m]['skin_name'].split('|')
#
#     skinNumber = len(skinName)
#
#     for bigskin in range(1,skinNumber+1):
#         urlPocture = 'http://game.gtimg.cn/images/yxzj/img201605/heroimg/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(bigskin) + '.jpg'
#
#         picture = requests.get(urlPocture).content
#
#         with open(hero_dir + cname +"-" + skinName[bigskin-1] + '.jpg', 'wb') as f:
#             f.write(picture)
