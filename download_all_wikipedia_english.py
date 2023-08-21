import requests

url = 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2'
response = requests.get(url, stream=True)

with open('enwiki-latest-pages-articles.xml.bz2', 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
