# euler 30

def jam(number):
    sum_num = 0
    for j in range(len(number)):
        sum_num += int(number[j]).__pow__(5)
    return sum_num


list_adad = []

for i in range(2,1000000):
    adad = str(i)
    hasel = jam(adad)
    if hasel == i:
        list_adad.append(int(hasel))

#print(list_adad)
print("answer is %i" % sum(list_adad))











#def compute():
	# As stated in the problem, 1 = 1^5 is excluded.
	# If a number has at least n >= 7 digits, then even if every digit is 9,
	# n * 9^5 is still less than the number (which is at least 10^n).
	#ans = sum(i for i in range(2, 1000000) if i == fifth_power_digit_sum(i))
	#return str(ans)


#def fifth_power_digit_sum(n):
	#return sum(int(c)**5 for c in str(n))


#if __name__ == "__main__":
	#print(compute())