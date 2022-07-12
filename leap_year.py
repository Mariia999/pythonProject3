year = int(input("Year "))
if year % 4 != 0:
    print("No")

elif year % 100 == 0:
    if year % 400 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")