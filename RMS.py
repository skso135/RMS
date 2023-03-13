## 230202 소스날려먹음 ㅠ 새시작
######### Dev By. EM-TECH 전산팀 권철환 대리 #############
##### github 주소 : https://github.com/skso135/RMS.git
#####
##### 설치 패키지리스트
##### 설치방법 : pip install [패키지명]
##### pyinstaller : 실행파일 생성을 위한 패키지
##### pymssql : mssql 연결을 위한 패키지
##### psutil : 시스템 리소스 정보출력을 위한 패키지
##### platform : OS 정보출력을 위한 패키지
##### math : 사이즈 변환 함수 작성을 위한 패키지
##### traceback : 스케쥴 무한반복 예외시 에러메세지 확인용 패키지
##### socket : 현재사용중인 네트워크 정보확인을 위한 패키지
##### pytz : 타임존 확인을 위한 패키지
## 230215 아나콘다로 환경 재세팅

import platform, psutil, datetime, pymssql, time, math, traceback, socket, os
from pytz import timezone
from datetime import datetime
# import schedule

# 사이즈 변환 함수
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s%s" % (s, size_name[i])

# 리소스 수집 및 출력 함수
def resource_trace():
    #####DB연결부분#####
    #DB연결정보
    server = '192.168.10.49'
    database = 'RMS'
    username = 'sa'
    password = 'emtech@2580'
    #DB접속
    con = pymssql.connect(server, username, password, database)
    cursor = con.cursor()

    ##### 단말의 통신중인 NIC IP확인 #####
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    srv_ip = s.getsockname()[0]
    #####리소스수집부분#####
    current_time = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S") # 현재시간
    os_kind = platform.system()                                 # os 종류
    os_ver = platform.release()                                 # os 버전
    pc_name = platform.node()                                   # PC컴퓨터명
    ip_mac = ""
    ip_info = ""
    for k, v in psutil.net_if_addrs().items(): 
        if len(v)>1:                                                
            if os_kind == "Windows":
                if v[1].address == srv_ip:                              # 검출된 IP가 통신중인 IP와 동일하다면 
                    ip_mac = v[0].address                               # mac주소
                    ip_info = v[1].address                              # ip주소 
            elif os_kind == "Linux":
                if v[0].address == srv_ip:                              # 검출된 IP가 통신중인 IP와 동일하다면 
                    ip_mac = v[2].address                               # mac주소
                    ip_info = v[0].address                              # ip주소

            
    cpu_used = psutil.cpu_percent()                               # cpu 사용율
    mem_ttl = psutil.virtual_memory().total                     # 메모리TTL
    mem_used = psutil.virtual_memory().used                     # 메모리사용량
    mem_userate = psutil.virtual_memory().percent               # 메모리사용율
    mem_availrate = round(100 - mem_userate,2)                  # 메모리여유율
    down_ttl_bef = psutil.net_io_counters().bytes_recv          # 1초전 다운로드량
    up_ttl_bef = psutil.net_io_counters().bytes_sent            # 1초전 업로드량
    time.sleep(1)                                               # 1초 딜레이
    down_ttl = psutil.net_io_counters().bytes_recv              # 현재 다운로드량
    up_ttl = psutil.net_io_counters().bytes_sent                # 현재 업로드량
    down_speed = down_ttl - down_ttl_bef                        # 초당 다운로드
    up_speed = up_ttl - up_ttl_bef                              # 초당 업로드
    DiskList = []                                               # disklist 선언
    for i in psutil.disk_partitions():                          # 디스크파티션 요소로 반복 
        if i.fstype in ('NTFS','FAT12','FAT16','FAT32','ext','ext2','ext3','ext4','xfs'):        # 디스크 종류범위내에 있을때
            DiskList.append(i.mountpoint)                           # disklist에 추가
        
    ####정보출력부분#####
    print("\n<데이터 수집시간:{} 수집주기:{}초>\n<리소스정보>\n[OS정보] 종류:{} | 버전:{} | PC명:{} | IP주소:{} | MAC주소:{}\n[CPU정보] 사용율:{}%\n[Memory정보] 총용량:{} | 사용량:{} | 사용율:{}% | 여유율:{}%\n[Network정보] 다운로드속도:{}/s | 업로드속도:{}/s"
    .format(str(current_time),rep_time,os_kind,os_ver,pc_name,ip_info,ip_mac,cpu_used,convert_size(mem_ttl),convert_size(mem_used),mem_userate,mem_availrate,convert_size(down_speed),convert_size(up_speed)))
    
    ####디스크정보수집#####
    sqlquery = ""
    for i in DiskList:                                          # disklist 요소로 반복
        disk_path = i                                           # 디스크경로
        disk_ttl = psutil.disk_usage(i).total                   # 디스크총용량
        disk_used = psutil.disk_usage(i).used                   # 디스크사용량
        disk_userate = psutil.disk_usage(i).percent             # 디스크사용율
        disk_availrate = round(100-disk_userate,2)              # 디스크여유율
        print("[DISK정보] 경로:{} | 총용량:{} | 사용량:{} | 사용율:{}% | 여유율:{}%".format(disk_path,convert_size(disk_ttl),convert_size(disk_used),disk_userate,disk_availrate))
        #####insert query문#####
        sqlquery += ("insert into rms100 values('{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},'{}');"
        .format((ip_mac+"_"+ip_info),os_kind,os_ver,pc_name,ip_info,ip_mac,cpu_used,mem_ttl,mem_used,mem_userate,mem_availrate,down_ttl,up_ttl,down_speed,up_speed,disk_path,disk_ttl,disk_used,disk_userate,disk_availrate,current_time))
    
    #####DB 데이터 전송부분#####
    cursor.execute(sqlquery)    
    con.commit()    # DB입력승인
    con.close()     # DB연결해제



# 실행소스
rep_time = 60 #int(input("수집주기를 입력해주세요(초 단위, 3600초=1시간) --> "))  # 반복주기
print("<데이터수집중({})... 수집주기:{}초>"
      .format(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S"),rep_time))
while True:
    try : 
        ipaddress=socket.gethostbyname(socket.gethostname())
        if ipaddress == '127.0.0.1':                                            # 인터넷 통신불가
            print("You are not connected to the internet! Please Check!")
        else:                                                                   # 인터넷 통신
            resource_trace()                                                    # 데이터 수집 함수
        time.sleep(rep_time)                                                # 수집 딜레이
    except Exception as e:
        print(traceback.format_exc())
        print("Exception Message : ",e)
        break

os.system("pause")                                          # 에러종료시 콘솔창 유지



# # 스캐쥴 시작
# sched.every(rep_time).seconds.do(resource_trace)          # 반복설정
# while True:
#     try : 
#         sched.run_pending()
#     except Exception as e:
#         print(traceback.format_exc())
#         print(e)
#         break








