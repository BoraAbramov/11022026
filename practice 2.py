
grades = [90, 75, 100, 55, 90, 60]
#1
print(grades.count(90))
#2
print(grades.index(100))
#3
grades.append(80)
print(grades)
#4
grades.remove(55)
print(grades)
#5
grades.insert(2, 50)
print(grades)
#6
grades.pop(3)
print(grades)
#7
print(max(grades))
#8
print(min(grades))
#9
print(sum(grades))
#A
print(len(grades))
#B
back = grades.copy()
print(back)
#C
grades.clear()
#D
print(grades + back)

