#帮我写一份爬虫代码
import requests
from bs4 import BeautifulSoup

# 定义一个函数get_html，用于获取12306网站的html代码
url = 'https://www.12306.cn/mormhweb/'
# 定义一个url，用于存储12306网站的url
r = requests.get(url)
# 使用requests模块的get方法，获取url对应的html代码
r.encoding = 'utf-8'
# 设置html代码的编码格式为utf-8
soup = BeautifulSoup(r.text, 'html.parser')
# 使用BeautifulSoup模块的html.parser解析html代码
print(soup.prettify())
