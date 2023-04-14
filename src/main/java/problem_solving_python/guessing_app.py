if __name__ == '__main__':
    date = 10
    while True:
        d = int(input('Guess my birthday: '))
        if d == date:
            print('Correct guess')
            break
        else:
            print('Incorrect guess')

