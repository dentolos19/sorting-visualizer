from colors import Colors


class Algorithms:
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
                    yield {j: Colors.GREEN, j + 1: Colors.RED}
        return list

    def insertion_sort(list):
        for i in range(1, len(list)):
            key = list[i]
            j = i - 1
            while j >= 0 and key < list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = key
            yield {i: Colors.GREEN, j + 1: Colors.RED}
        return list