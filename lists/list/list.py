fruits = ["Apples","Bananas","Oranges",1,2,3]
arr = [5,2,3,6,4]
# so you can change the values in the lists,so hence in lists are mutable
fruits[1] = "Grapes"
print(fruits)

# Lists Slicing
print(fruits[1:4])

# List length printing
print(len(fruits))

# adding value 
fruits.append("Kunni")

#sort the list
arr.sort()
print(arr)

#reverse the list
fruits.reverse()

#adding the values in the preferred index
fruits.insert(2,"Mango")

fruits.pop(2)

fruits.remove("Oranges")
print(fruits)



