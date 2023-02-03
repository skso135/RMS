# RMS
Server Resource Monitoring System


#####서버 리소스 모니터링#####
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
    리소스 데이터 수집(OS, IP, CPU, Memory, Disk, Network)
    대시보드(grafana이용)
6.	프로세스
    traceP/G execute in server --> DATA strot to DB --> Data spread to grafana dashboard
7.	개발목표
    Lv0. 데이터 수집하여 DB에 축적
    Lv1. 축적된 Data를 확인하는 Web or P/G 대시보드화면
    ---초과목표---
    Lv2. P/G 경량화
    Lv3. 기능, 소스 및 UI 고도화
8.	개발단계
    수집P/G 개발 -> 완료
    일부서버 배포 및 수집확인 -> 완료
    그라파나 대시보드 적용 -> 진행중
    전 서버 적용 -> 미진행
    경량화 -> 미진행
    고도화 -> 미진행
9.	산출물
매뉴얼 : 
등등










#####실행파일 생성방법#####
1.	Vscode 콘솔창
2.	C:\Users\N-797_LUS\AppData\Roaming\Python\Python39\Scripts\pyinstaller.exe --icon=./icon/monitor_icon1.ico -F C:\Users\N-797_LUS\Desktop\python_code\PythonStudy\practice\RMS\RMS.py 입력
3.	C:\Users\N-797_LUS\AppData\Roaming\Python\Python39\Scripts\dist 또는 C:\Users\N-797_LUS\Desktop\python_code\PythonStudy\practice\RMS\dist 경로 폴더에서 실행파일 확인
 
#####VSCODE에서 Git commit#####
1. 좌측 소스제어 탭 선택
2. 변경사항 +(변경내용스테이징) 클릭
3. 'commit' 버튼 위 텍스트창에 변경이력메시지 작성
4. 'commit' 우측 아래화살표 클릭하여 'commit + push' 클릭