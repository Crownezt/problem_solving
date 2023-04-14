if __name__ == '__main__':
    arr = [1, 8, 18, 4, 5]
    max_num = arr[0]
    next_max = arr[0]

    for i in arr:
        if i > max_num:
            next_max = max_num
            max_num = i
        if next_max < i < max_num:
            next_max = i
    print(max_num, next_max)
