with open('day1/input.txt', 'r') as file:
    list1 = []
    list2 = []

    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

total_sum = 0
for num1, num2 in zip(list1, list2):
    total_sum += abs(num1 - num2)

# part 1
print(total_sum)

# part 2
# total_similarity = 0
# for num in list1:
#     total_similarity += num * list2.count(num)
total_similarity = sum([num * list2.count(num) for num in list1])
print(total_similarity)