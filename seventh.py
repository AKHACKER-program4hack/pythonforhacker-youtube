num = 2
num2 = int(input("num2> "))

if num > num2:
    print(str(num) + " is greater than " + str(num2))
elif num < num2:
    print(str(num) + " is not greater than " + str(num2))
elif num == num2:
    print(str(num) +" = " + str(num2))
elif num2 / num == 2:
    print("num2 / num")
else:
    print("else statment exec")

print(num2 / num)