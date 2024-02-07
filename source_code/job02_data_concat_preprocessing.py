import pandas as pd
import glob
from konlpy.tag import Okt

game_df = pd.read_csv("../steam.csv")

game_df.reset_index(inplace=True)

files = glob.glob("../crawled_data/review_data*.csv")  # 지정한 형식과 같은 모든 파일의 경로를 리스트로 만듬

full_df = pd.DataFrame()

for file in files:
    if file.count("_") != 3:  # 파일 형식에 따라 '_'가 세개가 안되는 경우
        temp_df = pd.read_csv(file)
        full_df = pd.concat([full_df, temp_df], ignore_index=True)


# review_data_334_667, 667_1001의 경우 게임 타이틀이 안 들어가 있음, 이를 위해 분리 하여 다시 만듬
df_334 = pd.read_csv("../review_data_334_667.csv")

df_334.reset_index(inplace=True)

print(len(game_df["titles"][334:665]))
print(len(df_334["reviews"]))

df_temp1 = pd.DataFrame({"titles": list(game_df["titles"][334:665]), "reviews": list(df_334["reviews"])})

full_df = pd.concat([full_df, df_temp1], ignore_index=True)

df_667 = pd.read_csv("../review_data_667_1001.csv")

df_667.reset_index(inplace=True)

print(len(game_df["titles"][665:]))
print(len(df_667["reviews"]))

df_temp2 = pd.DataFrame({"titles" : list(game_df["titles"][665:]), "reviews" : list(df_667["reviews"])})

full_df = pd.concat([full_df, df_temp2], ignore_index=True)

full_df.drop_duplicates(ignore_index=True, inplace=True)

full_df.dropna(inplace=True)

stop_df = pd.read_csv("../stopwords.csv")

stopwords = list(stop_df["stopword"])

stopwords += ["게시일", "월", "일", "게시", "액세스", "조기"]

cleaned_sentences = []

okt = Okt()

for idx, review in enumerate(full_df["reviews"]):
    print(f"\r{idx/len(full_df)}", end="")

    tokened_review = okt.pos(review, stem=True)

    df_token = pd.DataFrame(tokened_review, columns=["word", "class"])
    df_token = df_token[df_token["class"].isin(["Noun", "Adjective", "Verb"])]

    words = []

    for word in df_token["word"]:
        if len(word) > 1:
            if word not in stopwords:
                words.append(word)

    cleaned_sentence = " ".join(words)

    cleaned_sentences.append(cleaned_sentence)

save_df = pd.DataFrame({"titles" : full_df["titles"], "reviews" : cleaned_sentences})

save_df.to_csv("../cleaned_review.csv", index=False)

save_df = pd.read_csv("../cleaned_review.csv")

save_df.dropna(inplace=True)

save_df.to_csv("../cleaned_review.csv", index=False)
