# Assignment 1

# the letter 'i' is used to store the result of the loop.
user_input = input("Please type in a number.")
result = 
for i in range (1, int(user_input)+1):
    fact = fact * i 
#"fact" is multiplied by every iteration of the loop or "i" in this case
print ("The factorial is:")
print (fact)



# Assignment 2



word = input('Type in a word')

word_rev = reversed(word) #reversed takes input and returns the reverse input
if list(word) == list(word_rev):
    print('True, it is a palindrome')
else:
    print('False, this is not a plindrome')
    



# Assignment 3

number = int(input("Please enter a number"))

for i in range(2, int(number/2)):
    if num % i == 0:
        print("not a prime number")
        
    else:
        print("prime number")



