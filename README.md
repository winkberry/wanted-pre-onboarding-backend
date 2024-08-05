# wanted-pre-onboarding-backend
원티드 프리온보딩 백엔드
( python + django + DRF)

# 기업의 채용을 위한 웹 서비스

## 채용공고 목록 보기  
http://127.0.0.1:8000/api/Recruitment-Notice/  
반환값 :  
![My Image](https://github.com/winkberry/wanted-pre-onboarding-backend/blob/main/등록완료후목록.png)

## 채용공고 목록 상세보기  
http://127.0.0.1:8000/api/Recruitment-Notice/{채용공고ID}
  
## 채용공고 등록하기  
요청타입: POST  
요청URL : http://localhost:8000/api/Recruitment-Notice/  
HEADER : Content-Type을 application/json으로 설정  
BODY -> ROW -> JSON       
![My Image](https://github.com/winkberry/등록.png)

## 채용공고 수정하기  
요청타입: PUT  
요청URL : http://localhost:8000/api/Recruitment-Notice/{채용공고ID}  
BODY -> ROW -> JSON  
![My Image](https://github.com/winkberry/풋요청.png)  
  
반환값 :  
![My Image](https://github.com/winkberry/풋성공.png)
  
## 채용공고 삭제하기  
요청타입: DELETE  
요청URL : http://localhost:8000/api/Recruitment-Notice/{채용공고ID}  
반환값 :  
![My Image](https://github.com/winkberry/딜리트완료후목록.png)  

## 채용공고 검색하기 (선택사항)
요청타입 : GET  
요청URL : http://localhost:8000/api/search/Recruitment-Notice/?company_name={회사이름}&position={포지션}&company_country={국가}&company_region={지역}&compensation={금액}&technologies={사용기술}
* 공백이 삽입되어 있을 경우 공백에 '%20'를 삽입하면 됩니다.
  
![My Image](https://github.com/winkberry/html로검색.png)    
