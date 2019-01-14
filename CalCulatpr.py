#!/usr/bin/python
#Author : MR.CL4Y
#Contact : 085752481601
import random
import sys
import time
import os,sys
blue = '\033[34;1m'
green = '\033[32;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('WELCOME IN MY TOOLS..')
mengetik('.')
mengetik('.')
mengetik('menghubungi MR.CL4Y..')
mengetik ('Please Wait !!')
mengetik ('WELCOME..!!')
mengetik ('kalo gak Tau Username Sama Password Bisa pm = 085752481601')
print
print ("\033[1;32mMasukan UserName&Password")
username = 'MR.CL4Y'
password = 'RcT'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:

			os.system('clear')
                else:
                        print "\n\033[1;36mSorry Invalid password !!!\033[00m"
                        print "Back Login\n"
                        restart()

        else:
                print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
os.system(" figlet -f slant MR.CL4Y |lolcat")
print(green),"###############################################"
time.sleep(0.23)
print(red),"###############################################"
time.sleep(0.23)
print(cyan),"Author         : MR.CL4Y"
print(purple),"Github       : https://github.com/RabbitCL4Y"
print(red),"Contact         : RabbitCL4Y123@gmail.com"
print(yellow),"Team         : Rabbit Cyber Team"
print(blue),"Team           : 2Easy4Hack Team"
print(green),"###############################################"
time.sleep(0.23)
print(red),"###############################################"
x = input('masukkan angka ke 1 :')
y = input('masukkan angka ke 2 :')
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1 + num2)
