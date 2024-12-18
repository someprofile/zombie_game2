def menu(arg1, *args):

    options = [arg1, *args]
    
    menu_string = ""

    for i in options:
        menu_string += f"{options.index(i) + 1}. {i}\n"
        #print()
    

    while True:
        x = input(menu_string)
        x = x.lower()
        x = x.strip("., ")
        #print(x)
    
    

        
        if x in options:
            print(f"You decided to {x}")
            return x
        else:
            print("That is not one of the commands")



#menu("stab", "use item", "change equipment", "open map", "run")