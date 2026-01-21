import random 

r = random.randint(1, 50)
x = 1
num = int(input("Enter a number between 1 and 50: "))

while num != r:    
    x += 1

    if num > r:
        print("That is above the target")
    elif num < r: 
        print("That is below the target")
    else:
        break

    num = int(input("Enter a number between 1 and 50: "))

print("Correct you guessed in", x, "attempts")
        
    
    


