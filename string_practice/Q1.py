col = input("Enter a colour: ")
print("Length of colour: ", len(col))
col1 = col[::-1]
print("Colour x10: ", col *10)
print("First letter: ", col[0])
print("First 3 letters: ", col[0:3])
col1 = col[::-1]
print("Colour backwards: ", col1)
if col[6] != 0:
    print("Seventh character: ", col[6])
else:
    print("Not long enough")
print("1st and last letters removed: ", col[1:-1])
print("Caps: ", col.upper())
print("a's replaced with e's: ", col.replace("a", "e"))

