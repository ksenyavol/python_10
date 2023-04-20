# 4.	Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в байтовое и
# выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words:
    a = i.encode('utf-8')
    print(a)
    b = a.decode('utf-8')
    print(b)


