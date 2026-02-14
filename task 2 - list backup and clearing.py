
grades = [85, 90, 78, 92, 88]

# section 1 + 2

grades2 = grades.copy()
grades.clear()

#section 3

print(f"grades list {grades}")
print(f"grades2 list {grades2}")

#section 4

numbers = [95, 100]

print(f"grades2 + jbl {grades2 + numbers}")

grades2.extend(numbers)
print(f"grades2 extend {grades2}")