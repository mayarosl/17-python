import string

# открываем файл
file = open ('wiki.txt', 'r', encoding = 'utf-8')
corpus = file.read ()
file.close ()

# делаем все буквы строчными, делим текст на слова
corpus = corpus.lower ()
lines = corpus.split (u'\n') # u' - это юникод, \n' - это новая строка
words = corpus.split ()

print ("Количество строк: ", len (lines))

# создаем счетчик, который считает слова
counter_words = 0

# начинаем цикл, который берет слово из корпуса
# и добавляет его в наш словарь
for word in words:
    word = word.strip (string.punctuation + '')
    # это новая переменая, .strip удаляет то, что мы указали в скобках
    counter_words = counter_words+1
    
print ("Количество слов: ", counter_words)

# создаем счетчик, который считает согласные
counter_cons = 0
# создаем массив, в котором записаны все возможные гласные
consonants = [u'б', u'в', u'г', u'д', u'ѓ', u'ж', u'з', u's', u'j', u'к', u'л',
              u'Љ', u'м', u'н', u'њ', u'п', u'р', u'с', u'т', u'ќ', u'ф', u'х',
              u'ц', u'ч', u'џ', u'ш']
for c in words: #переменная для слова, наличие которого
                # проверим в нашем массиве
    for everyletter in c: #есть ли согласная в нашем слове
        if everyletter in consonants:
    # это что?
            counter_cons = counter_cons+1
            

# создаем счетчик
counter_wov = 0

# создаем массив, в котором записаны все возможные гласные
wovels = [u'а', u'е', u'и', u'о', u'у']
for v in words: #переменная, наличие которой
                # проверим в нашем массиве
    if v in wovels:
    # это что?
        counter_wov = counter_wov+1


char = counter_cons+counter_wov
print ("Количество букв :", char)
