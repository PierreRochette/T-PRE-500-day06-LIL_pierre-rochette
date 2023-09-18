def funA (string, num) :

    compteur = 0

    for char in string :
        if char.islower() == True :
            compteur += 1

    if compteur >= num : 
        return True
    else :
        return False


def funB (string, num) :

    compteur = 0

    for char in string :
        if char.isupper() == True :
            compteur += 1

    if compteur >= num : 
        return True
    else :
        return False

##### LE CODE QUE J'ai proposé au début pour funC :

def funC (string, num) :

    compteur = 0 

    for char in string :
        compteur += 1 

    if compteur >= num : 
        return True 
    else :
        return False
    
#### Une manière plus simple de l'exprimer :

def funC_bis (string, num) :

    if len(string) >= num :
        return True 
    else :
        return False
    
############

def funD (string, num) :

    compteur = 0

    for char in string : 
        if char.isalnum() == False :
            compteur += 1

    if compteur >= num :
        return True 
    else :
        return False
    

def funE (string, num) :

    compteur = 0 

    for char in string :
        if char.isnumeric() == True :
            compteur += 1 

    if compteur >= num :
        return True
    else :
        return False 
    
###### TASK 01 ########

lower = funA
special = funD 

def check_password2 (func, num, string) :

    return func(string, num)


print(check_password2(lower, 4, "mysecretpassword"))
print(check_password2(special, 2, "mysecretpassword"))
print(check_password2(lower, ziz, "mysecretpassword"))