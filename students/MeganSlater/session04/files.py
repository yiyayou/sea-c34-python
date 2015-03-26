"""Do I have to close every file I open?"""
import io
f = io.open('secrets.txt', encoding-'utf-8')
secret_data = f.read
print "Is this thing still running?"


"""Can I edit the file once I open it?  How?"""
f = io.open('secrets.txt', r+)
f.write("I'm editing this file")
