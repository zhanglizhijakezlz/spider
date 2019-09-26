from lxml import etree #导入lxml的etree模块

text='''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)#调用HTML类 初始化 构造一个XPath解析对象
#result = html.xpath('//li//a')和result = html.xpath('//li/a')结果一样
result = html.xpath('//li//a')
print(result)
#//ul//a和//ul/a结果不一样
result = html.xpath('//ul//a')
print(result)

result = html.xpath('//li[@class="item-0"]/text()') #此处的含义是直接获取子节点
print(result)#返回结果为 换行符

result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)#返回预期结果

result = html.xpath('//li[@class="item-0"]//text()')
print(result)#返回三个结果