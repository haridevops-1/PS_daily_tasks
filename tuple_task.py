# Part 1: Tuples

# Activity 1: Tuples Basics
# Given the tuple: fruits = ("apple", "banana", "cherry", "mango", "banana")
'''
# fruits = ("apple", "banana", "cherry", "mango", "banana")
# print(len(fruits))
'''

'''
fruits = ("apple", "banana", "cherry", "mango", "banana")
output = fruits.find("banana")
print(output)
'''
'''
fruits = ("apple", "banana", "cherry", "mango", "banana")
fruits[2] = "grape"
print(fruits)
'''

'''
'tuple' object does not support item assignment - 
It is mutable, so it cannot modify, but we can change into list and can modify
'''

'''
fruits =  ("apple", "banana", "cherry", "mango", "banana")
changing = list(fruits)
changing[2] = "grapes"
fruits = tuple(changing)
print(fruits)
'''

# Activity 2: Tuples Grouping


'''
 (1) colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
print(art)
'''

'''
# (2)
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
repeat_color = colors * 3
print(repeat_color)
'''
# (3)
'''
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
middle = art[len(art)//2]   
print(middle)
'''

# (4)
'''
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
print("square exist in art?", "square" in art)
'''

# Activity 3: Tuple Operations

marks = (78, 85, 69, 90, 85)
'''
#(i) checking highest and lowest marks

highest = max(marks)
lowest = min(marks)
print("Highest mark is:", highest)
print("Lowest mark is:", lowest)

'''

'''
#(ii)counting marks 85
count = marks.count(85)
print("Number of marks occuring 85 is: ", count)

'''
'''

(iii)
average = sum(marks) /  len(marks)
print("Average marks:", average)
'''

# Activity 4: Rainfall Data:

# The monthly_rainfall tuple provides the rainfall in millimeters for each month from January to December:

# Calculate the total annual rainfall.
# Determine the average monthly rainfall.
# Identify the month(s) with exactly 120 mm of rainfall. (Hint: Consider using enumerate() or .count().)
# Find the highest and lowest rainfall values recorded.


monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
'''
(i) Total annual rainfall

total_rainfall = sum(monthly_rainfall)
print("Total annual rainfall:", total_rainfall, "mm")
'''

'''
(ii) Average monthly rainfall

average_rainfall = sum(monthly_rainfall) / len (monthly_rainfall)
print("The average monthly rainfall is: ", average_rainfall )

'''

'''
(iii) Months with exactly 120 mm

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
rain_120_months = [months[i]
 for i, rain in enumerate(monthly_rainfall) if rain == 120]
print("Months with 120 mm rainfall:", rain_120_months)


'''

'''
(iv) Highest and lowest rainfall

highest = max(monthly_rainfall)
lowest = min(monthly_rainfall)
print("Highest rainfall:", highest, "mm")
print("Lowest rainfall:", lowest, "mm")

'''