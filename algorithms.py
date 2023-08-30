from colors import Colors


class Algorithms:
    def __init__(self):
        pass

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