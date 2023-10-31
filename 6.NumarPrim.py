def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Introduceți un număr întreg: "))
if is_prime(number):
    print(f"{number} este un număr prim.")
else:
    print(f"{number} nu este un număr prim.")