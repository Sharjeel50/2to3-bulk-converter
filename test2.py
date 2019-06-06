import urllib.request, urllib.error, urllib.parse

try:
    x = urllib.request.urlopen("dsadsa").read()
    print(x)
except Exception as e:
    print(str(e))
