import time



def power_func (a, b) :
    return a ** b

def power_func_bis(a, b) :

    if b == 0 : 
        return 1
    else : 
        return a * power_func_bis(a, b - 1)


start = time.time()


print(power_func_bis(42, 84))
print(power_func_bis(42, 168))

end = time.time()

print("Temps d'exécution récursif : ", end - start)

start2 = time.time()


print(power_func(42, 84))
print(power_func(42, 169))

end2 = time.time()


print("Temps d'exécution non récursif : ", end2 - start2)


