import requests

url = 'YOUR DOMAIN'

image = '001.jpg'
data = open(image, 'rb')
file = {'file': data}

res = requests.post(url, files=file)
print(res.json())