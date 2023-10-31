n = int(input("Introduceți numărul de termeni Fibonacci pe care doriți să îi afișați: "))

a = 0
b = 1

if n <= 0:
    print("Introduceți un număr pozitiv.")
elif n == 1:
    print("Seria Fibonacci cu 1 termen este: 0")
else:
    print("Seria Fibonacci este:")
    print(a)
    print(b)

    for n in range(2, n):
        c = a + b
        print(c)
        a, b = b, c