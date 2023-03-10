![header](https://capsule-render.vercel.app/api?type=rect&amp;color=gradient&amp;text=%20%20RMS%20%20&amp;fontAlign=30&amp;fontSize=30&amp;textBg=true&amp;desc=Resource%20Management%20System&amp;descAlign=60&amp;descAlignY=50)

# RMS(Resource Monitoring System) - 리소스 모니터링 

## 프로젝트의개요
서버리소스 점검표를 주기적으로 작성하는 시간을 절약하기 위함.


## 프로젝트의특성
관리 대상 서버의 리소스를 DB에 자동수집하여 데이터를 모니터링하고자 함


## RMS_환경세팅
### 개발환경
- OS -> Windows_NT x64 10.0.19044
- DB언어 -> mssql
- DBMS -> SSMS
- DB언어 -> mssql
- DBMS -> SSMS
- IDE -> visual studio code 1.76.0 / python 3.7.0 
- ranguage -> python
- env -> 가상환경사용(anaconda)

### 서버환경
- OS -> winsrv2019 std
- DB서버 -> mssql srv 2016
- DB언어 -> mssql
- dashboard -> grafana


## 개발일정
1월 25일 ~ 3월 31일


## 요구사항
서버세팅
DB세팅
리소스 데이터 수집(OS, IP, CPU, Memory, Disk, Network)
대시보드(grafana이용)세팅


## 프로세스
### 단계
step01. 'RMS P/G' execute in server 
step02. DATA Collect to DB 
step03. Data spread to grafana dashboard
### 도식화
    -------------------------
    |                       |
    |       DASHBOARD       |
    |                       |
    -------------------------
            ^
            |   Data Printing
            |
    -------------------------
    |                       |
    |           DB          |
    |                       |
    -------------------------        
            ^
            |   Resource Collecting
            |
    -------------------------
    |                       |
    |         Servers       | <- 'RMS.exe' Execute
    |                       |
    -------------------------        


## 개발목표
Lv0. 데이터 수집하여 DB에 축적
Lv1. 축적된 Data를 확인하는 Web or P/G 대시보드화면
---초과목표---
Lv2. P/G 경량화(수집주기 1분으로 조정 후 부하량 감소)
Lv3. 고도화 및 개선
### 고도화대상
백그라운드화
작업표시줄 미니아이콘화
작업시작,중지,종료 기능
수집주기 설정
수집항목 설정(필요한가?)
버전업
UI


## 세부개발단계
    서버 설치 -> 가상화에 winsrv2019std 설치 완료 -> 23/02/06
    DB서버 설치 -> sqlsrv2016 설치 완료 -> 23/02/06
    수집P/G 개발 -> 완료 -> 23/02/06
    일부서버 배포 및 수집확인 -> 완료 -> 23/02/06
    그라파나 설치 -> 완료 -> 23/02/06
    그라파나 대시보드 적용 테스트 -> 완료
        대시보드 UI
            대시보드 종류 -> 전체서버, 본사, 국내지사(안양,동탄), 해외지사(베트남), 주요관측서버,
            대시보드 UI -> 현재시간, 서버들 정보(종류, 버전, IP, MAC, 최종수집일시), CPU, MEM, DISK, NETWORK
    전서버 적용 -> 완료 -> 23/02/21
        [서버리스트]
        [위치]  [구분]          [IP]                [주요서버]
        ------------------------1.0.0.7------------------------
        창원    ASM             192.168.10.20               
        창원    Commvault       192.168.10.175          V     1.0.1.0
        창원    emax_ERP        192.168.10.196                     
        창원    ERP_APP         192.168.10.190          V          
        창원    ERPDB           192.168.10.191          V
        창원    GSCMDB          192.168.10.197          V
        창원    GSCMFTP         192.168.10.195          
        창원    EDI             192.168.10.176                     
        창원    License         192.168.10.250          V          
        창원    NH              192.168.10.199                     
        창원    NH(viet)        192.168.10.109          
        창원    RMS             192.168.10.49           V           
        창원    CMS             192.168.10.62                      
        창원    PLM             192.168.10.194          V
        안양    NX서버          192.168.19.178          
        안양    MES             192.168.19.222                     
        안양    License         192.168.19.240          V           
        동탄    License         192.168.31.10           V
        동탄    MES             192.168.31.11                      
        EMVB    PMI T&T         192.168.22.109          V
        EMVB    MES             192.168.22.222          불특정주기로 프로그램 종료 됨
        EMVB    SAMSUNG_TSI     192.168.22.223          V 
        EMVB    SW용 Verify     192.168.22.230          V
        IMS     MES             192.168.23.6            
        EMVT    MES             192.168.52.220   
        창원    ArcServer       192.168.10.45           V
        창원    vcserver        192.168.10.177          리눅스
        ------------------------미적용------------------------
        창원    old_GW          192.168.10.188
        창원    S-Guard         192.168.10.53           리눅스
        창원    R-Guard         192.168.10.54
        창원    Cube#1          192.168.10.55
        창원    Cube#2          192.168.10.56


    RMS.exe 시작프로그램 등록 -> 완료 ->  23/02/21    
    그라파나 대시보드 완전적용 -> 진행중 -> 23/03/31이내(예정)
    인터넷 단절시에도 인터넷 연결대기상태 유지 개발(인터넷 재연결시 전송) -> 23/03/14
    경량화 -> 미진행
    고도화 -> 미진행



## 산출물
매뉴얼 : 개발 결과보고서, 프로그램 동작 메뉴얼 등등







# 실행파일 생성 방법
1.	Vscode 콘솔창
2.  C:\Users\N-797_LUS\Desktop\python_code\PythonStudy\practice\RMS\file_version.txt
    텍스트파일에서 버전정보 수정
3.	<!--C:\Users\N-797_LUS\AppData\Roaming\Python\Python39\Scripts\pyinstaller.exe -->
pyinstaller --icon=./icon/monitor_icon1.ico -F --version-file file_version.txt RMS.py 입력
4.	C:\Users\N-797_LUS\AppData\Roaming\Python\Python39\Scripts\dist 또는 C:\Users\N-797_LUS\Desktop\python_code\PythonStudy\practice\RMS\dist 경로 폴더에서 실행파일 확인
* pyinstall 옵션
    1. --noconsol  -> 콘솔창 없음
 
# VSCODE에서 Git commit 
1. 좌측 소스제어 탭 선택
2. 변경사항 +(변경내용스테이징) 클릭
3. 'commit' 버튼 위 텍스트창에 변경이력메시지 작성
4. 'commit' 우측 아래화살표 클릭하여 'commit + push' 클릭

# 작업되돌리기
터미널 -> git reset --hard HEAD^          #이전에 commit된 작업으로 돌아가기

# 작업이력 확인
터미널 -> git reglog                      #작업이력 확인
터미널 -> git reset --hard 작업코드(ex.896970d) #작업코드로 작업시점소스 리셋하기



# 트러블슈팅
1. exe실행 실패
    현상 : api-ms-core-path~~~.dll 없음
    원인 : 파이썬 3.9 구버전OS(win7,srv2008등)에서 지원불가
    해결책 : 기존파이썬 삭제 -> 아나콘다로 가상환경 구축하여 -> 여러 파이썬 버전으로 테스트 -> 3.7.0버전으로 프로그램 생성하여 사용
2. 콘솔창 종료되는 현상
    현상 : 리소스 수집시 콘솔창 종료
    원인 : 소스중 딕셔너리 키값으로 '이더넷'을 지정해준 소스의 문제로 특정 서버에는 '이더넷'이 아니라 '로컬영역'으로 표시된 네트워크로 되어있어서 오류 발생
    해결책 : 통신중인 ip를 찾아서 해당 ip와 매칭되는 mac주소를 찾는 소스 추가(socket패키지 사용)
<!-- ##### winsdksetup.exe #####
관련링크1 : https://pyinstaller.org/en/stable/usage.html#cmdoption-version-file
관련링크2 : https://devblogs.microsoft.com/cppblog/introducing-the-universal-crt/
범용CRT(=Universal CRT,Universal Visual C++ C Runtime)
구버전OS(win 8.1이하)에서 visual studio 2015용 visual C++ C Runtime이 설치보장되지 않음
그래서 범용CRT 설치해줘야 함 
-> 조치해도 해결안됨-->
3. 서버별 시간대 다름
    현상 : 수집 시간 차이
    원인 : 국외서버의 시간 세팅 값이 다름
    해결책 : 

# 아나콘다 설치 및 vscode 연동
1. 공홈에서 설치
2. 환경변수 추가 -> 재부팅
3. vscode -> ctrl + shift + p -> python interpreter -> 원하는 python버전(가상환경명) 선택
4. python버전변경 -> 'conda install python=버전'

<!-- 3. vscode 연결 , 명령 프롬프트 변경
4. vscode 터미널을 명령프롬프트로 선택해서 열고 'activate' 입력하면 콘다프롬프트로 변경
5. 콘다프롬프트에서 'conda activate 가상환경명' 입력해주면 원하는 환경으로 변경가능 -->