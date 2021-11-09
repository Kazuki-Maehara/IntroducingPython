import requests
url = 'URL_TO_API'
sp = 30

resp = requests.get(url)
print(resp)
print('-' * sp)

print(resp.text)
