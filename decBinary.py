decimal = int(input("Enter a number greater than or equal to 0: "))
while decimal < 0:
    print("Invalid, try again")
    decimal = int(input("Enter a number greater than or equal to 0: "))

remainder = decimal % 2
catStr = str(remainder)
print("{} % 2 = {} --- {}" .format(decimal, remainder, catStr))
whole = decimal // 2
print("{} / 2 = {}" .format(decimal, whole))


while whole != 0:
    remainderF = whole % 2
    remainStr = str(remainderF)
    catStr = remainStr + catStr    
    print("{} % 2 = {} --- {}" .format(whole, remainderF, catStr))
    save = whole
    whole = whole // 2
    print("{} / 2 = {}" .format(save, whole))    

    
print(" ")
    
print("{} in binary is {}" .format(decimal, catStr))
