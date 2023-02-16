import datetime, pytz, os, socket, psutil
# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 현재시간
# current_time_kotz = datetime.datetime.now(pytz.timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S") # 현재시간
# print(current_time,'\n', current_time_kotz)

##### 단말의 통신중인 NIC IP확인 #####
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
srv_ip = s.getsockname()[0]

ip_mac = ""
ip_info = ""
for k, v in psutil.net_if_addrs().items(): 
    print("<key>\n{}\n<value>\n{}\n{}\n".format(k,v,len(v)))                 
    if len(v)>1:    
        if v[1].address == srv_ip:                              # 검출된 IP가 통신중인 IP와 동일하다면
            ip_mac = v[0].address                               # mac주소        
            ip_info = v[1].address                              # ip주소
print(srv_ip, ip_mac, ip_info)

os.system("pause")