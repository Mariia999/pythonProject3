class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def __str__(self):
        return 'Phone number - {self.number}; model - {self.model}; weight - {self.weight}' .format(self=self)

    def receiveCall(self, name):
        return f'Dzvinok vid {name}'

    def getNumber(self):
        return self.number


    receiveCall(+380501212121)

    def sendMessage(self):
        return f'{}'

a = Phone("+380501212121", "Iphone 11", "220")
a2 = Phone("+380991414141", "Iphone 12", "250")
a3 = Phone("+380961515151", "Iphone 13", "230")

a.receiveCall = ("Masha")
a.getNumber = ()
a2.receiveCall = ("Pasha")
a2.getNumber = ()
a3.receiveCall = ("Sasha")
a3.getNumber = ()

print(a)
print(a2)
print(a3)


