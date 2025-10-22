# Part 2: 
# sets

# rainfall_data = {120, 150, 180, 120, 90, 110, 130}

'''
# Q1: How many rainfall values are in the set?
print(len(rainfall_data))

'''

'''
#Q2: Can you directly change the value of an item in a set?

rainfall_data [2] = 200
print(rainfall_data)

## set cannot be change, 
# because every values will be in unordered place we cannot change the values

'''

'''
# Q3: Check if 150 is present inside rainfall_data:
print(150 in rainfall_data)

'''

'''
#Q4: Convert the set to a list
temp = list(rainfall_data)
print(type(temp))

'''

'''
#Q5: Print every rainfall value by traversing the set:

for rain in rainfall_data:
    print(rain)

'''

'''
#Q6: Remove the value 120 from the set:

rainfall_data.remove(120)
print(rainfall_data)
'''

'''
#Q7: Add the value 110 and observe:
rainfall_data.add(110)
print(rainfall_data)

'''

#Part 2: Joining Multiple Sets

rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
'''
Q1: Print all unique rainfall measurements for Chennai and Madurai:

unique_chennai_madurai = rainfall_chennai | rainfall_madurai
print(unique_chennai_madurai)

Q2: Merge all three readings using update() and union():

# Merge all three
all_rainfall = rainfall_chennai.copy()
all_rainfall.update(rainfall_madurai, rainfall_coimbatore)
print(all_rainfall)

all_rainfall_union = rainfall_chennai.union(rainfall_madurai, rainfall_coimbatore)
print(all_rainfall_union)

Q3: Common Rainfall (present in all three cities):

# Common rainfall
print(rainfall_chennai & rainfall_madurai & rainfall_coimbatore)

Q4 Unique Chennai rainfall:

print(rainfall_chennai - (rainfall_madurai | rainfall_coimbatore))

Q5: Rainfall in at least two cities
print((rainfall_chennai & rainfall_madurai) | (rainfall_chennai & rainfall_coimbatore) | (rainfall_madurai & rainfall_coimbatore))

Q6: Increase rainfall by 10
print({rain + 10 for rain in rainfall_chennai})

part 3

#Q1:  Delete set
del rainfall_coimbatore

Q2: Clear rainfall_chennai
rainfall_chennai.clear()
print(rainfall_chennai)

'''