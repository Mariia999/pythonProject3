def nd(n):
    i = 1
    a = []
    while i * i <= n:
        if n % i == 0:
            if i == n//i:
                a.append(i)
            else:
                a.append(i)
                a.append(n//i)
        i += 1
    a.sort()
    print("Nunbers_of_elements: ", len(a))

nd(4)
