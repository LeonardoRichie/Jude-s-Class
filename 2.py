x = input("enter a name of a text file: ")
y = open(x, "r")
readall = y.readlines()
number = 0
list = []
for k in readall:
    number = number + 1
    list.append("{}.{}".format(number, k)) #putting the sentence per line in a list
newname = input("Enter a new file name: ")
newfile = open(newname, "w")
for z in list:
    newfile.write(z) #create a new file from the list
print("file created")