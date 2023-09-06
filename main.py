import json
import sys
import random
import os

class tcolors:
    RED = '\033[31m'
    YELLOW = '\033[93m'
    GREEN = '\033[32m'
    CLEAR = '\033[0m'

if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    if arg == '-pt':
        words_file = open('words_pt.json')
        print("Game is loaded in portuguese")
    elif arg == '-en':
        words_file = open('words_en.json')
        print("Game is loaded in english")
    else:
        print(f'Argument {arg} is not supported')
        exit()
else:
    words_file = open('words_pt.json') if input("Choose your language: ('PT' or 'EN'): ") == 'PT' else open('words_en.json') 

words = json.load(words_file)
random_word = words[random.randint(0, len(words))]
tries = 1
print(random_word)
while tries <= 6:
    attempt = input(f'Insert your {tries} attempt: ')
    if len(attempt) == 5:
        if attempt in words:
            answers = []
            correct_letters = [i for i in random_word]
            for index, letter in enumerate(random_word):    
                att = attempt[index]    
                if letter == att:
                    answers.append(2)
                    print(f"{tcolors.GREEN}{att}{tcolors.CLEAR}", end=" ")
                    correct_letters.remove(att)
                elif att in random_word and att in correct_letters:
                    answers.append(1)
                    print(f"{tcolors.YELLOW}{att}{tcolors.CLEAR}", end=" ")
                    correct_letters.remove(att)
                else:
                    answers.append(0)
                    print(f"{tcolors.RED}{att}{tcolors.CLEAR}", end=" ")
            print()
            if 0 not in answers and 1 not in answers:
                print("Congrats!!!")
                exit()
            tries = tries + 1
        else:
            print("Word not in list!")
    else:
        print("Only 5 letter words!")
print(f"You are out of attempts, the answer was {tcolors.GREEN}{random_word}{tcolors.CLEAR}.")
