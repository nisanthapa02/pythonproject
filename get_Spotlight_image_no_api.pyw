import requests, bs4, os

r = requests.get('https://spotlight.it-notes.ru')
soup = bs4.BeautifulSoup(r.content, 'lxml')
article = soup.find('article')
nameTitle = article.find('span', recursive=False).get_text()
downloadUrl = article.find('img').get('src')
# print(nameTitle, downloadUrl)

os.makedirs(os.path.join('D:\\', 'spotlight Image'), exist_ok=True)

r = requests.get(downloadUrl)
with open(os.path.join('D:\\', 'spotlight Image', nameTitle + '.jpeg'), 'wb') as file:
    for chunk in r.iter_content(chunk_size=10000):
        file.write(chunk)

