import re

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
result = re.search('li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.group(1))
print(result.group(2))

result = re.findall('li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
for results in result:
  print(results[0],results[1],results[2])

html = re.sub('<a.*?>|</a>','',html)
# print(html)
results = re.findall('<li.*?>(.*?)</li>',html,re.S)
# print(results)
for result in results:
  print(result.strip())#去掉字符串两边的空格或者换行符


str1 = '2016-12-25 12:00'
str2 = '2017-12-17 11:55'
str3 = '2018-12-23 15:00'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',str1)
result2 = re.sub(pattern,'',str2)
result3 = re.sub(pattern,'',str3)
print(result1,result2,result3)