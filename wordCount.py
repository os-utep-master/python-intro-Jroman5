import string 
#Reads file and places each word as part of a list
def fileReader(file):
	text = open(file,"r")
	words = text.read()
	table = words.maketrans("!;',.?:\"-","         ")
	words = words.translate(table)
	seperatedWords = words.split()
	for x in seperatedWords:
		print(x)
	text.close()

#main method
if __name__=="__main__":
    fileReader("speech.txt")
