"""
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths
of the word tokens in the text, divided by the number of word tokens). [open http://www.gutenberg.org/ and download an
e-book as plain text, use the file for texting your program]
"""

y = input("enter a text file: ")
a = open(y, "r")
readall = a.read()
x = readall.lower()
lengthofwords = len(x) #count how many letters
split = len(x.split()) #count how many words
averagewordlength = lengthofwords / split #average
a.close()
print("the average of word length is {}".format(round(averagewordlength, 2)))
