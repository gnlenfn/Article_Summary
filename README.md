# 기사요약 웹앱 만들기
검색할 키워드를 선정하여 추가하면 해당 키워드로 검색하여 원하는 기사 수 만큼 스크래이핑 하여 요약한다.

### 1. 요약 알고리즘
- 원래 transformer를 이용하여 요약 모델을 만드려 했으나, 한국어 데이터의 부족으로 (레이블 구하는게 어렵다) gensim의 summarize method를 사용했다.
- gensim의 summarize는 TextRank 알고리즘을 이용하는 요약 방식으로 통계를 기반으로 따로 훈련 없이 문서요약이 가능하다고 한다.

### 2. 웹앱 구성
- Flask를 사용해 간단한 웹앱을 만들었고, 키워드추가 페이지와 article list 페이지 두 개가 있다.
- 그리고 AWS를 통해 배포를 진행했다. 하지만 배포는 2%부족한 느낌.. 더 알아볼 필요 있음
- gunicorn과 nginx를 사용했는데 gunicorn이 매끄럽게 되지 않는다. 오류메세지도 잘 모르겠음...

[웹앱 접속](http://13.209.102.180:5000/)

### 3. 추가할 기능
- [ ] 보여주는 기사의 최신화가 필요하다. --> 일정 시간 간격 혹은 매일 일정 시간에 새로 기사를 검색하도록 한다.
- [ ] db구성에서 개선점이 있을 수 있을 것 같은데 아직 잘 모르겠다. 공부가 더 필요

### 4. 보안 문제
- 현재 db 정보가 그대로 github에 올라가있다. 무료 클라우드고 누가 이거로 뭘 하겠냐 라는 생각으로 그냥 했지만 위험한 부분이다.
