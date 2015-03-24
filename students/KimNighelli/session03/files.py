'''
This is for Task 8 - Files

1) Make a document. Read in the document. Then print every other line of the document.
2) Open and write to a new document
'''

# Question 1: Can I read in a document and print out every other line?

def read_and_print(file):
    f = open(file, 'r')
    for index, line in enumerate(f.readlines()):
        if index % 2 == 0:
            print line.strip()
    

if __name__ == "__main__":
    read_and_print("./files_test1.txt")

