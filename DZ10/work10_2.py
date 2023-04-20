# 2.Каждое из слов «class», «function», «method» записать в
# байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое
# и длину соответствующих переменных

str = ['class', 'function', 'method']

for word in str:
    byte_word = bytes(word, 'ascii')
    print(f'Переменная {word}:')
    print(f"\tТип: {type(byte_word)}")
    print(f"\tСодержимое: {byte_word}")
    print(f"\tДлина: {len(byte_word)}")

    
    
