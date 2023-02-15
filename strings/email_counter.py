email = []
gmail = 0
for i in range(2):
    x = (input("Enter email: "))
    email.append(x)
    if (x[-9:-1]) == "@gmail.com":
        gmail = gmail + 1
        print("Number of gmail:", gmail)
    else:
        print("No gmail")


