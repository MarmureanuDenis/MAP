numere=input('Introduceti lista de numere separata prin spatiu ')
numere=numere.split() #Separam numerele prin spatiu
numere = [float(num) for num in numere] #Convertim numerele in valori float

minim=min(numere)
maxim=max(numere)

print(f'Cel mai mic numar este {minim}')
print(f'Cel mai mare numar este {maxim}')