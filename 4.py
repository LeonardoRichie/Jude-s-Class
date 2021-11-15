x = input("enter a name of a text file: ")
y = open(x, "r")
readall = y.read()
z = readall.split() #divide into one word each
for k in range(len(z)-1): #formating by giving \n for every . to make a new line
    if (z[k][-1]) == "." and (z[k+1][0].isupper()) and not ((z[k][-1] == ".") and (z[k][0].isupper()))\
            or (z[k][-1]) == "!" and (z[k+1][0].isupper()) and not ((z[k][-1] == ".") and (z[k][0].isupper()))\
            or (z[k][-1]) == "?" and (z[k+1][0].isupper()) and not ((z[k][-1] == ".") and (z[k][0].isupper())):
        z[k] = z[k].replace(z[k],"{}\n".format(z[k]))
    else:
        z[k] = z[k]. replace(z[k],"{} ".format(z[k]))

y.close()
for a in z: #printing z that has been changed
    print(a, end="")