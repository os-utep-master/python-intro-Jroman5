import string 
#Reads file, removes punctuation and returns a list of words in alphabetical order, and in lowercase
def fileReader(file):
	text = open(file,"r")
	words = text.read()
	table = words.maketrans("!;',.?:\"-","         ")
	words = words.translate(table)
	seperatedWords = words.split()
	seperatedWords = [element.lower() for element in seperatedWords]
	seperatedWords.sort()
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
	print(wordCount)


#main method
if __name__=="__main__":
    organizedWords=fileReader("speech.txt")
    wordCounter(organizedWords)
