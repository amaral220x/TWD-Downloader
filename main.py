# Objetivo desse projeto é baixar todas as HQs de The Walking Dead

import requests
import bs4
import mediafire_dl
from alive_progress import alive_bar
import os


url = 'http://ndrangheta-br.blogspot.com/search/label/The%20Walking%20Dead'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os links
links = soup.find_all('a')
downloads = []
for link in links:
    #print(link.get('href'))
    link = link.get('href')
    if 'mediafire' in str(link):
        downloads.append(link)

if not os.path.exists('Downloads'):
    os.makedirs('Downloads')

print(f'Foram encontrados {len(downloads)} links de download')
edicao = 1
with alive_bar(len(downloads)) as bar:
    for download in downloads:
        output = f'Downloads/The Walking Dead - Edicao {edicao}.cbr'
        edicao += 1
        mediafire_dl.download(download,output, quiet=True)
        bar()

