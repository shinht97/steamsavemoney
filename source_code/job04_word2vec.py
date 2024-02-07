import pandas as pd

from gensim.models import Word2Vec

df_reviews = pd.read_csv("../games_with_review_and_genre.csv")

reviews = list(df_reviews["reviews"])
print(reviews[0])

tokens = []

for sentence in reviews:
    token = sentence.split()
    tokens.append(token)

embedding_model = Word2Vec(tokens, vector_size=100, window=4,
                           min_count=20, workers=4, epochs=100, sg=1)

embedding_model.save("../models/word2vec_reviews.model")

print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))
