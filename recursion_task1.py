def is_palindrome(phrase) :
    
    if len(phrase) < 1 :
        return True
    else :
        if phrase[0] == phrase[-1] :
            is_palindrome(phrase[1:-1])
            return True
        else :
            return False 
        

phrase = str(input("Enter a string : ")).lower()

if is_palindrome(phrase) == True :
    print("Palindrome")
else :
    print("Not Palindrome")

