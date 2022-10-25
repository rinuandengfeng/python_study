import os
import urllib
import requests
from urllib import request

# 创建存放皮肤的文件夹
hero_dir = 'D:\img\\'
if not os.path.exists(hero_dir):
    os.mkdir(hero_dir)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Connection': 'close',  # 当请求成功后，马上断开该次请求（及时释放请求池中的资源）
}
url = 'http://pvp.qq.com/web201605/js/herolist.json'
res = requests.get(url=url, headers=headers)
# 返回的是json数据
res_json = res.json()
# 英雄总数
hero_num = len(res_json)
for i in range(hero_num):
    hero_name = res_json[i]['cname']
    # 英雄代码
    hero_code = res_json[i]['ename']
    # 跳过没有皮肤的
    if res_json[i].get('skin_name'):
        # 皮肤名称列表
        skin_list = res_json[i]['skin_name'].split('|')
        for j in range(len(skin_list)):
            # 每个皮肤的存放地址
            skin_path = hero_dir+ hero_name + '-' + skin_list[j] + '.jpg'
            # 每个皮肤的url地址
            skin_url = f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_code}/{hero_code}-bigskin-{j + 1}.jpg'
            urllib.request.urlretrieve(url=skin_url, filename=skin_path)
        print(hero_name + ' skins download success !')
print('over')
