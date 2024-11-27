def read_file(filename):
    try:
        file = open(filename, 'r')
        data = file.read()
        print("Data:", data)
    except FileNotFoundError:
        print("Error: The file was not found.")
    finally:
        print("Closing the file...")
        file.close()  # Ensures the file is closed, regardless of success or failure

# Let's simulate calling this function with a non-existent file
read_file("non_existent_file.txt")

def numChars(filename):
    '''returns the number of characters in file filename'''
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    return len(content)

def numWords(filename):
    '''returns the number of words in file filename'''
    infile = open(filename)
    content = infile.read()
    infile.close()
    wordList = content.split()
    return len(wordList)

def numLines(filename):
    '''returns the number of lines in file filename'''
    infile = open(filename, 'r')
    lineList = infile.readlines()
    infile.close()
    return len(lineList)