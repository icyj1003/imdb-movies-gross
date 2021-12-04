import pandas as pd

# đọc bộ dữ liệu
df = pd.read_csv('./data/data_preprocessed.csv')

# sắp xếp lại các cột

print(df.columns)

df = df[['casts', 'directors', 'writers', 'genres',
         'certificate', 'countries_of_origin', 'languages', 'production_companies', 'sound_mix', 'aspect_ratio', 'budget', 'runtime', 'release_date']]

print(df.columns)

df.to_csv('./data/data_model.csv', index=False, encoding='utf-8-sig')
