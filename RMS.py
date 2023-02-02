## 230202 소스날려먹음 ㅠ 새시작





import platform, psutil, schedule, datetime, pymssql

# 함수 선언
def message():
    #####DB연결부분#####
    #DB연결정보
    server = '192.168.10.49'
    database = 'RMS'
    username = 'sa'
    password = 'emtech@2580'
    #DB접속
    con = pymssql.connect(server, username, password, database)
    cursor = con.cursor()
    #SQL 실행문
    # cursor.execute('select * from rms100')
    # print(cursor.fetchone())

    #####정보출력부분#####
    #수집시간, 전송주기
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print("<데이터 수집시간:{}>\n<수집주기:{}분>".format(str(current_time),rep_time))
    #print("<수집정보>\n{}".format())

    #OS 종류, 버전, PC명
    print(psutil)
    os_kind = platform.system()
    os_ver = platform.release()
    pc_name = platform.node()

    #cpu 사용율
    #메모리 ttl, 사용량, 사용율
    #네트워크 다운로드양, 업로드양, 초당수신트래픽, 초당발신트래픽
    #디스트 경로, ttl, 사용량, 사용율

    #cursor.execute('insert')   #DB INSERT
    con.close() #DB연결해제






# 실행소스
rep_time = 10                               # 반복주기
schedule.every(5).seconds.do(message)       # 반복설정
#schedule.every(10).minutes.do(message)     # 반복설정



# 스캐쥴 시작
while True:
    schedule.run_pending()
    #time.sleep(1)

# 설치 패키지리스트
# 설치방법 : pip install [패키지명]
# pyinstaller : 실행파일 생성을 위한 패키지
# pymssql : mssql 연결을 위한 패키지
# psutil : 시스템 리소스 정보출력을 위한 패키지
# platform : OS 정보출력을 위한 패키지
