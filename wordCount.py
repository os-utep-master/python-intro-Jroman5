import string 
#Reads file and places each word as part of a list without punctiation, in alphabetical order, and in lowercase
def fileReader(file):
	text = open(file,"r")
	words = text.read()
	table = words.maketrans("!;',.?:\"-","         ")
	words = words.translate(table)
	seperatedWords = words.split()
	seperatedWords = [element.lower() for element in seperatedWords]
	seperatedWords.sort()
	for x in seperatedWords:
		print(x)
	text.close()

#main method
if __name__=="__main__":
    fileReader("speech.txt")
