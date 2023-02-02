## 230202 소스날려먹음 ㅠ 새시작





import os, platform, psutil, schedule, datetime, pymssql

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
    os_kind = platform.system()
    os_ver = platform.release()
    pc_name = platform.node()
    ip_info = psutil.net_if_addrs()
    
    # ip_mac = 
    print(ip_info.get('이더넷')[1].address)

    #cpu 사용율
    cpu_used = psutil.cpu_percent()
    #메모리 ttl, 사용량, 사용율
    #네트워크 다운로드양, 업로드양, 초당수신트래픽, 초당발신트래픽
    #디스트 경로, ttl, 사용량, 사용율

    #cursor.execute('insert')   #DB INSERT
    con.close() #DB연결해제


    

# dict_items([
# ('이더넷', [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='B0-25-AA-3B-6C-3F', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.13.104', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::b6a4:b22c:3d1:6c75', netmask=None, broadcast=None, ptp=None)]), 
# ('Wi-Fi', [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='34-2E-B7-EA-B0-D7', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.183.32', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::e348:629c:2cdf:a503', netmask=None, broadcast=None, ptp=None)]), 
# ('로컬 영역 연결* 1', [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='34-2E-B7-EA-B0-D8', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.74.106', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::6627:14e3:da95:ccd5', netmask=None, broadcast=None, ptp=None)]), 
# ('로컬 영역 연결* 10', [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='36-2E-B7-EA-B0-D7', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.201.254', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::71df:bcff:bbc3:f872', netmask=None, broadcast=None, ptp=None)]), 
# ('Bluetooth 네트워크 연결 3', [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='34-2E-B7-EA-B0-DB', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.155.156', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::fb60:e766:d792:ab3b', netmask=None, broadcast=None, ptp=None)]), 
# ('Loopback Pseudo-Interface 1', [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)])
# ])

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
