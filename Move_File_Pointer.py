f = open("sample.txt", "r")

#Seek Function

# move to 11 character
f.seek(11)
# read from 11th character
print(f.read())


#Tell Function :

# read first line
f.readline()
# get current position of file handle
print(f.tell())

