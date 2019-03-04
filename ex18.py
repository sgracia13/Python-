# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

#ok, that *args is actually pointless. We can just do this
def print_two_again(arg1,arg2):
    print"arg1: %r, arg2: %r" % (arg1,arg2)

#this just takes one argument
def print_one (arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
        print "I got nothin'."


#remember that all this is doing is calling on each definition from above
#the names that are in quotes are being inserted where the %r is in the above definitions
print_two("Sebastian","Gracia")
print_two_again("Sebastian", "Gracia")
print_one("First")
print_none()