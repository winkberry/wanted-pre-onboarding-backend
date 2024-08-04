# wanted-pre-onboarding-backend
원티드 프리온보딩 백엔드
( python + django + DRF)

# 기업의 채용을 위한 웹 서비스

# 채용공고 목록 보기  
http://127.0.0.1:8000/api/Recruitment-Notice/  

# 채용공고 목록 상세보기  
http://127.0.0.1:8000/api/Recruitment-Notice/{채용공고ID}  
  
# 채용공고 등록하기  
요청타입: POST  
요청URL : http://localhost:8000/api/Recruitment-Notice/  
HEADER : Content-Type을 application/json으로 설정  
BODY -> ROW -> JSON  
{  
    "company": 1,  
    "position": "백엔드 시니어 개발자",  
    "compensation": 3000000,  
    "technologies": "PHP, apach",  
    "content": "00회사에서 백엔드 시니어 개발자를 채용합니다."  
}  
  
# 채용공고 수정하기  
요청타입: PUT  
요청URL : http://localhost:8000/api/Recruitment-Notice/{채용공고ID}  
BODY -> ROW -> JSON  
{  
    "company": 1,  
    "position": "수정할내용",  
    "compensation": 수정할금액,  
    "technologies": "수정할스택",  
    "content": "수정할내용."  
}  
  
# 채용공고 삭제하기  
요청타입: DELETE  
요청URL : http://localhost:8000/api/Recruitment-Notice/{채용공고ID}  
  
