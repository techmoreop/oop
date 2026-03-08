class parrot:
    s = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot('blu', 10)
wii = parrot('wii', 15)

print('Blu is a ', blu.s)

print('wii is also a ', wii.s)

print('Blu name is', blu.name)

print('Blu age is', blu.age)

print('wii name is', wii.name)

print('wii age is', wii.age)