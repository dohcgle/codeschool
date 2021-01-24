import requests
from pprint import pprint
# r = requests.get('https://randomuser.me/api/')
# # pprint(dict(r.headers))
# pprint(r.headers['Content-Type'])

try:
    print(int('as'))
except ValueError:
    print('Error')