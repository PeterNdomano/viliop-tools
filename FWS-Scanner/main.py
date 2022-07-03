# importing sys
import sys

#adding python_modules folder to path
sys.path.insert(0, '../python_modules')

import requests
r = requests.get('http://google.com')
print(r.headers)
