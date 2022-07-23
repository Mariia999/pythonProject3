def nc():
    x = [0,1,2,3,4,5,8,101,9,10,11]
    max = x[0]
    for i in range(1,len(x)):
        if x[i] > max:
            max =x[i]
    print(max)


nc()