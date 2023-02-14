# RMS
Server Resource Monitoring System


##### 서버 리소스 모니터링 #####
1.	프로젝트의 개요
    서버리소스 점검표를 주기적으로 작성하는 시간을 절약하기 위함.
2.	프로젝트의 특성
    관리 대상 서버의 리소스를 DB에 자동수집하여 데이터를 모니터링하고자 함
3.	개발환경
    <개발환경>
    OS -> win10
    IDE -> visual studio code
    ranguage -> python
    DB -> mssql
    DBMS -> SSMS
    <서버환경>
    OS -> winsrv2019 std
    DB -> mssql srv 2016
    dashboard -> grafana
4.	개발일정 : 1월 25일 ~ 3월 31일
5.	요구사항
    서버세팅
    DB세팅
    리소스 데이터 수집(OS, IP, CPU, Memory, Disk, Network)
    대시보드(grafana이용)세팅
6.	프로세스
    traceP/G execute in server --> DATA save to DB --> Data spread to grafana dashboard
7.	개발목표
    Lv0. 데이터 수집하여 DB에 축적
    Lv1. 축적된 Data를 확인하는 Web or P/G 대시보드화면
    ---초과목표---
    Lv2. P/G 경량화
    Lv3. 기능, 소스 및 UI 고도화
8.	세부개발단계
    서버 설치 -> 가상화에 winsrv2019std 설치 완료 ~23/02/06
    DB서버 설치 -> sqlsrv2016 설치 완료 ~23/02/06
    수집P/G 개발 -> 완료 ~23/02/06
    일부서버 배포 및 수집확인 -> 완료 ~23/02/06
    그라파나 설치 -> 완료 ~23/02/06
    그라파나 대시보드 적용 테스트 -> 완료
        대시보드 UI
            그룹핑 -> 전체화면, 창원, (안양,동탄), 해외(베트남)
            UI -> 현재시간, OS정보(종류, 버전), IP, MAC
    전서버 적용 -> 진행중 -> 23/03/31이내(예정)
        <서버리스트>
        위치            구분            IP                  설치유무            비고
        창원            ASM             192.168.10.20           V
        창원            Commvault       192.168.10.175          V
        창원            ERPDB           192.168.10.191          V
        창원            GSCMFTP         192.168.10.195          V
        창원            GSCMDB          192.168.10.197          V
        창원            emax_ERP        192.168.10.196          X           실패원인 확인필요
        창원            ERPAPP          192.168.10.190          X           실패원인 확인필요
        창원            EDI             192.168.10.176          X           실패원인 확인필요(저버전)
        창원            License         192.168.10.250          X           실패원인 확인필요
        창원            NH              192.168.10.199          X           실패원인 확인필요
        창원            NH(veit)        192.168.10.109          X           실패원인 확인필요
        창원            RMS             192.168.10.49           X           실패원인 확인필요
        창원            CMS             192.168.10.62           X           실패원인 확인필요
        창원            PLM             192.168.10.194          X           실패원인 확인필요
        창원            OLD_GW          192.168.10.188
        안양            NX서버          192.168.19.178
        안양            License         192.168.19.240          X           실패원인 확인필요
        안양            MES             192.168.19.222          X           실패원인 확인필요
        동탄            MES             192.168.31.11           X           실패원인 확인필요
        동탄            License         192.168.31.10           V
        EMVB            MES             192.168.22.222          X           실패원인 확인필요
        EMVB            SAMSUNG_TSI     192.168.22.223          X           실패원인 확인필요
        EMVB            PMI T&T         192.168.22.109
        EMVB            SW용 Verify     192.168.22.230
        EMVT            MES             192.168.52.220
        IMS             MES             192.168.23.6


    
    그라파나 대시보드 완전적용 -> 진행중 -> 23/03/31이내(예정)
    경량화 -> 미진행
    고도화 -> 미진행
9.	산출물
매뉴얼 : 
등등







##### 실행파일 생성방법 #####
1.	Vscode 콘솔창
2.	C:\Users\N-797_LUS\AppData\Roaming\Python\Python39\Scripts\pyinstaller.exe --icon=./icon/monitor_icon1.ico -F C:\Users\N-797_LUS\Desktop\python_code\PythonStudy\practice\RMS\RMS.py 입력
3.	C:\Users\N-797_LUS\AppData\Roaming\Python\Python39\Scripts\dist 또는 C:\Users\N-797_LUS\Desktop\python_code\PythonStudy\practice\RMS\dist 경로 폴더에서 실행파일 확인
* pyinstall 옵션
    1. --noconsol  -> 콘솔창 없음
 
##### VSCODE에서 Git commit #####
1. 좌측 소스제어 탭 선택
2. 변경사항 +(변경내용스테이징) 클릭
3. 'commit' 버튼 위 텍스트창에 변경이력메시지 작성
4. 'commit' 우측 아래화살표 클릭하여 'commit + push' 클릭

##### 작업되돌리기 #####
터미널 -> git reset --hard HEAD^          #이전에 commit된 작업으로 돌아가기

##### 작업이력 확인 #####
터미널 -> git reglog                      #작업이력 확인
터미널 -> git reset --hard 작업코드(ex.896970d) #작업코드로 작업시점소스 리셋하기



##### 트러블슈팅 #####
1. exe실행 실패
    현상 : api-ms-core-path~~~.dll 없음
    원인 : 파이썬 3.9 구버전OS(win7,srv2008등)에서 지원불가
    해결책 : 
2. 콘솔창 종료되는 현상
    현상 : 리소스 수집시 콘솔창 종료
    원인 : (추정원인)import된 패키지가 안먹히는?
    해결책 : 

##### winsdksetup.exe #####
관련링크1 : https://pyinstaller.org/en/stable/usage.html#cmdoption-version-file
관련링크2 : https://devblogs.microsoft.com/cppblog/introducing-the-universal-crt/
범용CRT(=Universal CRT,Universal Visual C++ C Runtime)
구버전OS(win 8.1이하)에서 visual studio 2015용 visual C++ C Runtime이 설치보장되지 않음
그래서 범용CRT 설치해줘야 함