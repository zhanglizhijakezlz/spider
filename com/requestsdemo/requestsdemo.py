import requests

req = requests.get('https://github.com/favicon.ico')
print(req.text)
print(req.content)