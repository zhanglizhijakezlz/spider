from selenium import webdriver
chdriver='E:\软件\谷歌\chromedriver.exe'
# 创建浏览器对象
dr = webdriver.Chrome(executable_path=chdriver)

# 发送请求
dr.get('http://www.baidu.com/')

# 获取查看源码,不是network中的源码
#print(dr.page_source)
# 获取cookie信息
print(dr.get_cookies()) # 输出cookie信息列表信息
# 获取title
print(dr.title) # 百度一下，你就知道
# 关闭浏览器
# 关闭当前浏览器
dr.close()

