import pandas as pd

# đọc bộ dữ liệu
df = pd.read_csv('./data/data_preprocessed.csv')

# sắp xếp lại các cột

print(df.columns)

df = df[['genres', 'countries_of_origin', 'languages',
         'runtime', 'release_date']]

df = pd.get_dummies(df, prefix=['genres',
                                'certificate', 'countries_of_origin', 'languages', 'production_companies', 'sound_mix', 'aspect_ratio'])

print(len(df.columns))

df.to_csv('./data/data_model.csv', index=False, encoding='utf-8-sig')
