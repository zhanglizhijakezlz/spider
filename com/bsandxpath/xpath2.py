html = """
    <div id='content'>
        <ul class='list'>
            <li class='one'>One</li>
            <li class='two'>Two</li>
            <li class='three'>Three</li>
            <li class='four four1 four2 four3'>Four</li>
            <div id='inner'>
                <a href='http://www.baidu.com'>百度一下</a>
                <p>第一段</p>
                <p>第2段</p>
                <p>第3段</p>
                <p>
                    第4段
                    <span>法大师傅大师傅</span>
                </p>
                <p>第5段</p>
                <p>第6段</p>
            </div>
        </ul>
    </div>
"""

from lxml.html import etree
obj= etree.HTML(html)

# print(obj.xpath('//ul/li[@class="one"]/text()')[0])
# all_li = obj.xpath('//ul/li')
# for li in all_li:
#     class_value = li.xpath('@class')[0]
#     text_value = li.xpath('text()')[0]
#     print(class_value, text_value)

# print(obj.xpath('//div[@id="inner"]//text()'))
# print(obj.xpath('//div[@id="inner"]/text()'))
print(obj.xpath('//ul/li[contains(@class, "four")]/text()'))