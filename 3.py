import os
os.chdir('C:\\Users\\Richie\\PycharmProjects\\SIRJUDESASSIGNMENT')
y = input("enter a text file: ")
a = open(y, "r")
readall = a.read()
x = readall.lower()
lengthofwords = len(x) #count how many letters
split = len(x.split()) #count how many words
averagewordlength = lengthofwords / split #average
a.close()
print("the average of word length is {}".format(round(averagewordlength, 2)))
