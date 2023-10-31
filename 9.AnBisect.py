x=int(input('Anul este '))
if(x % 4==0 and x % 100!=0) or (x % 400==0):
    print(f'{x} este an bisect')
else:
    print(f'{x} nu este an bisect')
