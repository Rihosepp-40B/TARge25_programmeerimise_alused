numbers = [1, 2, 3, 4, 5]

another_numbers = numbers

separate_numbers = numbers[:]

def plus_one(numbers: list[int]):
    for i in range(len(numbers)):
        numbers[i] += 1

print(numbers)
plus_one(numbers)
print(numbers)


print(numbers)   # 5, 2, 3
print(another_numbers)
print(separate_numbers)