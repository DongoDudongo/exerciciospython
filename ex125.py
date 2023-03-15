import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com/')
except urllib.error.URLError:
    print('o site não está acessivel no momento')
else:
    print('O site está acessivel')
