#-*- coding:utf-8 -*-

import urllib.request
import json
import time
import os

start = time.time()
respond = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")

respond = respond.read().decode('utf-8')  # 防止出现编码问题
respond = respond.encode('utf-8')[3:].decode('utf-8')

json_hero = json.loads(respond)
hero_num = len(json_hero)

hero_dir = 'D:\img\\'
if not os.path.exists(hero_dir):
    os.mkdir(hero_dir)

x = 0

for i in range(hero_num):
    skin_names = json_hero[i]['skin_name'].split('|')

    for cnt in range(len(skin_names)):
        save_file_name = (hero_dir + str(json_hero[i]['ename']) + '-' + json_hero[i]['cname'] + '-'
                          + skin_names[cnt] + '.jpg')
        skin_url = ('http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(json_hero[i]['ename']) + '/'
                    + str(json_hero[i]['ename']) + '-bigskin-' + str(cnt + 1) + '.jpg')
        urllib.request.urlretrieve(skin_url, save_file_name)
        time.sleep(1)
        x += 1
        print("正在下载...第" + str(x) + "张")

end = time.time()
time_second = end - start
print("共下载" + str(x) + "张,共耗时" + str(time_second) + "秒")
