import pandas as pd
import glob


review_df = pd.read_csv("../cleaned_review.csv")

genre_path = glob.glob("../genre_*")

genre_df = pd.DataFrame()

for file in genre_path:
    temp_df = pd.read_csv(file)
    genre_df = pd.concat([genre_df, temp_df], ignore_index=True)

print(genre_df.head())
print(len(genre_df))
print(len(review_df))

concated_df = pd.merge(review_df, genre_df, how="inner", left_on="titles", right_on="titles")
# cleaned_review에 있는 게임만 장르를 적용

print(concated_df.head())
concated_df.info()

concated_df.to_csv("../games_with_review_and_genre.csv", index=False)

