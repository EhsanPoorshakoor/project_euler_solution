# euler 29   a**b

import math

list_adad = []
list_nahayi = []

for a in range(2,101):
    for b in range(2,101):
        hasel = a.__pow__(b)
        #print("hasel is %i , a = %i , b = %i" %(hasel , a , b))
        list_adad.append(hasel)

list_nahayi = sorted(list_adad)
answer = list(dict.fromkeys(list_nahayi)) #remove duplicate parameters

print(len(answer))

