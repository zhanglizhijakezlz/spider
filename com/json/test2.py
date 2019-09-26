import requests
import json

# 目标：
# 爬取豆瓣网电视信息
# 1、电视名称、封面信息、评分等

class Douban(object):

    def __init__(self):
        self.url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        # 创建文件对象
        self.file = open('douban.json','w',encoding='utf8')

    # 发送请求，获取数据
    def get_data(self):
        response = requests.get(url=self.url,headers=self.headers)
        # 把响应数据转成str类型
        return response.content.decode()

    # 解析数据
    def parse_data(self,data):
        print(data)
        # 把电视数据转成字典
        dict_data = json.loads(data)
        # print(dict_data)
        result_list = dict_data['subjects']
        data_list = []
        # 获取电视列表数据
        for result in result_list:
            temp = {}
            temp['title'] = result['title']
            temp['rate'] = result['rate']
            temp['url'] = result['url']
            data_list.append(temp)
        # 返回数据列表
        return data_list

    # 保存电视数据
    def save_data(self,data_list):
        # 遍历列表
        for data in data_list:
            str_data = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(str_data)

    # 关闭文件对象
    def __del__(self):
        self.file.close()

    def run(self):
        # 1、构建请求头和url
        # 2、发送请求，获取数据
        data = self.get_data()
        # 3、解析数据
        data_list = self.parse_data(data)
        # 4、保存文件
        self.save_data(data_list)


if __name__ == '__main__':
    douban = Douban()
    douban.run()