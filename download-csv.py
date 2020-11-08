import requests


print('Beginning file download with requests')

url = input('Enter url: ')
path = input('Enter path after download: ')
fileName = input('Enter filename: ')

r = requests.get(url)

with open(f'{path}/{fileName}', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print('Downloading done')
