import string 
import re
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
		file = open("countedWords.txt","w+")
		for x in countedWords:
			file.write(x + " " + str(countedWords[x]) + "\n")
	finally:
		file.close()




#main method
if __name__=="__main__":
    organizedWords=fileReader("speech.txt")
    fileWriter(wordCounter(organizedWords))
