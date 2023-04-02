numbers = [3,6,2,8,4,10]
largest=numbers[0]
for number in numbers:
    if(number > largest):
        largest = number
print(f"The largest number in list is {largest}")