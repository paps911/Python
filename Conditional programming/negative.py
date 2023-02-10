#ask for input
#check if input is negative
#If negative, tell user wrong input
#If positive check greater than 50
#If greater than 50, divide by 2
#If less than 50, tell user number less than 50
num = eval(input("Number:"))
if num < 0:
    print("Wrong input.")
else :
    print("Number is positive")
    if num > 50 :
        x = num/2
        print(x)
    else :
        print("Number is less than 50")
    



