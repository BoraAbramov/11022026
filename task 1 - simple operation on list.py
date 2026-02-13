
numbers = [10, 20, 30, 20, 40, 50]

#section 1

i = 0
for number in numbers:
    if number == 20:
        i += 1

print(f"{i} times 20 appears")

#section 2

print(f"number 30 index: {numbers.index(30)}")

#section 3

numbers.append(99)
print(f"number 99 added to end {numbers}")

#section 4

numbers.insert(2, 15)
print(f"number 15 added to index 2 {numbers}")

#section 5

numbers.remove(20)
print(f"number 20 removed {numbers}")

#section 6

numbers.pop(3)
print(f"number from index 3 removed")

#section 7
#section 8
#section 9
#section 10
#section 11
