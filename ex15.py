from sys import argv

script, filename = argv

#open file filename
txt = open(filename)

print "Here's your file %r: " % filename
# read file and display the content on screen
print txt.read()

txt.close()

print "Type the filename again:"
# request file name
file_again = raw_input("> ")
#open file
text_again = open(file_again)
#read and display it
print text_again.read()

text_again.close()