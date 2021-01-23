import requests

r = requests.get('https://jsonapiplayground.reyesoft.com/v2/authors')

print(r.status_code)
print(r.headers['content-type'])

#print(r.json())

authors = r.json()

#print(authors['data'][0])

for author in authors['data']:
    attributes = author['attributes']
    print(attributes['name'], attributes['birthplace'])

    