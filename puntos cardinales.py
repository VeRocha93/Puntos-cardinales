x = int(input("Ingresa valor de x:"))
y = int(input("Ingresa valor de y:"))


if x == 0 or y == 0:
    print ("Ingresa un número distinto al origen ")
    
elif x > 0 and y > 0:
    print ("El punto se encuentra en el cuadrante I.")
elif x < 0 and y > 0:
    print ("El punto se encuentra en el cuadrante II.")
elif x < 0 and y < 0:
    print ("El punto se encuentra en el cuadrante III.")
elif x > 0 and y < 0:
    print ("El punto se encuentra en el cuadrante IV")