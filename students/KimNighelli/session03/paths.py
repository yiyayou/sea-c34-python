import os

'''
This is for Task 8 - Paths

I had a few questions about paths.

1) What is my current absolute path for this file? What's the difference between
basename and dirname? Can OS print out all the files in the current directory?
'''

print "The absolute path to this file is %s" % (os.path.abspath('paths.py'))

print "The directory that this program is housed in is %s" % (os.path.dirname('~/Desktop/CodeFellows/sea-c34-python/students/KimNighelli/session03/paths.py'))

print "The basename of this program is %s" % (os.path.basename('./paths.py'))

# Print all the files in a set directory

print "All the current files in this directory are: "
path = '.' #Current working directory
for file in os.listdir(path):
    print file

'''
It appears that dirname and basename come from the same path, with basename being the last part of the path,
and dirname being the full path of the directory that the object you specify is housed in. 

Output from the print statements:

The absolute path to this file is /Users/knighelli/Desktop/CodeFellows/sea-c34-python/students/KimNighelli/session03/paths.py
The directory that this program is housed in is ~/Desktop/CodeFellows/sea-c34-python/students/KimNighelli/session03
The basename of this program is paths.py
All the current files in this directory are:
    dictionaries.py
    exceptions.py
    files.py
    paths.py

'''
