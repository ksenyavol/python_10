# 1.Каждое из слов «разработка», «сокет», «декоратор» представить
# в строковом формате и проверить тип и содержание соответствующих
# переменных. Затем с помощью онлайн-конвертера преобразовать строковые
# представление в формат Unicode и также проверить тип и содержимое
# переменных.

strs = ['разработка', 'сокет', 'декоратор']

for word in strs:
    print(f'{type(word)},содержимое: {word}')
    print("После преобразования: ")

    for word in strs:
        unicode_word = ""
        for letter in word:
            unicode_word+= "\\u" + str(hex(ord(letter)))[2:]
        print(f'{type(unicode_word)},содержимое: {unicode_word}')

