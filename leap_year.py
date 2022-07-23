def y(a):

    if a % 4 != 0:
        print("No")
    elif a % 100 == 0:
        if a % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")


y(2000)