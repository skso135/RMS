import platform, psutil, datetime, pymssql, time, math, traceback, socket
from pytz import timezone
from datetime import datetime

def resource_trace():
    cpu_used = psutil.cpu_percent()                               # cpu 사용율
    cpu_used2 = psutil.cpu_percent(percpu=True)
    print("{}\n{}".format(cpu_used, cpu_used2))

# 실행소스
rep_time = 3 #int(input("수집주기를 입력해주세요(초 단위, 3600초=1시간) --> "))  # 반복주기
print("<데이터수집중({})... 수집주기:{}초>"
      .format(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S"),rep_time))
while True:
    try : 
        resource_trace()
        time.sleep(rep_time)
    except Exception as e:
        print(traceback.format_exc())
        print("Exception Message : ",e)
        break