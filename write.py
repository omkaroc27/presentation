person_data = ['Name: Onkar', '\nAddress: 591/5 Plot No 5', '\nCity: Kolhapur']
Data = "onkar"
# writing string and list of lines to a file
fp = open("sample.txt", "w")   #First open file
fp.writelines(person_data)  # Write Data
fp.write(Data)  # Write Data
fp.close()

# opening the file in read mode
fp = open("sample.txt", "r")
print(fp.read())  #Read that Data Through Read method
fp.close()
