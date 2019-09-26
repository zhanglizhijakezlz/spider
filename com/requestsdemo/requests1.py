import requests

response = requests.get('http://www.baidu.com')
print(response.status_code)  # 打印状态码
print(response.url)          # 打印请求url
print(response.headers)      # 打印头信息
print(response.cookies)      # 打印cookie信息
print(response.text)  #以文本形式打印网页源码
print(response.content) #以字节流形式打印



response = requests.get('http://httpbin.org/get')
print(response.text)
print(response.json())  #response.json()方法同json.loads(response.text)
print(type(response.json()))



data = {
    'name': 'tom',
    'age': 20
}

response = requests.get('http://httpbin.org/get', params=data)
print(response.text)


response = requests.get('http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-002.jpg')
b = response.content
with open('a.jpg','wb') as f:
    f.write(b)