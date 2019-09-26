from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
chdriver='E:\软件\谷歌\chromedriver.exe'
# 创建浏览器对象
driver = webdriver.Chrome(executable_path=chdriver)
driver.maximize_window()
driver.get("http://music.163.com/#/song?id=31877470")
driver.switch_to.frame("contentFrame")
time.sleep(5)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.save_screenshot('d:/gg.png')  # 截图
for i in range(80):
    b = driver.find_element_by_xpath("//a[starts-with(@class,'zbtn znxt')]")
    b.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@data-type='reply']")))
        print(driver.page_source)
    except NoSuchElementException:
        print('OMG')

    time.sleep(1)
driver.quit()