# 异常处理
#
# 在你不确定会发生什么错误时，尽量使用try...except来捕获异常
#
# 所有的requests exception：
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

try:
    response = requests.get('http://www.baidu.com',timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('timeout')
except HTTPError:
    print('httperror')
except RequestException:
    print('reqerror')