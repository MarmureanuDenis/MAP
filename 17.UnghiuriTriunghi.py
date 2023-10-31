a = float(input("Introduceți primul unghi: "))
b = float(input("Introduceți al doilea unghi: "))
c = float(input("Introduceți al treilea unghi: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print("Cele trei unghiuri pot forma un triunghi.")
    else:
        print("Cele trei unghiuri nu pot forma un triunghi.")
else:
    print("Unghiurile trebuie să fie mai mari decât 0 pentru a forma un triunghi.")