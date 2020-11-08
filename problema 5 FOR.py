"""Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură."""
n=eval(input("introduceti n="))
suma=0
for a in range(1,n+1):
    if(a%3==0 and a%5==0):
        suma+=a
print(suma)