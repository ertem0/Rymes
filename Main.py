import sys
import os

words_dic = {}

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_new_rymes_key(last_letters, words):
    last_letters = last_letters.capitalize()

    words_dic[last_letters] = []
    for word in words:
        word = word.replace("\n", "")
        
        if last_letters == word[len(word) - len(last_letters):].capitalize():
            words_dic[last_letters].append(word)
    

def get_rymes(last_letters="", directory="Words/wordlist-big-20190329.txt"):


    last_letters = last_letters.capitalize()
    
    if last_letters not in words_dic.keys():
        words_file = open(directory,'r')
        words = words_file.readlines()

        create_new_rymes_key(last_letters, words)

        words_file.close()

    return words_dic[last_letters]

if __name__ == '__main__':
    print("Rimas Sao FIXES (Rataphabio): ")

    while True:
        last_letters = input()
        print(get_rymes(last_letters, resource_path("Words/wordlist-big-20190329.txt")))
        print(len(get_rymes(last_letters, resource_path("Words/wordlist-big-20190329.txt"))), " Palavras")