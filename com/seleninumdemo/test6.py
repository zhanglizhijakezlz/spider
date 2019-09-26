from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait#引入 WebDriverWait对象

chdriver='E:\软件\谷歌\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=chdriver)
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser,10)
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))#调用until方法 节点出现
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))#调用until方法 按钮可点击
# print(input,button)

# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')