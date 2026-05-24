def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
       user_guess = user_input()
       template = build_template(template, word_in_play,user_guess)  
def get_word(w):
    """
    input:w - list with strings(words)
    output:for now:first element in list as string
           TODO: random string from list
    """
    return w[0]
def start_template(w):
    """
    input:w-string(word)
    output:replace all chars in string to '_',
           return replaced chars as string with length w==t
    """
    t = []
    for i in w:
        t.append('_')
    return t
def welcome_speech(t):
    """
    input:t-template(string)
    output:return None,used as just built-in fuction print()
    """
    print (f'''
    dobro pozhalavat v igry - hangman 2000
    vasha zadacha ugadat zagadannoe slovo za neskolko popitok,
    inache vas zhdet rasplata!
    Zagadannoe slovo sostoit iz {len(t)} bukv {t}
    ''')
def list_to_string_convert(t):
    """
    input:t-template(list)
    output:s-list converted to string
    """
    s=''
    return s.join(t) 
def user_input():
    """
    output:return str,built-in input() function
    """
    return input('vvediti bykvy:')

def build_template(t,w,g=''):
    """
    input: t - template (list),w - word (string),g - guess (string)
    output: t - template (list) with replaced characters in template
                if character in word == guess:
                    'character'
                else:
                     '_'
    """
    for i in range(len(w)):
        if w[i] == g:
            t[i]=g
    return t
