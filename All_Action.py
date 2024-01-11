f = "sample.txt"

#Open 

with open('sample.txt', 'r') as f:
                    print(f.read())
                    print()
#Read

with open('sample.txt', 'r') as f:
                    content = f.read()  # Reads the entire file
                    line = f.readline()  # Reads a single line
                    lines = f.readlines()  # Reads all lines into a list
print("Content :" ,content)
print("Line",line)
print("Lines" ,lines )

#Write 


