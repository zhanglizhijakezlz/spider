import re
from bs4 import BeautifulSoup
from lxml import etree
import requests


class SpiderCompare(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    def get_code(self):
        response = requests.get('https://tieba.baidu.com/p/5743456239?pn=1', headers=self.headers).text
        return response

    def use_re(self, code):
        pattern = re.compile(r'<li class="d_name".*?<a.*?>(.*?)</a>'
                             r'.*?<cc.*?class="d_post_content j_d_post_content ">(.*?)</div>', re.S)
        result = re.findall(pattern, code)
        pattern = re.compile(r'<.*?>|<br>|</a>', re.S)
        for name, content in result:
            new_name = re.sub(pattern, '', name)
            new_name = pattern.sub('', name)
            # 两种写法
            new_content = re.sub(pattern, '', content)
            print(new_content)

    def use_xpath(self, code):
        new_code = etree.HTML(code)
        name = new_code.xpath('//li[@class="d_name"]/a/text()')
        for new in name:
            print(new.replace(' ', '').strip('\n'))
        content = new_code.xpath('//cc/div[@class="d_post_content j_d_post_content "]//text()')
        for new in content:
            print(new)

    def use_soup(self, code):
        soup = BeautifulSoup(code, 'lxml')
        name = soup.select('li.d_name a')
        for new in name:
            print(new.get_text())

        content = soup.select('cc div')
        for new in content:
            print(new.get_text())


    def manager_spider(self):
        code = self.get_code()
        #正则不出来结果
        # self.use_re(code)
        # self.use_xpath(code)
        self.use_soup(code)


spider = SpiderCompare()
spider.manager_spider()