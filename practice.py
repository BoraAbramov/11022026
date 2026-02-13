import random

grades = []
for i in range(10):
    grades.append(random.randint(0,100))

print(grades)

a = False
for i in grades:
    if i > 90:
        print(True)
        break
print(a)


for i in grades:
    if i > 90:
        print(False)
        break
print(True)
