temp = input('Gimme a number: ')
try:
    temp = float(temp)  
    if temp < 77:
        print("brrr.")
    elif temp >= 77:
        print("hot asf outside")
except ValueError:
    print("Wrong input tubby.")
    
    

