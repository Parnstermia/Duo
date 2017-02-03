#!/usr/bin/env python3
def openDictionary(word_list, txt):
    with open(txt) as fil:
        for row in fil:
            words = row.split('\t')
            word_list.append(words[0].strip("\n"))
    return word_list


def includeWords(word_list, old_words_file, newWords):
    counter = 0
    with open(old_words_file, 'a') as f:
        with open(newWords) as new:
            for word in new:
                aux = word.strip("\n")
                if aux not in word_list:
                    word_list.append(aux)
                    f.write(aux)
                    counter = counter + 1

    return counter


def updateDictionary(word_list, old_words_file, new_words_file):
    word_list = openDictionary(word_list, old_words_file)
    number = includeWords(word_list, old_words_file, new_words_file)
    print("There are <" + str(number) + "> new words registered")


Old_words = input("Enter the Old words dictionary :\n------>")
New_words = input("Enter the new words file text  :\n------>")
word_list = []

updateDictionary(word_list, Old_words, New_words)
