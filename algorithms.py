from colors import colors


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            num1 = list[j]
            num2 = list[j + 1]
            if num1 > num2:
                list[j], list[j + 1] = (
                    list[j + 1],
                    list[j],
                )
                yield {j: colors.GREEN, j + 1: colors.RED}
    return list


def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
        yield {i: colors.GREEN, j + 1: colors.RED}
    return list


def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
        yield {i: colors.GREEN, min_index: colors.RED}
    return list