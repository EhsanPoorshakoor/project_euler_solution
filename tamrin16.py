# euler 48

import math

sum_number = 0
for i in range(1,1001):
    sum_number += i.__pow__(i)
    hasel = str(sum_number)

print(hasel[-10:])

