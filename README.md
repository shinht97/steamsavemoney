# 🎮 게임 리뷰 기반 추천 시스템

**SteamSaveMoney**는 자연어 처리(NLP)와 TF-IDF 분석을 활용하여 사용자가 선택한 게임과 유사한 리뷰를 가진 다른 게임을 추천하는 데스크탑 애플리케이션입니다. 이 프로그램은 게임 리뷰 데이터를 분석하여 유사한 감성을 가진 게임을 찾아줍니다.

---

## 🧩 주요 기능

- **리뷰 기반 게임 추천**: 선택한 게임의 리뷰와 유사한 리뷰를 가진 게임을 추천합니다.
- **키워드 및 장르 기반 추천**: 특정 키워드와 장르를 조합하여 게임을 추천합니다.
- **직관적인 GUI 제공**: PyQt를 사용하여 사용자 친화적인 인터페이스를 제공합니다.

---

## 🖼️ 인터페이스 예시

![게임 선택 화면](https://github.com/shinht97/steamsavemoney/assets/71716980/f968c857-09be-42eb-8f2b-cef3cf60abae)
*게임을 지정하여 유사한 댓글이 있는 게임 추천*

![키워드 및 장르 선택 화면](https://github.com/shinht97/steamsavemoney/assets/71716980/4b7b0dcb-5184-4a13-b216-c5163fe5f53a)
*특정 키워드와 장르를 이용한 게임 추천*

---

## 🗂️ 프로젝트 구조

```
steamsavemoney/
├── crawled_data/                 # 크롤링된 원시 데이터
├── models/                       # 학습된 모델 파일
├── source_code/                  # 주요 소스 코드
├── cleaned_review.csv            # 전처리된 리뷰 데이터
├── games_with_review_and_genre.csv # 게임, 리뷰, 장르 정보
├── steam.csv                     # Steam 게임 데이터
├── steampp_app.py                # 메인 애플리케이션 실행 파일
├── steampp.ui                    # PyQt UI 파일
├── dialog.ui                     # 추가 UI 구성 파일
├── requirements.txt              # 필요한 패키지 목록
├── README.md                     # 프로젝트 설명 파일
```

---

## ⚙️ 설치 및 실행 방법

1. **필수 패키지 설치**

   ```bash
   pip install -r requirements.txt
   ```

2. **애플리케이션 실행**

   ```bash
   python steampp_app.py
   ```

---

## 🛠 사용 기술

- **언어**: Python
- **라이브러리**: PyQt, scikit-learn, pandas, numpy 등
- **모델**: TF-IDF 기반 유사도 분석 모델

---

## 📄 참고 자료

- [requirements.txt](https://github.com/shinht97/steamsavemoney/blob/main/requirements.txt): 필요한 패키지 목록
- [cleaned_review.csv](https://github.com/shinht97/steamsavemoney/blob/main/cleaned_review.csv): 전처리된 리뷰 데이터

---

## 📅 프로젝트 진행 기간

**2025년 2월 12일 ~ 2025년 2월 22일**

---

프로젝트에 대한 자세한 내용은 [GitHub 리포지토리](https://github.com/shinht97/steamsavemoney)를 참고하시기 바랍니다.

<!-- # 자연어 처리를 이용한 게임 추천 프로그램

자연어 처리 모델과 TFIDF 분석을 이용하여 지정한 게임의 리뷰와 비슷한 리뷰가 있는 게임을 추천하는 프로그램 제작

===================================================================

### 리뷰 분석을 이용한 어플리케이션

![image](https://github.com/shinht97/steamsavemoney/assets/71716980/f968c857-09be-42eb-8f2b-cef3cf60abae)
<게임을 지정하여 유사한 댓글이 있는 게임 추천>  

![image](https://github.com/shinht97/steamsavemoney/assets/71716980/4b7b0dcb-5184-4a13-b216-c5163fe5f53a)
<특정 키워드와 장르를 이용한 게임 추천>  -->
