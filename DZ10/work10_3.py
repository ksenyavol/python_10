# 3.	Определить, какие из слов «attribute», «класс», «функция»,
# «type» невозможно записать в байтовом типе.

words = ['attribute', 'класс', 'функция']

for word in words:
    try:
        byte_word = bytes(word, 'ascii')
        print(f"{word} - Можно записать в байтовом формате")
    except UnicodeEncodeError:
        print(f"{word}  - невозможно записать в байтовом формате")
