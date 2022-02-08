import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''Bagels, a deductive logic game.
By ZQRey
Я думаю о {NUM_DIGITS}-значном числе без повторяющихся цифр.
Попробуйте угадать, что это такое. Вот некоторые подсказки:
Когда я говорю: Это означает:
Pico Одна цифра правильная, но в неправильном месте.
Fermi Одна цифра правильная и в правильном положении.
Bagels Ни одна цифра не является правильной.

Например, если секретным числом было 248, а вашим предположением было 843,
подсказками будет Fermi Pico.''')

    secretNum = getSecretNum()
    print('Я придумал номер.')
    print(f'У вас есть {MAX_GUESSES} попыток.')

    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f'Попытка #{numGuesses}: ')
            guess = input('> ')
        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1
        if guess == secretNum:
            break  # Правильно, выходим из цикла.
        if numGuesses > MAX_GUESSES:
            print('Ваши попытки закончились.')
            print('Ответ был {}.'.format(secretNum))
            break
        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Хотите продолжить отгадывать? (да или нет)')
        if input('> ').lower().startswith('н'):
            print('Спасибо за игру!')
            break


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    numbers = numbers[:3]
    return numbers

def getClues(guess, secretNum):
     """Возвращает строку с подсказками pico, fermi и bagels
     для полученной на входе пары из догадки и секретного числа."""
     if guess == secretNum:
        return 'Вы ответили верно!'

     clues = []

     for i in range(len(guess)):
        if guess[i] == secretNum[i]:
           # Правильная цифра на правильном месте.
           clues.append('Fermi')
        elif guess[i] in secretNum:
           # Правильная цифра на неправильном месте.
            clues.append('Pico')
     if len(clues) == 0:
        return 'Bagels' # Правильных цифр нет вообще.
     else:
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный
        # порядок ничего не выдавал.
        clues.sort()
     # Склеиваем список подсказок в одно строковое значение.
     return ' '.join(clues)

if __name__ == '__main__':
    main()
