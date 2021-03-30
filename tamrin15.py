# eluer 28

def jam(num):
    var = (num-1)/2
    hasel = (3 + 2 * var * ( 8 * var * var + 15 * var +13)) /3  # formula for calculate
    return hasel


# for print the value
def main():
    diagonal = jam(1001)
    print("%i" % diagonal)


main()




