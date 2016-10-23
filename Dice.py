import random

money = 0

while True:
    dice = random.randrange(1,10,1)

    num = input("Adivina un numero entre 1 y 10 (press q to quit): ")
    
    if num == 'q':
        break
        
    if int(num) == dice:
        print("Adivinaste!")
        money = money + 1
    else:
        print("Sos un choto, era %s" % (dice))

print ('Ganaste %s puntos' % (money)) 
