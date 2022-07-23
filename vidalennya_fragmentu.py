def f():
    x = 'kflghdlk sdlk h lk hlkfh kldhyoikjk'
    x = x[:x.find('h')] + x[x.rfind('h') + 1:]
    print(x)


f()