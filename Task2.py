number = input ("Enter 4 digits number: ")

if (len(number) != 4):
    print("Don't mess with me. Just enter a 4 digits number: ") 
else:
    product = int(number[0])*int(number[1])*int(number[2])*int(number[3])
    reverse = int(number[3]),int(number[2]),int(number[1]),int(number[0])
    order = "".join(sorted(str(number)))
    print(product, reverse, order)