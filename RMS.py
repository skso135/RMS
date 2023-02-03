## 230202 소스날려먹음 ㅠ 새시작





import platform, psutil, schedule, datetime, pymssql, time

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

    #OS 종류, 버전, PC명, ip, mac
    os_kind = platform.system()                                 # os 종류
    os_ver = platform.release()                                 # os 버전
    pc_name = platform.node()                                   # PC컴퓨터명
    ip_mac = psutil.net_if_addrs().get('이더넷')[0].address     # mac주소
    ip_info = psutil.net_if_addrs().get('이더넷')[1].address    # ip주소
    
    #####리소스 수집#####
    cpu_used = psutil.cpu_percent()                             # cpu 사용율
    mem_ttl = psutil.virtual_memory().total                     # 메모리TTL
    mem_used = psutil.virtual_memory().used                     # 메모리사용량
    mem_userate = psutil.virtual_memory().percent               # 메모리사용율
    mem_availrate = psutil.virtual_memory().available           # 메모리여유율

    #네트워크 다운로드양, 업로드양, 초당수신트래픽, 초당발신트래픽
    down_ttl_bef = psutil.net_io_counters().bytes_recv          # 1초전 다운로드량
    up_ttl_bef = psutil.net_io_counters().bytes_sent            # 1초전 업로드량
    time.sleep(1)                                               # 1초 딜레이
    down_ttl = psutil.net_io_counters().bytes_recv              # 현재 다운로드량
    up_ttl = psutil.net_io_counters().bytes_sent                # 현재 업로드량
    down_speed = down_ttl - down_ttl_bef                        # 초당 다운로드
    up_speed = up_ttl - up_ttl_bef                              # 초당 업로드
    #디스트 경로, ttl, 사용량, 사용율
    DiskList = []                                               # disklist 선언
    for i in psutil.disk_partitions():                          # 디스크파티션 요소로 반복
        if i.fstype == 'NTFS':                                  # NTFS일때 
            DiskList.append(i.device)                           # disklist에 추가
    for i in DiskList:                                          # disklist 요소로 반복
        disk_path = i                                           # 디스크경로
        disk_ttl = psutil.disk_usage(i).total                   # 디스크총용량
        disk_used = psutil.disk_usage(i).used                   # 디스크사용량
        disk_userate = psutil.disk_usage(i).percent             # 디스크사용율
        disk_availrate = 100-disk_userate                       # 디스크여유율
        print("경로:{}, 총용량:{}, 사용량:{}, 사용율:{}, 여유율:{}".format(disk_path,disk_ttl, disk_used, disk_userate, disk_availrate))


    

    #cursor.execute('insert')   #DB INSERT
    con.close() #DB연결해제




# 실행소스
rep_time = 10                               # 반복주기
schedule.every(3).seconds.do(message)       # 반복설정
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
