"""Can paths be used for anything other than opening a file?"""
import os
# we can print the current working directory
print "The current working directory is", os.getcwd()
# we can see all the files in that directory
print os.listdir("newdir")
