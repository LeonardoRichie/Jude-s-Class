import os
os.chdir('C:\\Users\\Richie\\PycharmProjects\\SIRJUDESASSIGNMENT')
inputfile= input("input a text file: ")
x = open(inputfile, "r")
def returnhapax(x):
    readall = x.read()
    x = readall.lower()
    x = x.replace(',', '')
    x = x.replace('.', '')
    x = x.replace('-', ' ')
    mydict = {}
    split = x.split()
    for word in split:
        mydict[word] = mydict.get(word,0)+1
    print("list of hapaxes:")
    for key in mydict:
        if mydict[key] == 1:
            print("-", key)
returnhapax(x)