import requests
# resp = requests.get('http://www.neuedu.com')
# print(resp)
# # <Response [200]>
# # 也可以这么写
# response = requests.request("get", "http://www.neuedu.com")
# print(response)
# # <Response [200]>

import requests
url = 'http://www.baidu.com/'
r = requests.get(url)
print(r.text)
print(r.encoding)
print(r.content.decode())
print(r.headers)



kw = {'wd':'东软'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params=kw, headers = headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)
# 查看响应内容，response.content返回的字节流数据
print(response.content)

# 查看完整url地址
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)