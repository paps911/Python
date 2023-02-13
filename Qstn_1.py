num = eval(input("List 5 numbers:"))
sum = sum(num)
print("Sum:", sum)
print("Last number:", num[4])
print("Reverse order:", num[::-1])
if (num.count(5)) != 0:
    print("5 present")
else :
    print("5 not present")
print("Number of 5's:", num.count(5))
num2 = num[1:4]
num2.sort()
print("New list:", num2)


