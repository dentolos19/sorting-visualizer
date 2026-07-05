import colors


def bubble_sort(values):
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            num1 = values[j]
            num2 = values[j + 1]
            if num1 > num2:
                values[j], values[j + 1] = (
                    values[j + 1],
                    values[j],
                )
                yield {j: colors.GREEN, j + 1: colors.RED}
    return values


def insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
        yield {i: colors.GREEN, j + 1: colors.RED}
    return values


def selection_sort(values):
    for i in range(len(values)):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
        yield {i: colors.GREEN, min_index: colors.RED}
    return values


def heap_sort(values):
    n = len(values)

    for i in range(n // 2 - 1, -1, -1):
        yield from _heap_sort_helper(values, n, i)

    for i in range(n - 1, 0, -1):
        values[i], values[0] = values[0], values[i]
        yield {i: colors.GREEN, 0: colors.RED}
        yield from _heap_sort_helper(values, i, 0)

    return values


def _heap_sort_helper(values, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and values[i] < values[left]:
        largest = left

    if right < n and values[largest] < values[right]:
        largest = right

    if largest != i:
        values[i], values[largest] = values[largest], values[i]
        yield {i: colors.GREEN, largest: colors.RED}
        yield from _heap_sort_helper(values, n, largest)


def merge_sort(values):
    yield from _merge_sort(values, 0, len(values) - 1)
    return values


def _merge_sort(values, start, end):
    if start >= end:
        return

    middle = (start + end) // 2
    yield from _merge_sort(values, start, middle)
    yield from _merge_sort(values, middle + 1, end)
    yield from _merge(values, start, middle, end)


def _merge(values, start, middle, end):
    left = values[start : middle + 1]
    right = values[middle + 1 : end + 1]
    left_index = 0
    right_index = 0
    write_index = start

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            source_index = start + left_index
            values[write_index] = left[left_index]
            left_index += 1
        else:
            source_index = middle + 1 + right_index
            values[write_index] = right[right_index]
            right_index += 1

        yield {write_index: colors.GREEN, source_index: colors.RED}
        write_index += 1

    while left_index < len(left):
        source_index = start + left_index
        values[write_index] = left[left_index]
        yield {write_index: colors.GREEN, source_index: colors.RED}
        left_index += 1
        write_index += 1

    while right_index < len(right):
        source_index = middle + 1 + right_index
        values[write_index] = right[right_index]
        yield {write_index: colors.GREEN, source_index: colors.RED}
        right_index += 1
        write_index += 1


def quick_sort(values):
    yield from _quick_sort(values, 0, len(values) - 1)
    return values


def _quick_sort(values, low, high):
    if low >= high:
        return

    pivot_index = yield from _partition(values, low, high)
    yield from _quick_sort(values, low, pivot_index - 1)
    yield from _quick_sort(values, pivot_index + 1, high)


def _partition(values, low, high):
    pivot = values[high]
    smaller_index = low - 1

    for current_index in range(low, high):
        if values[current_index] <= pivot:
            smaller_index += 1
            values[smaller_index], values[current_index] = values[current_index], values[smaller_index]
            yield {smaller_index: colors.GREEN, current_index: colors.RED, high: colors.RED}

    pivot_index = smaller_index + 1
    values[pivot_index], values[high] = values[high], values[pivot_index]
    yield {pivot_index: colors.GREEN, high: colors.RED}
    return pivot_index


def shell_sort(values):
    gap = len(values) // 2

    while gap > 0:
        for i in range(gap, len(values)):
            current_value = values[i]
            j = i

            while j >= gap and values[j - gap] > current_value:
                values[j] = values[j - gap]
                yield {j: colors.GREEN, j - gap: colors.RED}
                j -= gap

            values[j] = current_value
            yield {j: colors.GREEN, i: colors.RED}

        gap //= 2

    return values
