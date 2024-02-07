import pandas as pd #데이터프레임을 위한
import matplotlib.pyplot as plt  #시각화를 위한
from gensim.models import Word2Vec #모델을 사용하기 위한
from sklearn.manifold import TSNE #고차원 임베딩 벡터
from matplotlib import font_manager, rc #폰트 설정을 위한 라이브러리
import matplotlib as mpl

font_path = '../malgun.ttf' #한글 폰트 파일의 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 파일에서 가죠오는 폰트 이름
mpl.rcParams['axes.unicode_minus'] = False
# 마이너스 기호를 표시할 때 유니코드에서 마이너스 기호를 올바르게 표시하기 위한 설정
rc('font', family = font_name)
# 폰트 설정을 변경하여 한글 폰트를 사용하도록 설정

# 키워드 받기-------------------------------------------------------------

embedding_model = Word2Vec.load('../models/word2vec_reviews.model')
# 훈련된 Wor2vec모델 로드
key_word = input('키워드 입력')  # 분석할 키워드
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
# 모델을 사용하여 키워드와 가장 유사한 단어 10개를 추출
print(sim_word)

vectors = [] # 임베딩 벡터를 저장할 빈 리스트를 생성
labels = [] # 단어 라벨을 저장할 빈 리스트를 생성

for label, _ in sim_word:
    # 추출한 유사 단어 리스트에서 단어와 유사도를 순회하면서
    labels.append(label)  # 단어를 labels 리스트에 추가
    vectors.append(embedding_model.wv[label])
# 해당 단어의 임베딩 벡터를 vectors 리스트에 추가
print(vectors[0])
print(len(vectors[0]))

df_vectors = pd.DataFrame(vectors)
# vectors 리스트를 데이터프레임으로 변환
print(df_vectors.head())

tsne_model = TSNE(perplexity=9, n_components=2,init='pca',n_iter=2500)
# TSNE 모델을 초기화
new_value = tsne_model.fit_transform(df_vectors)
# 데이터프레임을 사용하여 임베딩 벡터를 2차원으로 축소
df_xy = pd.DataFrame({'words': labels, 'x': new_value[:, 0], 'y': new_value[:, 1]})
# 축소된 2차원 벡터와 단어 라벨을 포함하는 데이터프레임을 생성
df_xy.loc[df_xy.shape[0]] = (key_word, 0, 0)
# 데이터프레임의 마지막 행에 키워드와 위치를 (0,0)

print(df_xy)
print(df_xy.shape)

plt.figure(figsize=(8, 8))
# 그래프의 크기를 설정
plt.scatter(0, 0, s=1500, marker='*')
# 키워드 위치에 별표()를 표시합니다.

# 단어와 그에 해당하는 위치를 이어주는 선을 그립니다-------------------------------
for i in range(len(df_xy)):
    # 데이터프레임의 행 수만큼 반복하면서
    a = df_xy.loc[[i, 10]]
# 현재 단어와 키워드의 위치를 포함하는 데이터프레임을 생성
    plt.plot(a.x, a.y, '-D', linewidth = 1)
# 단어와 키워드의 위치를 연결하는 선을 그립니다.
    plt.annotate(df_xy.words[i], xytext=(1,1), xy=(df_xy.x[i], df_xy.y[i]),
                 textcoords = 'offset points', ha ='right', va = 'bottom')
# 단어 라벨을 표시합니다.
    plt.show() # 그래프를 화면에 출력
# ---------------------------------------------------------------------------



