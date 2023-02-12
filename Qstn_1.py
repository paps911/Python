num = eval(input("List 5 numbers:"))
sum = sum(num)
print("Sum:", sum)
print("Last number:", num[4])
print("Reverse order:", num[::-1])
if (num.count(5)) != 0:
    print("Yes")
else :
    print("No")
print("Number of 5's:", num.count(5))
num2 = num[1:4]
num3 = num2.sorted
print("New list:", num3)


