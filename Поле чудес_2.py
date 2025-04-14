word = "автомобиль"
guesd = []
attempts = 7
print("Добро пожаловать в игру 'Поле чудес!'")
print("Сегодня у нас на кону замечательные призы!")
while attempts > 0:
    print("\nУгадайте слово, которое состоит из " + str(len(word)) + " букв.")
    current = ''
    for i in word:
        if i in guesd:
            current += i
        else:
            current += '_'
    print("Слово: ", current)
    letter = input("Введите букву: ").lower()
    if len(letter) != 1 or not ('а' <= letter <= 'я' or letter == 'ё'):
        print("Пожалуйста, введите одну русскую букву.")
        continue
    if letter in guesd:
        print("Вы уже называли эту букву. Попробуйте другую.")
        continue
    guesd.append(letter)
    if letter in word:
        print("Поздравляем! Буква '" + letter + "' есть в слове.")
    else:
        attempts -= 1
        print("К сожалению, буквы '" + letter + "' нет в слове. Осталось попыток: " + str(attempts))
    word_guessed = True
    for i in word:
        if i not in guesd:
            word_guessed = False
            break
    if word_guessed:
        print("ДА ЛАДНО! Вы выиграли: '" + word + "'")
        break
else:
    print("Вы проиграли! Загаданное слово было: '" + word + "'")
