def f():
    return (int(input('number: ')) for _ in range(2))
def max(a, b):
    if a > b:
        return a
    return b
print(max(*f()))

