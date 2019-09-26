html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')  # 声明对象并选定解析方式
print(soup.prettify())  # prettify()方法将html格式化并补齐代码
print(soup.title.string) #输出title标签内容
#更多内容查看https://www.cnblogs.com/mzc1997/p/7813819.html