import pandas as pd
import glob
from konlpy.tag import Okt

game_df = pd.read_csv("../steam.csv")

full_df = pd.DataFrame()

# files = glob.glob("../review_data*.csv")
#
# for file in files:
#     temp_df = pd.read_csv(file)
#     full_df = pd.concat([full_df, temp_df], ignore_index=True)

df_0 = pd.read_csv("../review_data_0.csv")

full_df = pd.concat([full_df, df_0], ignore_index=True)

df_30 = pd.read_csv("../review_data_0.csv")

full_df = pd.concat([full_df, df_30], ignore_index=True)

df_60 = pd.read_csv("../review_data_0.csv")

full_df = pd.concat([full_df, df_60], ignore_index=True)

df_90 = pd.read_csv("../review_data_0.csv")

full_df = pd.concat([full_df, df_90], ignore_index=True)

df_334 = pd.read_csv("../review_data_334_667.csv")

df_temp1 = pd.DataFrame({"titles" : list(game_df["titles"][335:667]), "reviews" : list(df_334["reviews"])})

full_df = pd.concat([full_df, df_temp1], ignore_index=True)

df_667 = pd.read_csv("../review_data_667_1001.csv")

df_temp2 = pd.DataFrame({"titles" : list(game_df["titles"][667:1001]), "reviews" : list(df_667["reviews"])})

full_df = pd.concat([full_df, df_temp2], ignore_index=True)

full_df.drop_duplicates(ignore_index=True, inplace=True)

full_df.dropna(inplace=True)

stop_df = pd.read_csv("../stopwords.csv")

stopwords = list(stop_df["stopword"])

stopwords += ["게시일", "월", "일"]

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
