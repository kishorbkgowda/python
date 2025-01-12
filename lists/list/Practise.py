#How do you create a list in Python with the values [1, 2, 3, 4, 5]?
list = [1,2,3,4,5]

#What is the output of the following code?
my_list = [10,20,30,40,50]
print(my_list[2])

# so the output will be 30

#How can you add the value 50 to the end of a list?
my_list.append(50)

#How do you remove the first occurrence of the value 30 from a list?
my_list.remove(30)

#How can you find the length of a list?
print(len(my_list))

#How do you combine two lists [1, 2, 3] and [4, 5, 6] into one list?
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

# What is the result of this slicing operation:
# python
# Copy code
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])
# the answer would be [20,30,40]

#How do you check if the value 25 exists in a list?
print(my_list.__contains__(25))

#Write a program to create a list of numbers and print the largest number in it.
largest_number = [2,1,3,6,5]
largest_number.sort()
print(largest_number[len(largest_number)-1])

#What is the difference between append() and extend() in lists?
#    so append means where the value get added at the last index of the list