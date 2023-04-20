# 5.Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

<<<<<<< Work10

import subprocess
import chardet
import os

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

ARGS = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

print(os.name)
=======

import subprocess
import chardet
import os

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

ARGS = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

print(os.name)

>>>>>>> new_branch
