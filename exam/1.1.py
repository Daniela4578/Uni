import random

def my_input(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if not low < number < high:
                raise ValueError("Invalid number! n should be between 20 and 80")
            else:
                return number
        except ValueError as e:
            print(e)


def count_3(list):
    count = 0
    for j in range(len(list)):

        numC = int(list[j] / 100)
        if numC % 3 == 0 and numC != 0:
            count += 1
        else:
            continue
    return count

def max_negative(list):
    maxN = -800
    for j in range(len(list)):
        if list[j] < 0:
            if list[j] > maxN:
                maxN = list[j]
            else:
                continue
        else:
            continue
    return maxN


def min_positive(list):
    minP = 1000
    for j in range(len(list)):
        if list[j] > 0:
            if list[j] < minP:
                minP = list[j]
            else:
                continue
        else:
            continue
    return minP


def average_even(newlist):
    if len(newlist) < 1:
        raise Exception("List2 is empty!")
    count = 0
    sum = 0
    for j in range(2, len(newlist), 1):
        sum += newlist[j]
        count += 1
    if count > 0:
        average = sum // count
        return average
    else:
         return "0"


def negative_2(newlist):
    if len(newlist) < 1:
        raise Exception("List2 is empty!")
    negel = []
    for j in range(len(newlist)):
        if len(newlist[j]) == 2 and newlist[j] < 0:
            negel.append(newlist[j])
        else:
            continue
    return negel


def delete_max_negative(newlist):
    if len(newlist) < 1:
        raise Exception("List2 is empty!")
    maxN = -800
    for j in range(len(newlist)):
        if newlist[j] > maxN:
            maxN = newlist[j]
        else:
            continue
    return maxN


n = my_input("n = ", 20, 80)

list1 = []

# INPUT FROM PERSON
# for i in range(n):
# #     num = int(input("number = "))
# #     if -800 < num < 1000:
# #         list1.append(num)
# #     else:
# #         print("Number should be between -800 and 1000")
# #     i -= 1

#INPUT BY CP
for i in range(n):
    list1.append(random.randint(-800,1000))

print(list1)
print(f"count of elements: {count_3(list1)}")
print(f"max negative element: {max_negative(list1)}")
print(f"min positive: {min_positive(list1)}")

list2 = []
for k in range(len(list1)):
    if list1[k] % 7 == 0 and list1[k] % 2 != 0:
        list2.append(list1[k])
    else:
        continue

print(list2)
print(f"average even position: {average_even(list2)}")
print(f"max negative elament of list2: {delete_max_negative(list2)}")
list2.remove(delete_max_negative(list2))
print(list2)


for i in range(1,10, 2):
    print(i, end="")