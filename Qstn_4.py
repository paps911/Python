list = []
for i in range (4):
    n = eval(input("Enter a number between 1 and 12: "))
    if n >10:
        n = 10
    list.append(n)
    print(list)
