# 5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
import chardet
import os

results = ''
ARGS = ['ping', 'yandex.ru']
subprocess_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in subprocess_ping.stdout:
    results += line.decode('cp866')

ARGS = ['ping', 'youtube.com']
subprocess_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in subprocess_ping.stdout:
    results += line.decode('cp866')

print(results.encode('utf-8').decode('utf-8'))

import subprocess
import chardet
import os

results = ''
ARGS = ['ping', 'youtube.com']
subprocess_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in subprocess_ping.stdout:
    results += line.decode('cp866')

ARGS = ['ping', 'youtube.com']
subprocess_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in subprocess_ping.stdout:
    results += line.decode('cp866')

print(results.encode('utf-8').decode('utf-8'))