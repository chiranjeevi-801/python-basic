l1= []

l1.append(1)
l1.append(1.5)
l1.append('python')
print(l1[0])


help()

import array

arr=array.array('i',[1,2,3,4,5])
print(arr)
arr[0]=10
print(arr)



#----------------------------------------------------------------------------------------------------------------

## EXAMPLE 1

# A list of numbers
numbers = [10, 20, 30, 40, 50]

# Access elements
print(numbers[0])  # 10
print(numbers[3])  # 40


# Add a new element
numbers.append(60)
print(numbers)  # array('i', [10, 20, 30, 40, 50, 60])

# Loop through the array
for num in numbers:
    print(num)

#-----------------------------------------------------------------------------------------------------------------

# EXAMPLE 2
# 2D array (like a matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element in row 2, column 3
print(matrix[1][2])  # 6

# Loop through rows
for row in matrix:
    print(row)


#-----------------------------------------------------------------------------------------------------------------
## EXAPLE 3


fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[1])  # banana

# Add a new element
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Remove an element
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'orange']


#-----------------------------------------------------------------------------------------------------------------
# EXAMPLE 4

import array

# Array of integers
numbers = array.array('i', [1, 2, 3, 4, 5])

# Access elements
print(numbers[2])  # 3

# Add a new element
numbers.append(6)
print(numbers)  # array('i', [1, 2, 3, 4, 5, 6])

# Remove an element
numbers.pop(1)  # remove element at index 1
print(numbers)  # array('i', [1, 3, 4, 5, 6])
