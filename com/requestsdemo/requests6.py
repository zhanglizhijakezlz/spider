import requests


# 使用代理
url = 'http://www.baidu.com/'

# 免费代理
proxies = {
    'http':'http://27.203.242.102:8060',
    'http':'http://175.18.58.51:8060'
}
# # 付费代理,用户名：密码@ip和port
# proxies = {
#     'http':'http://user:pwd@115.223.200.85:9000'
# }


response = requests.get(url,proxies=proxies)
print(response.text)