import random
import os
os.system("cls")

def vocal_problem(string):

    string = string.upper()
    vowels = (('Á','A'),('É','E'),('Í','I'),('Ó','O'),('Ú','U'))
    for a,b in vowels:
        string = string.replace(a,b)
    return string

def run():

    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        words = [line.upper() for line in f]

    random_word = random.choice(words).strip('\n')
    l = len(random_word)
    word = list(random_word)

    wmark_word = vocal_problem(random_word) 
    wmark_list = list(wmark_word) 
  
    empty_word = ['_' for j in range(l)]
    word_str = " ".join(empty_word)

    key = True

    while key:

        print('¡Adivina la palabra!')
        print(word_str)
        letter = vocal_problem(input('\nIngrese una letra: ').upper())

        try:
            if len(letter) != 1 or letter.isnumeric():
                raise ValueError('Solo ingrese una letra, y de tipo no númerico')

            if wmark_list.count(letter) != 0:
                i = wmark_list.count(letter)
                while i != 0:
                    index_letter = wmark_list.index(letter)
                    wmark_list[index_letter] = None
                    empty_word[index_letter] = word[index_letter]
                    word_str = " ".join(empty_word)
                    i-=1

            if empty_word.count('_') == 0:
                key = False

        except ValueError as ve:    
            os.system('cls')
            print(ve)
            continue

        os.system("cls")
    
    print(f'¡Ganaste! La palabra era {random_word}')

if __name__=='__main__':
    run()
