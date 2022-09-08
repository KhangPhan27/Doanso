from colorama import init, Fore, Back, Style
from colorama import Fore, Back, Style
import  os 
import sys
import time
from random import uniform
os.system('clear')
text='Đây là 1 chương trình đoán số được phát triển bởi Khang Phan'
for x in text:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(uniform(0, 0.2))
time.sleep(3)
check = True
checkanswer = True
while check == True:
     os.system('clear')
     sum=0
#function
     def logo():
          print(Fore.RED + '   _  ___    _          _   _  _____ ')
          print(' | |/ / |  | |   /\   | \ | |/ ____|')
          print(" | ' /| |__| |  /  \  |  \| | |  __ ")
          print(' |  < |  __  | / /\ \ | . ` | | |_ |')
          print(' | . \| |  | |/ ____ \| |\  | |__| |')
          print(' |_|\_\_|  |_/_/    \_\_| \_|\_____|')
          print(Fore.GREEN)
          print('Delerloped by Khang Phan \n')
          print(Fore.YELLOW)
          print('hãy nghĩ về một con số từ 1 đến 64 và tìm chúng trong dãy số sau đây \nnếu có ấn "yes" nếu không ấn "no" \n')
          print(Fore.CYAN)
          return;
          
     logo()
     print('Dãy 1:')
     print('1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 41 43 45 47 49 51 53 55 57 59 61 63')
     print(Fore.MAGENTA)
     inp=input('[yes or no]? ')
     if inp=='yes':
	      sum=sum+1
     inp=0
     
     os.system('clear')
     logo()
     print('Dãy 2:')
     print('2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31 34 35 38 39 42 43 46 47 50 51 54 55 58 59 62 63')
     print(Fore.MAGENTA)
     inp=input('[yes or no]? ')
     if inp=='yes':
	      sum=sum+2
     inp=0

     os.system('clear')
     logo()
     print('Dãy 3:')
     print(' 4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31 36 37 38 39 44 45 46 47 52 53 54 55 60 61 62 63')
     print(Fore.MAGENTA)
     inp=input('[yes or no]? ')
     if inp=='yes':
	      sum=sum+4
     inp=0

     os.system('clear')
     logo()
     print('Dãy 4:')
     print(' 8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31 40 41 42 43 44 45 46 47 56 57 58 59 60 61 62 63')
     print(Fore.MAGENTA)
     inp=input('[yes or no]? ')
     if inp=='yes':
	      sum=sum+8
     inp=0

     os.system('clear')
     logo()
     print('Dãy 5:')
     print(' 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63')
     print(Fore.MAGENTA)
     inp=input('[yes or no]? ')
     if inp=='yes':
	      sum=sum+16
     inp=0

     os.system('clear')
     logo()
     print('Dãy 6:')
     print(' 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63')
     print(Fore.MAGENTA)
     inp=input('[yes or no]? ')
     if inp=='yes':
	      sum=sum+32
     inp=0
     print(sum)
     os.system('clear')
     print(Fore.RED + '   _  ___    _          _   _  _____ ')
     print(' | |/ / |  | |   /\   | \ | |/ ____|')
     print(" | ' /| |__| |  /  \  |  \| | |  __ ")
     print(' |  < |  __  | / /\ \ | . ` | | |_ |')
     print(' | . \| |  | |/ ____ \| |\  | |__| |')
     print(' |_|\_\_|  |_/_/    \_\_| \_|\_____|')
     print(Fore.GREEN)
     print('Delerloped by Khang Phan \n') 
     print(Fore.CYAN)
     print('Số bạn chọn là: ',sum)
     print(Fore.MAGENTA)
     repeat=input('bạn có muốn thử lại [yes/no]: ')
     if repeat=='yes':
     	check =True
     else:
     	check =False


