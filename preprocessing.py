import pandas as pd
from imdb.cleaning import *

# đọc bộ dữ liệu thô
df = pd.read_csv('./data/data.csv')

# drop bỏ các phim bị khuyết doanh thu
df.dropna(subset=['gross_worldwide'], inplace=True)

# drop các phim trùng lặp
df.drop_duplicates(inplace=True)

# apply các hàm xử lý
df['gross_worldwide'] = df['gross_worldwide'].apply(currency_conv)
df['budget'] = df['budget'].apply(currency_conv)
df['certificate'] = df['certificate'].apply(certification_conv)
df['score'] = df['score'].apply(pp_score)
df['votes'] = df['votes'].apply(pp_vote)
df['user_reviews'] = df['user_reviews'].apply(pp_review)
df['critic_reviews'] = df['critic_reviews'].apply(pp_review)
df['runtime'] = df['runtime'].apply(to_minutes)
df['release_date'] = df['release_date'].apply(get_year)
df['color'] = df['color'].apply(pp_color)
df['casts'] = df['casts'].apply(pp_cast)
df['writers'] = df['writers'].apply(pp_writer)
df['aspect_ratio'] = df['aspect_ratio'].apply(pp_ar)

# lưu bộ dữ liệu
df.to_csv('./data/data_preprocessed.csv', index=False, encoding='utf-8-sig')
