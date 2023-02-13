#Index - position of item in list
#append - adds a no. to the bottom of the list
#sort - arranges no. in ascending or descending order
#count - counts no. of times an item has been repeated
#pop - removes item from list numbers.remove(45)
#insert
#remove - removes the 1st occurence of a no.
numbers = [45, 67, 34, 76, 23, 90]
# print(numbers.index(67))

# names = ("python","java","c#")
# print(names.index("c#"))
#index - gets the index of an element in list

#before appending
# for i in range(len(numbers)):
    # print(numbers[i])
# print("\n")    
# numbers.append[40]

#after appending
# for i in range(len(numbers)):
#     print(numbers[i])

# print(numbers.pop(2))
# numbers.insert(2, 100)
# for i in range(len(numbers)):
#     print(numbers[i])

numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])