if __name__ == '__main__':

    x = [1, 3, 4, 5]
    y = [2, 6, 7, 8]

    new_arr = x + y
    print(new_arr)

    for i in range(0, len(new_arr) - 1, 1):
        for j in range(0, len(new_arr) - i - 1, 1):
            if new_arr[j] > new_arr[j + 1]:
                temp = new_arr[j]
                new_arr[j] = new_arr[j + 1]
                new_arr[j + 1] = temp
    print(new_arr)
