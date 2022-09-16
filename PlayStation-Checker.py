try:import random;from colorama import Fore;from requests import post;from user_agent import generate_user_agent;from time import sleep
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
def saver(user):
    ID=''#Telegram id
    token=''#Telegram bot token
    try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New username’s Claimed @{user} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck')
    except:pass
    with open('Available.txt', 'a') as x:
        x.write(user+'\n')
def with_list():
    error,count,done=0,0,0
    try:file=open('user.txt', 'r')
    except FileNotFoundError:exit('[!] No users File Detected - Note users file must be in user.txt File ..')
    while True:
        sleep(3)
        user=file.readline().split('\n')[0]
        ru=post(f"https://accounts.api.playstation.com/api/v1/accounts/onlineIds",headers={'Host': 'accounts.api.playstation.com','User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://id.sonyentertainmentnetwork.com/','Content-Type': 'application/json; charset=utf-8','Content-Length': '58','Origin': 'https://id.sonyentertainmentnetwork.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'cross-site','Te': 'trailers','Connection': 'close'},json={"onlineId": user,"reserveIfAvailable": False}).status_code
        if ru==201 or ru==200:print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='');done+=1;count+=1;saver(user)
        elif ru==406 or ru==429 or ru==400:print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='');error+=1;count+=1
        else:print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='');error+=1;count+=1
def without_list():
    count,done,error=0,0,0
    user=""
    lena=input('[?] Length: ');length=(int(lena))
    if length<16:pass
    else:exit("[!] Max Letters in The user is 16")
    if length>3:pass
    else:exit("[!] Min Letters in The user is 3")
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm1234567890"
    while True:
        sleep(3)
        for user in range(1):
            user=""
            for item in range(length):
                user+=random.choice(chars)
        ru=post(f"https://accounts.api.playstation.com/api/v1/accounts/onlineIds",headers={'Host': 'accounts.api.playstation.com','User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://id.sonyentertainmentnetwork.com/','Content-Type': 'application/json; charset=utf-8','Content-Length': '58','Origin': 'https://id.sonyentertainmentnetwork.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'cross-site','Te': 'trailers','Connection': 'close'},json={"onlineId": user,"reserveIfAvailable": False}).status_code
        if ru==201 or ru==200:print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='');done+=1;count+=1;saver(user)
        elif ru==406 or ru==429 or ru==400:print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='');error+=1;count+=1
        else:print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='');error+=1;count+=1
print("""

██████╗ ██╗     ███████╗       ██████╗██╗  ██╗
██╔══██╗██║     ██╔════╝      ██╔════╝██║  ██║
██████╔╝██║     ███████╗█████╗██║     ███████║
██╔═══╝ ██║     ╚════██║╚════╝██║     ██╔══██║
██║     ███████╗███████║      ╚██████╗██║  ██║
╚═╝     ╚══════╝╚══════╝       ╚═════╝╚═╝  ╚═╝
                                                                   
        By @TweakPY - @vv1ck                          
""")
LW=int(input("[1] without List\n[2] with List\n---------------\nEnter > : "))
if LW==1:without_list()
elif LW==2:with_list()
else:exit('\n[!] Exit... \n\nBy @TweakPY - @vv1ck')
