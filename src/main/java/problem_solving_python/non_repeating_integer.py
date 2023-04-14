def find_first_unique(numbers):
    for i in range(0, len(numbers), 1):
        unique = False
        for j in range(i+1, len(numbers), 1):
            if numbers[i] == numbers[j]:
                exists = True
        if not unique:
            return numbers[i]


def find_all_unique(numbers):
    number = []
    for i in range(0, len(numbers), 1):
        exists = False
        for j in range(i+1, len(numbers), 1):
            if numbers[i] == numbers[j]:
                exists = True
                number.append(numbers[i])
        if not exists:
            return number


if __name__ == '__main__':
    arr = [1, 2, 4, 3, 4, 5, 6, 2, 1]
    print(find_first_unique(arr))
    print(find_all_unique(arr))
