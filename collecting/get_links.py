import requests
from bs4 import BeautifulSoup

### add 
file_name = "links.txt"

f = open(file=file_name, mode='w')

i = 1
while i <= 500:
    if (i <= 9501):

        # Tao link
        url = f"/search/title/?title_type=feature&release_date=2010-01-01,2020-12-31&view=simple&count=250&start={i}"
        print(f'Từ {i} đến {i + 250 - 1}: {url}')
        f.write(url + '\n')

    else:
        
        # Tao link
        page = requests.get("https://www.imdb.com/" + url)
        soup = BeautifulSoup(page.content, "html.parser")
        url = soup.find('a', class_='lister-page-next next-page').get('href')
        print(f'Từ {i} đến {i + 250 - 1}: {url}')
        f.write(url + '\n')

    i = i + 250

f.close()