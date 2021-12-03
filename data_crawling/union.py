import os
import pandas as pd

parts = []
dir = os.listdir(path='./data')

for file in dir:
    parts.append(file.replace('.csv', ''))

missings = []

for i in range(1, 459):
    if str(i) not in parts:
        missings.append(i)

if len(missings) != 0:
    print('Các trang còn thiếu: ')
    for item in missings:
        print(item)
else:
    print('Đã đủ file, bắt đầu hợp nhất!')
    header = ['title', 'casts', 'directors', 'writers', 'genres', 'certificate', 'release_date', 'countries_of_origin', 'languages', 'production_companies',
              'gross_worldwide', 'budget', 'runtime', 'color', 'sound_mix', 'aspect_ratio', 'score', 'votes', 'user_reviews', 'critic_reviews', 'metascore']
    df = pd.DataFrame()
    count = 0
    for file in dir:
        part = pd.read_csv(f'./data/{file}')
        df = pd.concat([df, part], ignore_index=True)
        count = count + 1
        print(f"Đã hợp nhất {count} files!")
    print(df.shape)
    df.to_csv('./data/data.csv', index=False, encoding='utf-8-sig')
    print('Đã hoàn tất!')
