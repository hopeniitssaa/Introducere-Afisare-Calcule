"""Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
342 243 234 432."""

a=int(input("dati a= "))
b=int(input("dati b= "))
c=int(input("dati c= "))
print( a, "+" ,b,"+" ,c, "=",a + b + c)
print(a, "+" ,c, "+" ,b, "=",a + c + b)
print(c, "+" ,b, "+" ,a, "=",c + b + a)
print(c, "+" ,a, "+" ,b, "=",c + a + b)
print(b, "+" ,a, "+" ,c, "=",b + a + c)
