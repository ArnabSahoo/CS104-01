names = []

for i in range(10):
    acceptedName = input("Enter name: ")
    names.append(acceptedName)

print(names)

while len(names) > 0:
    print(names.pop(0))

print(names)
