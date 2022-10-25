import re
import requests
import json


def getLOLImages():
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    html_js = requests.get(url_js).text
    # print(html_js)
    req = '"key":(.*?),"data"'
    # print(req)
    list_js = re.findall(req, html_js)
    # print(list_js[0])

    dict_js = json.loads(list_js[0])

    pic_list = []
    for hero_id in dict_js:
        print(hero_id)
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = "00" + num
            elif len(num) == 2:
                hero_num = "0" + num
            print(hero_num)

            numstr = hero_id + hero_num
            url = 'http://ossweb-img.11.com/images/lol/web201310/skin/big1' + numstr + 'jpg'
            pic_list.append(url)
    list_filepath = []

    path = "D:\img\\"

    for name in dict_js.values():
        print(name)
        for i in range(20):
            file_path = path + name + str + ".jpg"
            list_filepath.append(file_path)

        n = 0
        for picurl in pic_list:
            res = requests.get(picurl)

            n = n + 1
            if res.status_code == 200:
                print("正在下载%s:" % list_filepath[n])

                with open(list_filepath[n], "web") as f:
                    f.write(res.content)


getLOLImages()
