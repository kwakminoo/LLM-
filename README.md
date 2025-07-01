# LLM-

# 🧠 LLM 학습 커리큘럼 (입문자용)

## 🎯 전체 목표
- 1단계: 기초 개발자 되기 (프로그래밍 + 컴퓨터 기초)
- 2단계: AI와 딥러닝 이해 + LLM 작동 원리 습득
- 3단계: LLM 실습 + 모델 직접 사용하기

---

## 📘 1단계: 기초 다지기 — 컴퓨터와 AI의 기초 이해

### ✅ 목표
- 컴퓨터와 프로그래밍의 기본 개념 이해
- Python 언어의 기초 습득
- AI와 머신러닝의 큰 그림 파악

### 📚 추천 학습 자료
- [CS50 (하버드 무료 강의)](https://cs50.harvard.edu/x/) — 컴퓨터 과학 기초
- Python 입문
  - [점프 투 파이썬](https://wikidocs.net/book/1) (한국어 무료)
  - [파이썬 프로그래밍 기초 by 생활코딩](https://opentutorials.org/course/1750)
- AI 개념 이해
  - [생활코딩 - 머신러닝 (영상)](https://www.youtube.com/watch?v=Sm3Ry4j9mTo)
  - 유튜브에서 "머신러닝 개념" 검색 (한글 자료도 많음)

---

## 📗 2단계: LLM 작동 원리 이해하기 — NLP & 딥러닝 기본기

### ✅ 목표
- 자연어 처리(NLP)의 기초 이해
- 신경망, 딥러닝 기본 원리 습득
- Transformer 구조 개념 이해

### 📚 추천 학습 자료
- [Machine Learning by Andrew Ng (Coursera)](https://www.coursera.org/learn/machine-learning) - 한국어 자막 있음
- FastCampus - 딥러닝 올인원 패키지 (학생 할인 가능)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- NLP 기초
  - [HuggingFace NLP 과정](https://huggingface.co/learn/nlp-course)

---

## 📙 3단계: 실전 LLM — 직접 써보고, 만들어보기

### ✅ 목표
- Hugging Face로 사전 학습된 LLM 모델 활용
- 간단한 챗봇, 문서 요약, 감정 분석 등 실습
- LLM 파인튜닝(간단한 미세조정) 경험

### 🛠️ 실습 추천
- Google Colab 활용 (무료 GPU 지원)
- HuggingFace 모델 사용 실습: `transformers` 라이브러리
- LLM 프로젝트 예제 따라하기
  - 간단한 챗봇 만들기
  - 텍스트 분류기 만들기
  - 문장 요약기 만들기

### 📚 추천 자료
- [Hugging Face 튜토리얼](https://huggingface.co/docs/transformers/index)
- GitHub: `awesome-llm`, `awesome-transformers` 자료 모음
- [모두의 딥러닝](https://github.com/hunkim/DeepLearningZeroToAll) 시리즈

---

## 🧱 1단계: 컴퓨터 & Python 기초 (4~5주)

| 주차 | 목표 | 학습 내용 | 추천 자료 |
|------|------|-----------|------------|
| 1주차 | 컴퓨터 작동 원리 이해 | 컴퓨터 구조, 메모리, 코드 실행 개념 | CS50 강의 0~1주차 |
| 2주차 | Python 설치 + 기본 문법 | 변수, 자료형, 조건문, 반복문 | 점프 투 파이썬, 생활코딩 |
| 3주차 | 함수와 리스트/딕셔너리 | 함수, 리스트, 딕셔너리, 예외 처리 | 위 자료 계속 |
| 4주차 | 파일 입출력 & 프로젝트 | 간단한 텍스트 파일 읽기/쓰기, 미니 프로젝트 (예: 계산기) | 직접 코딩 |
| 5주차 | GitHub & 개발 툴 사용 | VSCode 설치, GitHub 사용법, 코드 업로드 | GitHub Docs, 유튜브 ‘기초 Git’ |

> 🎯 목표: Python으로 간단한 프로그램을 작성할 수 있다

---

## 🧠 2단계: AI/딥러닝 기초 + LLM 구조 이해 (6주)

| 주차 | 목표 | 학습 내용 | 추천 자료 |
|------|------|-----------|------------|
| 6주차 | 머신러닝 개념 | 지도학습 vs 비지도학습, 회귀/분류 개념 | 생활코딩 머신러닝 |
| 7주차 | 딥러닝 개념 이해 | 퍼셉트론, 다층 퍼셉트론, 역전파 개념 | 모두의 딥러닝 |
| 8주차 | Python으로 딥러닝 기초 코드 작성 | Numpy & Pandas로 행렬 다루기, 간단한 뉴럴넷 구현 | Numpy 공식문서, 유튜브 |
| 9주차 | NLP 기초 | 토큰화, 어휘 임베딩, 문장 벡터 | HuggingFace NLP 과정 |
| 10주차 | Transformer 이해 | Self-Attention, 인코더/디코더 구조 | The Illustrated Transformer |
| 11주차 | LLM 개요 이해 | GPT 구조, Pretraining vs Fine-tuning | 블로그, HuggingFace 문서 |

> 🎯 목표: LLM이 어떤 방식으로 작동하는지 이론적으로 설명 가능

---

## 🚀 3단계: LLM 실습 & 프로젝트 (6주 이상)

| 주차 | 목표 | 학습 내용 | 실습 자료 |
|------|------|-----------|------------|
| 12주차 | HuggingFace 사용법 익히기 | Transformers 라이브러리 설치, Colab 사용법 | HuggingFace 튜토리얼 |
| 13주차 | 사전 학습 모델 실행 | GPT2 불러와서 텍스트 생성해보기 | `transformers` 라이브러리 실습 |
| 14주차 | 감정 분석 모델 만들기 | IMDb 영화 리뷰로 감정 분석 | `pipeline('sentiment-analysis')` |
| 15주차 | 문서 요약 실습 | 뉴스 기사 요약, 요약 정확도 테스트 | `pipeline('summarization')` |
| 16주차 | 나만의 챗봇 만들기 | 간단한 대화 모델 만들기 | GPT2 + Streamlit |
| 17주차~ | LLM 파인튜닝 | 작은 데이터로 GPT 모델 미세 조정 | Google Colab + HuggingFace datasets |

> 🎯 목표: LLM을 직접 실행/응용할 수 있으며, 간단한 프로젝트를 만들 수 있다

---

## 🧩 선택 확장: 이후에 할 수 있는 것들

- LLM 모델 비교/분석: GPT, LLaMA, Claude 등 비교
- 오픈소스 참여: HuggingFace의 이슈 기여
- 미니 논문 읽기: [arXiv-sanity](https://www.arxiv-sanity.com/)
- ChatGPT Plugin, LangChain, RAG, Agents 공부

---

## 📌 도움 요청

이 커리큘럼을 기반으로 한 주간 계획표, 실습 가이드, 개인 프로젝트 지도 등이 필요하면 언제든지 요청하세요! 💡
