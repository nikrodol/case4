"""Case-study #4 Анализ текста
Разработчики:
Батенев П.А., Григорьев А.Е., Долгих Н.А.
"""

text = input("Введите текст:")
count_sentence = text.count(".") + text.count("?") + text.count("!")
number = text.split()
count_words = len(number)
text_ = text.lower()
count_syllables = text_.count("а") + text_.count("е") + text_.count("о") + text_.count("у") + text_.count("э") \
                  + text_.count("ю") + text_.count("я") + text_.count("и") + text_.count('ы')

ASL = None
ASW = None
FRE = None
print('Предложений:', count_sentence)
print('Слов:', count_words)
print('Слогов:', count_syllables)
print('Средняя длина предложения в словах:', ASL)
print('Средняя длина слова в слогах:', ASW)
print('Индекс удобочитаемости Флеша:', FRE)

#НИКИТА ЛЯ ЛЯ ЛЯ