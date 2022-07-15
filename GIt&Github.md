# Git/Github

### git 기본기

- Working Directory - 내가 작업하고 잇는 실제 디렉토리
- Staging Area - 커밋으로 남기고 싶은, 특정버전으로 관리하고 싶은 파일이 있는 곳
- Repository - 커밋들이 저장되는 곳


## git 기본문법

- git init
  - git 저장소를 만들 때 사용 

- git add . 
  - Untracked된 모든 파일 스테이징

- git add readme.md 
  - 특정 파일만 스테이징

- git commit -m '메시지' 
  - 스테이징된 것들을 메시지와 함께 업로드


## github 연결관련 문법

- git remote add origin https://github.com/appletail/SSAFY.git
  - main: 기본브랜치 이름, local repository
  - origin: 'https://github.com/appletail/SSAFY.git' 의 별명

- git push -u origin main
  - -u 를 사용할 경우 내가 설정한 상세한 세팅으로 업로드하고 이후에는 git push만 써도 된다.

- git push 
  - 로컬에서 변경한 것을 올리는 것

- git pull
  - 온라인에서 변경된 것을 내려받는 것

- git clone https://github.com/appletail/SSAFY.git
  - init + remote + pull
  - 깃허브상의 리포지토리를 통으로 내려받으면서 연결까지 한번에 하는 명령어


## git 기타 문법

- git status 
  - 현재 브랜치 위치와 파일들의 상태 확인

- git log
  - git의 commit history 보기
  - log가 길경우 q를 누르면 나갈 수 있음
  - git log --oneline 으로 작성하면 한줄짜리 히스토리를 볼 수 있음

- git diff 주소1 주소2
  - 두 커밋을 비교해서 무엇이 바뀌었는지 비교해줌
