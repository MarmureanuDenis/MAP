def cmmdc(m,n):
    while m!=n:
        if m>n: m=m-n
        else: n=n-m
    return m
m=int(input('m='))
n=int(input('n='))
print('cmmdc=', cmmdc(m,n))
print('cmmmc=', str(m*n//cmmdc(m,n)))
      