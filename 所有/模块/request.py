import requests
import random
#豆瓣首页

url='https://www.douban.com/'
#用于模拟http头的User——agent
user_list = (
    {'user-agent':"MOzilla/5.0(Macintosh;Intel Mac OS X 10.6;rv2.0.1)Gecko/20100101 Firefox/4.0.1"},
    {'user-agent':"Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
    {'user-agent':"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U ; en)Presto/2.8.131 Version/11.11"},
    {'user-agent':"Opera/9.80 (Windows NT 6.1; U;en) Presto/2.8.131 Version/11.11"},
    {'user-agent':"Mozilla/5.0 (MAcintosh;Intel Mac OS X 10_7_0) AppleWebkit/535.11 (KHTML,like Gecko) Chrome/17.0.963.56 Safari/535.11"}
)
user_agent = random.choice(user_list)
r = requests.get(url , headers = user_agent)


r.status_code
# print(r.text)
print(r.encoding)
# print(r.content)
