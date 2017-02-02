#!/usr/bin/env python3
def openDictionary(dictionary,txt):
	with open(txt) as fil:
		for row in fil:
			words = row.split(" ")
			if len(words) > 1:
				dictionary[words[0]] = words[1]
			else:
				dictionary[words[0]] = ""
	return dictionary

def includeWords(old_words_file,old_dict,newWords):
	counter = 0;
	f = open(old_words_file,'a')

	with open(newWords) as new:
		for word in new:
			if word not in old_dict:
				old_dict[word] = ""
				f.write(word + "\n")
				counter = counter + 1

	f.close()

	return counter			

def updateDictionary(old_words_file, new_words_file ,dictionary):
	dictionary = openDictionary(dictionary,old_words_file)
	number = includeWords(old_words_file, dictionary, new_words_file)
	print("There are <" + str(number) + "> new words registered")


Old_words = input("Enter the Old words dictionary      :\n")
New_words = input("Enter the new words file text       :\n")
dictionary = {'none': "default"}

updateDictionary(Old_words,New_words,dictionary)