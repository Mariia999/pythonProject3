def adder(*n):
    sum = 0

    for i in n:
        sum += i

    print("Sum: ", sum)

adder(4, 2, 8)