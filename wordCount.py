
#Reads file and places each line as a part of a list
def fileReader(file):
    text = open(file,"r")
    words = text.readlines()
    for x in words:
    	print(x)
    text.close()

#main method
if __name__=="__main__":
    fileReader("speech.txt")
