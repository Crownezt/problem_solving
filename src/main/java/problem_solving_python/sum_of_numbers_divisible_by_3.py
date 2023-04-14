if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for number in numbers:
        if numbers[number - 1] % 3 == 0:
            total += numbers[number - 1]
    print(total)
