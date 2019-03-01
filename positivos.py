contador_pares=0;
for a in range(-111100000, 100000000000):
    a=int(input("Ingrese un número"))
    if a%2==0:
         contador_pares=contador_pares+1
    else:
        break

print(contador_pares)



