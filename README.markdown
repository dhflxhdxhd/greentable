# 캡스톤/웹 프로젝트/그린테이블

<br>

## 간단 요약

---

👉🏻 [채식정보 웹 '그린테이블' 제안서 바로가기](https://docs.google.com/presentation/d/1TPNJSB8-3Ak64CxPvIKdvKU_JNcsfb-O6WOrEDMULyk/edit?usp=sharing)

프로젝트명 : **그린테이블🌿**

형식 : 웹 기반 비거니즘 정보 제공 서비스

목적 

다양한 이유로 늘어나는 채식 인구를 위한 장소와 관련한 정보를 새로운 방식으로 제공할 수 있도록 한다.

주 기능 

- 테스트 페이지를 더해 자신의 위치를 기준으로 한 맞춤형 비건 장소 정보 제공.
- 비건 관련 구매 웹 사이트 정보 제공

기대효과

- MZ 세대를 중심으로 채식에 관심을 가지는 사람들이 채식 문화를 보다 쉽게 경험할 수 있는 환경을 제공할 수 있을 것이다.
- 비거니즘에 대한 인식이 확대되어 비거니즘 전용 장소의 정보를 제공하지 않은 환경이 형성될 수 있다.

<br>

## 기능

---

### 전체 흐름

- 시작) 테스트 페이지 버튼과 웹사이트 정보 제공 페이지 버튼으로 나뉜다

    🥑 ***테스트 페이지 (주 기능)***

    - 테스트 시작 버튼을 누르면 테스트로 넘어간다.
        - 테스트 구성은 다음과 같다.
            1. 가장 가까운 곳 vs 장소 상관 없음
            2. 식당 vs 카페  
                식당) 한식 vs 샐러드 vs 양식 
                카페 / 디저트) 디저트 종류 vs 디저트 필요없어
            3. 가격대
            4. 인원수
            5. 당신은 현재 비건인가요
            6. ...
    - 테스트가 완료되면 테스트 결과 페이지가 나타난다.
    - 테스트 결과 페이지에는 테스트에 따른 장소와 (간단소개) 그리고 위치를 확인할 수 있는 버튼이 있다.
        - 위치 확인 버튼을 누르면 위치 정보가 지도와 연결되도록 한다.

    🥦***웹사이트 정보 제공 페이지***

    - 웹사이트 정보 제공 버튼을 누르면 웹사이트 정보 제공 페이지로 넘어간다.
    - 웹사이트 정보 제공 페이지는 채식 관련 구매 웹사이트 정보를 제공한다.  ****
    - **(장소 전체 데이터도 지도형식으로 제공하면 좋을 듯?싶다)**


<br>

## 참고 사이트/ 프로그램

---

[[Django, 공공데이터포털, Google Map으로 전기차 충전소 위치 찍기]](https://youtu.be/stHfQdcsZFo)

[[Django 템플릿]](http://pythonstudy.xyz/python/article/307-Django-%ED%85%9C%ED%94%8C%EB%A6%BF-Template)

[[Django 튜토리얼]](https://tutorial.djangogirls.org/ko/django_forms/)

[[데이터 베이스 구성 프로그램 / ERD CLOUD]](https://www.erdcloud.com/)

[[kakao 지도 api]](https://apis.map.kakao.com/web/sample/basicMarker/)

[[Django 데이터 변수를 javascript에 넘기기 feat. 카카오맵 API]](https://moondol-ai.tistory.com/133)
