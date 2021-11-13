import random
import datetime


def insertion(given_list):
    new_list = given_list
    for i in range(1, len(new_list)):
        for j in range(i, 0, -1):
            if new_list[j - 1] > new_list[j]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list


def merge_sort(given_list):
    left_list = given_list[0: (len(given_list) // 2)]
    right_list = given_list[(len(given_list) // 2): len(given_list)]
    left_list = insertion(left_list)
    right_list = insertion(right_list)
    a = merge(left_list, right_list)
    return a


def merge(left, right):
    i = 0
    j = 0
    new_list = []
    while (i < len(left)) and (j < len(right)):
        if right[j] > left[i]:
            new_list.append(left[i])
            i = i + 1
        else:
            new_list.append(right[j])
            j = j + 1
    if i > j:
        for x in range(j, len(right)):
            new_list.append(right[x])
    else:
        for x in range(i, len(left)):
            new_list.append(left[x])
    return new_list


a = []
for i in range(9999):
    x = random.randint(0, 100)
    a.append(x)
begin = datetime.datetime.now()
print(merge_sort(a))
end = datetime.datetime.now()
print(end - begin)
