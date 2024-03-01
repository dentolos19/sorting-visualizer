import colors


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


def heap_sort(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1):
        yield from heap_sort_helper(list, n, i)

    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        yield {i: colors.GREEN, 0: colors.RED}
        yield from heap_sort_helper(list, i, 0)

    return list


# definitions below are helper functions for the algorithms above


def heap_sort_helper(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[i] < list[left]:
        largest = left

    if right < n and list[largest] < list[right]:
        largest = right

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        yield {i: colors.GREEN, largest: colors.RED}
        yield from heap_sort_helper(list, n, largest)