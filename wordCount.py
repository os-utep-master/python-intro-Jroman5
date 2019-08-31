import sys
import string 
import re
import os
textInput =""
textOutput =""

def fileFinder():
	global textInput
	global textOutput
	if len(sys.argv) is not 3:
		print("Correct usage: wordCount.py <input text file> <output file>")
		exit()
	textInput = sys.argv[1]
	textOutput = sys.argv[2]
	if not os.path.exists(textInput):
		print("text file input %s doesn't exist! Exiting" %textInput)
		exit()


#Reads file, removes punctuation and returns a list of words in alphabetical order, and in lowercase
def fileReader(file):
	try:
		text = open(file,"r")
		words = text.read()
		pattern = "[\"!?;:,.-]"
		#table = words.maketrans("!;',.?:\"-","         ")
		#words = words.translate(table)
		words = re.sub(pattern," ",words)
		seperatedWords = words.split()
		seperatedWords = [element.lower() for element in seperatedWords]
		seperatedWords.sort()
	finally:
		text.close()
	return seperatedWords

#Takes a list of words and places them in a dictionary with the word as a key and the occurrences as its value
def wordCounter(words):
	wordCount = {}
	for x in words:
		if(x in wordCount):
			wordCount[x] = wordCount[x] + 1
		else:
			wordCount[x] = 1
	return wordCount

#Writes the counted words to a file 
def fileWriter(countedWords):
	try:
		file = open(textOutput,"w+")
		for x in countedWords:
			file.write(x + " " + str(countedWords[x]) + "\n")
	finally:
		file.close()




#main method
if __name__=="__main__":
	fileFinder()
	organizedWords=fileReader(textInput)
	fileWriter(wordCounter(organizedWords))
