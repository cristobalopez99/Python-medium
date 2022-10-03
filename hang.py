import os 
import random 

def draw_again_word(word, guessed_letters):
    os.system('clear')
    for letter in range(0, len(word) -1):
        if guessed_letters(letter) == True:
            print(word(letter), " ", end='')
        else:
            print("_ ", end='')

def guessed_word(guessed_letters):
    guessed_word = True
    for status in guessed_letters:
        if status == False:
            guessed_word = False
    return guessed_word


def mark_guessed_letters(letter, word, guessed_letters):
    if len(guessed_letters) > 0:
        for posible_letter in range(0, len(word) -1):
            if word(posible_letter) == letter:
                guessed_letters[posible_letter] = True
    else: 
        guessed_letters = [word[posible_letter] == letter for posible_letter in range(0, len(word) -1)]
    draw_again_word(word, guessed_letters)
    return guessed_letters

def draw_spaces_word(words):
    number_random = random.randint(1, len(words) +1)
    word_selected = words[number_random] 
    for i in range(1, len(word_selected)):
        print(" _", end='')
    print("")
    return word_selected

def read_file():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word)
    return words

def run():
    word_selected = draw_spaces_word(read_file())
    guessed_letters = []
    status_word = False
    while status_word == False:
        letter = input('Please type a letter: ')
        guessed_letters = mark_guessed_letters(letter, word_selected, guessed_letters)
        status_word = guessed_word(guessed_letters)
        if status_word == True:
            print('\nCongratulations!! you have won the game, the word is: ', word_selected)
            break
        else:
            print('\nTry again')

if __name__ == '__main__':
    run()            

                                 