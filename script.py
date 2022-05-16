# python script running in HTML

print('hello world from python')

from urllib import request
resp = request.urlopen('https://jadjuanan.pythonanywhere.com/on')

print(resp.code)
