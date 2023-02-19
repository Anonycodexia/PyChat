#!/bin/python

import sys, time, socket, threading, os

os.system('clear')

class colors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[31m'
    pink = '\033[35m'


banner = colors.cyan + """

           ████████████████████
          █────────────────────█
         █──────────────────────█
        █─────▄████▄──▄████▄─────█
        █───██▀────▀██▀────▀██───█
        █──██──▄▄▄──██──▄▄▄─▀██──█
       ▄█████──███──██──███──█████▄
       ██████──────████──────██████
       ▀█▀─▀██▄▄▄███▀▀███▄▄▄██▀─▀█▀
        █────▀▀▀▀▀──────▀▀▀▀▀────█
        █──────▄▄───────▄▄───────█
        █▄──────▀▀▀▀▀▀▀▀▀───────▄█
        █▓█────────────────────█▓█
        █▓▓█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▓▓█
       ▄██████████████████████████▄
       ██▀──────────────────────▀██
     ▄█▀──                      ──▀█▄
     ██▀─      PYTHON CHAT      ──▀██
     ██▀─         SERVER        ──▀██
     ██▀──────────────────────────▀██
      █─       PROGRAMMED BY      ─█
      █─                          ─█
      █─        ANONYCODEXIA      ─█
      █▄▄────────────────────────▄▄█
       ▀▀████████████████████████▀▀
         ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
          ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
           ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
            ▐▓▓▓▓▓▓▓▌▐▓▓▓▓▓▓▓▌
              ▐▓▓▓▓▌──▐▓▓▓▓▓▌
             ▄████▀────▀████▄



 [*]    SIMPLE PYTHON CHAT SERVER [*]
 [*]    Programmed By Anonycodexia    [*]

"""


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


print(banner)
slowprint(colors.pink + "[CONNECTING] Connecting to server..." )
slowprint(colors.green + "[CONNECTED] Connected to server...")
nickname = input(colors.blue + "[+] Enter your username : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 4545
client.connect((server, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            slowprint(bcolor.red + "[ERROR] An error occured!")
            client.close()
            break


def write():
    while True:
        message = '[{}] >> {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

