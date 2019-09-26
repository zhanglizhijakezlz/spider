from lxml import etree

text = ''' 
        <div> 
            <ul> 
                <li class="item-1"><a href="link1.html">first item</a></li> 
                <li class="item-1"><a href="link2.html">second item</a></li> 
                <li class="item-inactive"><a href="link3.html">third item</a></li> 
                <li class="item-1"><a href="link4.html">fourth item</a></li> 
                <li class="item-0"><a href="link5.html">fifth item</a> 
                # 注意，此处缺少一个 </li> 闭合标签 
            </ul> 
        </div> 

'''

# 使用etree,创建对象,把文本转换成elements对象
html = etree.HTML(text)

# 提取多条数据,需要对提取的结果进行遍历，或者说再次xpath
data_list = html.xpath('//div/ul/li/a')
# print(dir(data_list))
# print(data_list)
# 需要遍历的节点列表中如果没有数据，提取指定节点的数据会发生异常，
for data in data_list:
    # print(dir(data))
    # 三元表达式
    a_text = data.xpath('./text()')[0] if len(data.xpath('./text()')) > 0 else None
    a_href = data.xpath('./@href')[0]
    print(a_text,a_href)



print(html)
print(type(html))
print(dir(html))
# 返回的是对象
print(html.xpath('//div/ul/li[1]/a'))
# 提取链接，返回的是列表
print(html.xpath('//div/ul/li[1]/a/@href'))
# 提取文本,返回的是列表
print('html',html.xpath('//div/ul/li[1]/a/text()'))
# 提取文本,返回的是文本内容
# print(html.xpath('//div/ul/li[1]/a/text()')[0])