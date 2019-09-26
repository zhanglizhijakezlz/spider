import requests
import re
import json
# 请求页面
def get_one_page(url):
    header = {
    "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    }
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        return response.text
    return None

#解析页面
def parse_one_page(html):# html为网页源码
    pattern = re.compile(
    '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )#定义规则
    items = re.findall(pattern,html)#查找整个页面
    # print(items)
    #遍历结果生成字典
    for item in items:
        yield {
        'index':item[0],
        'image': item[1],
        'title': item[2].strip(),
        'actor': item[3].strip()[3:] if len(item[3]) > 3 else'',
        'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
        'score': item[5].strip()+item[6].strip()
        }
        #返回一个生成器 yield

#写入文件
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


# 定义一个main函数 调用get_one_page 发送请求 打印结果
def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):#遍历生成器
        write_to_file(item)
main()

# def main(offset):
#     url = 'http://maoyan.com/board/4?offset=' + str(offset)
#     html = get_one_page(url)
#     # print(html)
#     for item in parse_one_page(html):#遍历生成器
#         write_to_file(item)
#
# if __name__ == '__main__':
#     for i in range(10):
#         main(offset = i *10)