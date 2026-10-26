def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            lifes = check_attempt(lifes)
            print(f'Осталось {lifes} попытки')

        if lifes == 0:
            lose_speech()
            break

        if not progress:
            win_speech()
    
def welcome_speech(t):
    """
    это приветственная функция
    вход: t - шаблон слова
    выход: возращает None, выводит приветствие через print()
    """
    print(f"""
    Добро пожаловать в игру - угадай слово!
    Ваша задача:угадать загаданное слово за несколько попыток
    загаднное слово состоит из {len(t)} букв {t}
    """)

def get_word(w):
    return w[0]

def start_template(w):
    t = []
    for l in w:
        t.append('_')
    return t

def list_to_string_convert(t):
    s = ''
    return s.join(t)

def user_input():
    return input("Введите букву: ")

def build_template(t,w,g = ''):
    for i in range(len(w)):
        if t[i]=='_':
            if w[i]==g:
                t[i]=w[i]
            else:
                t[i]='_'
    return t


def print_result(g):
    print(f'Результат: {g}')

def check_win(g):
    for l in g:
        if l == '_':
            return True
    return False

def check_mistake(w, g):
    flag = False
    for i in w:
        if i == g:
            flag = True
    return flag

def check_attempt(life):
    life = life - 1
    return life

def lose_speech():
    print("Вы проиграли")

def win_speech():
    print("Вы выйграли")

game()




    
