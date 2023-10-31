vector = []
for i in range(8):
    element = float(input(f'Introduceți elementul {i + 1}: '))
    vector.append(element)

# Bubble Sort
n = len(vector)
sorted_vector = vector.copy()  # Creăm o copie a vectorului pentru a păstra originalul intact

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_vector[j] > sorted_vector[j + 1]:
            sorted_vector[j], sorted_vector[j + 1] = sorted_vector[j + 1], sorted_vector[j]

print('Vectorul sortat folosind metoda Bubble Sort:')
print(sorted_vector)

