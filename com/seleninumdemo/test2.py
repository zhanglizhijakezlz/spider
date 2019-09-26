from selenium import webdriver
chdriver='E:\软件\谷歌\chromedriver.exe'
# 创建浏览器对象
dr = webdriver.Chrome(executable_path=chdriver)
url = 'http://sh.58.com/'
# 构建浏览器对象

# 加载url对相应的响应
dr.get(url)

# 获取当前的url，窗口
print(dr.current_url)
print(dr.window_handles)
# 模拟点击房屋出租
el = dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

#点击房屋出租后，会打开新的标签页，需要传入新打开标签页的索引
dr.switch_to.window(dr.window_handles[-1])
print(dr.current_url)
print(dr.window_handles)

# # 定位所有title
node_list = dr.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li[1]/div[2]/h2/a')
for node in node_list:
    print(node.text, node.get_attribute('href'))