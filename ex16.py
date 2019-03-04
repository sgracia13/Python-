from sys import argv

#This allows me to insert command line arguments wherever I see fit in the script
#This is the declaration stage
script, filename = argv

#This prints on the screen as a prompt
# The "%r" references the command line argument. In this case it is "filename"
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

#This command gives you a prompt to answer
raw_input("?")

#This prints on the screen
print "Opening the file..."
#This is an action that python takes, in this case its opening a file
target = open (filename, 'w')


print "Truncating the file. Goodbye!"
#Truncating means emptying the file. The file has nothing in it, so it doesnt matter
#This is just an example of what it can do 
target.truncate()

print "Now I'm going to ask you for three lines."


#again, raw_input gives you the option to plug something in.
#You can actually write things in and it will store that info
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

#Again, when using target, you are telling the computer to take action.
#In this case, you are telling the computer to write what the user typed in.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#This is giving the computer the command to close your file.
#Remember what target does! It tells the computer to do what you tell it to do!
print "And finally, we close it."
target.close()