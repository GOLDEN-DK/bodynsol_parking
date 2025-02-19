1단계: 기본 환경 설정

1. 개발 환경 구축
   Python 가상환경 설정
   필수 라이브러리 설치 (Selenium, Flask, SQLite)
   Electron 프로젝트 초기화

단계별로 진행이 되면 좋을 것 같아.
전체적인 프로세스를 한번 확인 해줘.

2. 프로젝트 구조 생성

project/
├── backend/
│ ├── main.py
│ ├── services/
│ │ ├── automation.py
│ │ └── db_service.py
│ └── db/
│ └── database.db
└── frontend/
├── main.js
├── index.html
└── renderer.js

2단계: Python 백엔드 개발

1. Selenium 자동화 구현

- 로그인 기능
- 차량 조회 기능
- 주차시간 등록 기능

2. Flask API 서버 구현

- /check-car 엔드포인트
- /confirm-car 엔드포인트

3. SQLite DB 구현

- requests 테이블 생성
- session 테이블 생성
- DB 연동 로직 구현

3단계: Electron 프론트엔드 개발

1. 기본 UI 구현

- 차량번호 입력 폼
- 주차시간 선택 UI
- 사진 표시 영역
- 확인/다음 버튼

2. Python 백엔드 연동

- API 호출 로직 구현
- 응답 처리 로직 구현

4단계: 테스트 및 디버깅

1. 기능 테스트

- 로그인 테스트
- 차량 조회 테스트
- 주차시간 등록 테스트

2. 예외 처리

- 네트워크 오류
  로그인 실패
  차량 조회 실패

5단계: 배포 준비

1. Python 백엔드 패키징

- PyInstaller로 exe 파일 생성
- 의존성 확인 및 처리

2. Electron 앱 패키징

- electron-builder 설정
- 윈도우용 인스톨러 생성

6단계: 배포 및 유지보수

1. 배포

- 설치 프로그램 테스트
- 실제 환경 테스트

2. 유지보수 계획

- 로그 모니터링
- 버그 수정
- 기능 업데이트
