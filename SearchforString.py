with open(r"sample.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'is' in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
         
