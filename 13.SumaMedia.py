numere=input('Introduceti lista de numere separata prin spatiu ')
numere=numere.split() #Separam numerele prin spatiu
numere = [float(num) for num in numere]
suma=sum(numere)
media=suma/len(numere)

print(f'Suma numerelor este: {suma}')
print(f'Media numerelor este: {media}')