def sandwich(a, veg) :

    i = 0 
    index = 1

    if veg == None or veg == "Non" :

        while i < a : 
            print(index)
            print( " <////////// > " )
            print ( " ~~~~~~~~~~~~ " )
            print ( " O O O O O O " )
            print ( " ============ " )
            print ( " ============ " )
            print( " <////////// > " )
            i+= 1
            index += 1

    else :

        while i < a : 
            print(index)
            print( " <////////// > " )
            print ( " ~~~~~~~~~~~~ " )
            print ( " O O O O O O " )
            print ( " VEGE STEAK " )
            print ( " VEGE STEAK " )
            print( " <////////// > " )
            i+= 1
            index += 1


    return None

sandwich(2, None)
sandwich (3, "Non")
sandwich (4, "Oui")