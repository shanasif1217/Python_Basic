numbers = [1,2,3,4,5,5,6,6,7,7,8,9,9]
count= 0
for number in numbers:
    count=numbers.count(number)
    if count > 1:
        numbers.remove(number)
print("Output of First Method")
print(numbers)

#Let's do it using 2 lists
#am gonna declare another list
unique_list = []   #an empty list
for number in numbers:
    if number not in unique_list:
        unique_list.append(number)
print("Output of Second Method")
print(unique_list)