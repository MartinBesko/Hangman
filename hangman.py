import random 
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  
    while ('-' or ' ') in word:
        word = random.choice(words)

    return word.upper()
    

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print('Máš', lives, 'životov a už si použil: ', ''.join(used_letters))   
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Slovo: ', ' '.join(word_list))
        
        user_letter = input('Hádaj: ').upper()
    
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print('Netrafil si.')
        
        elif user_letter in used_letters:
            print(f'Už si použil {user_letter}')

        else:
            print('Toto nie je písmeno.')
    if lives == 0:
        print(f'Zomrel si, sorry. Slovo bolo {word}')
    else:
        print(f'Uhádol si slovo {word} !!')
    
hangman()
