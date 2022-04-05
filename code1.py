list1 = [12,13,34,45,67,890]
list1.sort(reverse=True)
print(list1)
print(list1[0])
#found the largest number in the list in 4 steps
list2 = [23,34,44,12,12,456,457]
max = list2[0]
for number in list2:
    if number > max:
        max = number
print(number)
#method 2 to find the largest number.
number1 = [1, 1, 1, 3, 3, 33, 4, 5, 89, 98]
dup = []
for i in number1:
    if i not in dup:
        dup.append(i)
print(dup)
##### removing the duplicates

















