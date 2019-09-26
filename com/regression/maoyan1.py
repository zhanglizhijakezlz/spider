import requests
import re
def get_one_page(url):
    header = {
    "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    }
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile(
    '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(pattern,html)
    print(items)
# 定义一个main函数 调用get_one_page 发送请求 打印结果
def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html)
    parse_one_page(html)
main()