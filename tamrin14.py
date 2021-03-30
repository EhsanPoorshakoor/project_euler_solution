# euler 20

multpy = 1
for i in range(1,101):
    multpy *= i
    zarb = str(multpy)


sum = 0
for j in range(len(zarb)):
    sum += int(zarb[j])

print(sum)