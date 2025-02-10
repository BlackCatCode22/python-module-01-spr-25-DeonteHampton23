num1 = input("Enter First Number:")
num2 = input("Enter Second Number:")
num3 = input("Enter Third Number:")
if num1 != num2 and num1 != num3 and num2 != num3: 
    if num1 > num2 and num1 > num3 : 
        largNum = num1
    elif num2 > num1 and num2 > num3 :
     largNum = num2
    else :
     largNum = num3 
    print("The largest Number is:", largNum)

else :
    print("All numbers must be differnt!")
