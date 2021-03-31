# euler 34

import math

def factoril(num):
    sum = 0
    for j in range(len(num)):
        adad = int(num[j])
        sum += math.factorial(adad)
    return sum
    


list_adad = []

for adad in range(11,1000000):
    adad_1 =str(adad)
    adad_2 = factoril(adad_1)
    if adad_2 == adad:
        list_adad.append(adad_2)
    else:
        continue

hasel = sum(list_adad)
print(hasel)
#print(list_adad)
        