
list1 = []
list2 = []

with open("input.txt", 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())  # Split line into two numbers and convert to int
        list1.append(num1)
        list2.append(num2)

# list1.sort()
# list2.sort()

# differenceTotal = 0

# for num1, num2 in zip(list1, list2):
#     differenceTotal += abs(num1-num2)

# print(differenceTotal)

similarityScore = 0
for num in list1:
    similarityScore += num * list2.count(num)

print(similarityScore)