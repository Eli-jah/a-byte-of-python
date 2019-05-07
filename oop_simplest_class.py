class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

    pass  # An empty block


person = Person('Elijah Wang')
# print(person)
person.say_hi()
