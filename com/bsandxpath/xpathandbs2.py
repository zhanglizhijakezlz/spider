from bs4 import BeautifulSoup
from lxml import etree
import requests

# 这是网页源码提取的部分
'''
<li>
<div class="il_img"><a href="/tupian/makelong_v47314/" title="美味的马卡龙图片" target="_blank">
<img src="http://img.ivsky.com/img/tupian/li/201803/13/macaroon-001.jpg" alt="美味的马卡龙图片"></a></div>
<p><a href="/tupian/makelong_v47314/" target="_blank">美味的马卡龙图片(12张)</a></p>
</li>

'''


class TianTangSpider(object):
    def get_code(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get('http://www.ivsky.com/tupian/meishishijie/', headers=headers).text
        return response

    def use_xpath(self, code):
        code = etree.HTML(code)
        # 因为a标签下面嵌套着img标签，这里只获取a标签的href 属性
        href = code.xpath('//div[@class="il_img"]/a')
        for i in href:
            print(i.get('href'))

        image_list = code.xpath('//div[@class="il_img"]/a/img')
        for name in image_list:
            src = name.get('src')
            alt = name.get('alt')

    def use_soup(self, code):
        soup = BeautifulSoup(code, 'lxml')
        image_list = soup.select('div.il_img img')
        for name in image_list:
            src = name.get('src')
            alt = name.get('alt')
            print(src,alt)

    def func_manager(self):
        code = self.get_code()
        self.use_xpath(code)
        self.use_soup(code)


tian = TianTangSpider()
tian.func_manager()