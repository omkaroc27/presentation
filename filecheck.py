import os.path
# file to check
file_path = r'sample.txt'
flag = os.path.isfile(file_path)
if flag:
    print(f'The file {file_path} exists')
else:
    print(f'The file {file_path} does not exist')
  


