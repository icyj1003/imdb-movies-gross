import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def get_info(url):
    page = ""
    while page == "":
        try: 
            page = requests.get(url)
            break
        except:
            print('Quá tải chờ 5s')
            time.sleep(5)
            continue

    soup = BeautifulSoup(page.content, 'html.parser')

    """title: Done
    """
    title = soup.find('h1', attrs={'data-testid': 'hero-title-block__title'}).text
    print(f"title: {title} ===============================================================")

    """Credits
    casts:
    directors:
    writers:
    """
   
    try:
        casts = ""
        directors = ""
        writers = ""
        credits = soup.find('div', role='presentation', class_='PrincipalCredits__PrincipalCreditsPanelWideScreen-hdn81t-0 iGxbgr')
        lines = credits.find_all('li', class_='ipc-metadata-list__item')
        for line in lines:
            if line.text.find('Star')!=-1:
                for item in line.find_all('a'):
                    casts = casts + item.text + ','
            if line.text.find('Director')!=-1:
                for item in line.find_all('a'):
                    directors = directors + item.text + ','
            if line.text.find('Writer')!=-1:
                for item in line.find_all('a'):
                    writers = writers + item.text + ','
    except AttributeError:
        casts = None
        directors = None
        writers = None
    print(f"casts: {casts}")
    print(f"directors: {directors}")
    print(f"writers: {writers}")


    """Storyline
    genres: Done
    certificate: Done
    """
    storyline = soup.find('section', attrs={'data-testid': 'Storyline'})

    # genres
    try:
        temp = storyline.find('li', attrs={'data-testid': 'storyline-genres'}).find_all('li', class_='ipc-inline-list__item')
        genres = ""
        for item in temp:
            genres = genres + item.text + ','
    except AttributeError:
        genres = None
    print(f"genres: {genres}")

    # certificate
    try:
        certificate = storyline.find('li', attrs={'data-testid': 'storyline-certificate'}).find('li', class_='ipc-inline-list__item').text
    except AttributeError:
        certificate = None
    print(f'certificate: {certificate}')
   
    """Details 
    release_date: Done
    countries_of_origin: Done
    languages: Done
    production_companies: Done
    """
    details = soup.find('section', attrs={'data-testid': 'Details'})

    # release_date
    try:
        release_date = details.find('li', attrs={'data-testid': 'title-details-releasedate'}).find('li', class_='ipc-inline-list__item').text
    except AttributeError:
        release_date = None
    print(f"release_date: {release_date}")

    # countries_of_origin
    try:
        temp = details.find('li', attrs={'data-testid': 'title-details-origin'}).find_all('li', class_='ipc-inline-list__item')
        countries_of_origin = ""
        for item in temp:
            countries_of_origin = countries_of_origin + item.text + ','

    except AttributeError:
        countries_of_origin = None
    print(f"countries_of_origin: {countries_of_origin}")

    # languages
    try:
        temp = details.find('li', attrs={'data-testid': 'title-details-languages'}).find_all('li', class_='ipc-inline-list__item')
        languages = ""
        for item in temp:
            languages = languages + item.text + ','
    except AttributeError:
        languages = None
    print(f"languages: {languages}")

    # production_companies:
    try:
        temp = details.find('li', attrs={'data-testid': 'title-details-companies'}).find_all('li', class_='ipc-inline-list__item')
        production_companies = ""
        for item in temp:
            production_companies = production_companies + item.text + ','
    except AttributeError:
        production_companies = None
    print(f"production_companies: {production_companies}")
    
    """Box office
    budget: Done
    gross_worldwide: Done
    """
    box_office = soup.find('section', attrs={'data-testid': 'BoxOffice'})

    # gross_worldwide
    try:
        gross_worldwide = box_office.find('li', attrs={'data-testid': 'title-boxoffice-cumulativeworldwidegross'}).find('span', class_='ipc-metadata-list-item__list-content-item').text
    except AttributeError:
        gross_worldwide = None
    print(f'gross_worldwide: {gross_worldwide}')

    # budget
    try:
        budget = box_office.find('li', attrs={'data-testid': 'title-boxoffice-budget'}).find('span', class_='ipc-metadata-list-item__list-content-item').text
    except AttributeError:
        budget = None
    print(f"budget: {budget}")

    """Technical specs
    runtime: Done
    color: Done
    sound_mix: Done
    aspect_ratio: Done
    """
    technical_specs = soup.find('section', attrs={'data-testid': 'TechSpecs'})

    # runtime
    try:
        runtime = technical_specs.find('li', attrs={'data-testid': 'title-techspec_runtime'}).find('span', class_='ipc-metadata-list-item__list-content-item').text
    except AttributeError:
        runtime = None
    print(f"runtime: {runtime}")

    # color
    try:
        color = technical_specs.find('li', attrs={'data-testid': 'title-techspec_color'}).find('li', class_='ipc-inline-list__item').text
    except AttributeError:
        color = None
    print(f"color: {color}")

    # sound_mix:
    try:
        temp = technical_specs.find('li', attrs={'data-testid': 'title-techspec_soundmix'}).find_all('li', class_='ipc-inline-list__item')
        sound_mix = ""
        for item in temp:
            sound_mix = sound_mix + item.text + ','
    except AttributeError:
        sound_mix = None
    print(f"sound_mix: {sound_mix}")

     # aspect_ratio
    try:
        aspect_ratio = technical_specs.find('li', attrs={'data-testid': 'title-techspec_aspectratio'}).find('li', class_='ipc-inline-list__item').text
    except AttributeError:
        aspect_ratio = None
    print(f"aspect_ratio: {aspect_ratio}")

    """
    votes: Done
    score: Done
    user_reviews: Done
    critical_reviews: Done
    metascore: Done
    """
    # score
    try:
        score = soup.find('div', attrs={"data-testid":'hero-rating-bar__aggregate-rating__score'}).text
    except AttributeError:
        score = None
    print(f"score: {score}")

    # votes
    try:
        votes = soup.find('div', class_='AggregateRatingButton__TotalRatingAmount-sc-1ll29m0-3 jkCVKJ').text
    except AttributeError:
        votes = None
    print(f"votes: {votes}")

    try:
        user_reviews = None
        critic_reviews = None
        metascore = None
        temp = soup.find('ul', attrs={"data-testid":'reviewContent-all-reviews'}).find_all('span', class_='score')
        for i in range(0, len(temp)):
            if i==0:
                user_reviews = temp[i].text
            elif i==1:
                critic_reviews = temp[i].text
            elif i==2:
                metascore = temp[i].text
    except AttributeError:
        user_reviews = None
        critic_reviews = None
        metascore = None
    print(f"user_reviews: {user_reviews}")
    print(f"critic_reviews: {critic_reviews}")
    print(f"metascore: {metascore}")
    return title, casts, directors, writers, genres, certificate, release_date, countries_of_origin, languages, production_companies, gross_worldwide, budget, runtime, color, sound_mix, aspect_ratio, score, votes, user_reviews, critic_reviews, metascore

start = time.time()

f = open('./collecting/links.txt', 'r')
links = f.read().split('\n')

print(f'Có {len(links)} trang\nĐảm bảo đường truyền internet và máy hoạt động trong thời gian thu thập dữ liệu\nThu thập từ trang thứ\nFile sẽ lưu dưới dạng [số trang].csv. Ví dụ: 1.csv')
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
        print(f"Phim thứ {count} trong số 250 phim của trang thứ {i + 1} trên tổng số {len(links)} trang, thực hiện đến trang thứ {e}")
        print(f"Đã thực hiện được {time.time() - start} giây")
        count+=1
        href = item.find('a').get('href')
        data.append(get_info("https://www.imdb.com"+ href))

    header = ['title', 'casts', 'directors', 'writers', 'genres', 'certificate', 'release_date', 'countries_of_origin', 'languages', 'production_companies', 'gross_worldwide', 'budget', 'runtime', 'color', 'sound_mix', 'aspect_ratio', 'score', 'votes', 'user_reviews', 'critic_reviews', 'metascore']
    df = pd.DataFrame(data=data)
    df.columns = header
    df.to_csv(f"./data/{i+1}.csv", index=False, encoding='utf-8-sig')


header = ['title', 'casts', 'directors', 'writers', 'genres', 'certificate', 'release_date', 'countries_of_origin', 'languages', 'production_companies', 'gross_worldwide', 'budget', 'runtime', 'color', 'sound_mix', 'aspect_ratio', 'score', 'votes', 'user_reviews', 'critic_reviews', 'metascore']

end = time.time()

print(f"Hoàn thành {e-s+1} trang hết {end-start} giây")