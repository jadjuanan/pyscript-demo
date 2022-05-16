# python script running in HTML

from urllib import request
resp = request.urlopen('https://jadjuanan.pythonanywhere.com/on')

print(resp.code)
