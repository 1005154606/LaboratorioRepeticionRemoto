
contadorPos=0
contadorNeg=0
contadorCeros=0


for x in range(1,11):
    x=int(input("Ingrese el número: "))
    if x>0:
        contadorPos=contadorPos+1
    elif x<0:
        contadorNeg=contadorNeg+1

    else:
        contadorCeros=contadorCeros+1

print("Los número positivos son", contadorPos)
print("Los números negativos son", contadorNeg)
print("Hay",contadorCeros,"ceros")











