import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from imdb_crawler.funcs import get_info


start = time.time()

f = open('./data_crawling/links.txt', 'r')
links = f.read().split('\n')

print(
    f'Có {len(links)} trang\nĐảm bảo đường truyền internet và máy hoạt động trong thời gian thu thập dữ liệu\nThu thập từ trang thứ\nFile sẽ lưu dưới dạng [số trang].csv. Ví dụ: 1.csv')
s = int(input('Từ trang: '))
e = int(input('Đến trang: '))
for i in range(s - 1, e):
    data = []
    link = "https://www.imdb.com" + links[i]
    page = ""
    while page == "":
        try:
            page = requests.get(link)
            break
        except:
            print('Quá tải chờ 5s')
            time.sleep(5)
            continue
    content = BeautifulSoup(page.content, 'html.parser')
    content = content.find_all('div', class_='lister-item mode-simple')
    count = 1
    for item in content:
        print(
            f"Phim thứ {count} trong số 250 phim của trang thứ {i + 1} trên tổng số {len(links)} trang, thực hiện đến trang thứ {e}")
        print(f"Đã thực hiện được {time.time() - start} giây")
        count += 1
        href = item.find('a').get('href')
        data.append(get_info("https://www.imdb.com" + href))

    header = ['title', 'casts', 'directors', 'writers', 'genres', 'certificate', 'release_date', 'countries_of_origin', 'languages', 'production_companies',
              'gross_worldwide', 'budget', 'runtime', 'color', 'sound_mix', 'aspect_ratio', 'score', 'votes', 'user_reviews', 'critic_reviews', 'metascore']
    df = pd.DataFrame(data=data)
    df.columns = header
    df.to_csv(f"./data/{i+1}.csv", index=False, encoding='utf-8-sig')


header = ['title', 'casts', 'directors', 'writers', 'genres', 'certificate', 'release_date', 'countries_of_origin', 'languages', 'production_companies',
          'gross_worldwide', 'budget', 'runtime', 'color', 'sound_mix', 'aspect_ratio', 'score', 'votes', 'user_reviews', 'critic_reviews', 'metascore']

end = time.time()

print(f"Hoàn thành {e-s+1} trang hết {end-start} giây")
