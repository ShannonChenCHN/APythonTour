


import requests


r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
status_code = r.status_code
header = r.headers['Content-Type']