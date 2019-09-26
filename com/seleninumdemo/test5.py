from selenium import webdriver

chdriver='E:\软件\谷歌\chromedriver.exe'
# 创建浏览器对象

browser = webdriver.Chrome(executable_path=chdriver)

browser.get('http://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li a')
print(lis)
for ele in lis:
    print(ele.text)
    print(ele.get_attribute('href'))
browser.close()