#Tests if the given string is a palindrome or not
def palindrome_test(string):
    if string==string[::-1]:
        return True            
    else:
        return False
run=True
while run==True:
    x=input("Enter a string to test for palindrome or 'exit':")
    if x=="exit":
        print("Thank you for your time.")
        run=False
        break
    else:
        #Takes the input string and converts it into a alphanumeric set
        x=x.lower()
        test_set=  ""
        for c in x:
            if c.isalnum():
                test_set += c
        #Checks wether the given string is palindrome or not    
        print("Is Palindrome:",palindrome_test(test_set))
        
