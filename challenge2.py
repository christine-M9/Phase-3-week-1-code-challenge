def two_positive_integers(numbers):

    positive_count = sum(1 for num in numbers if num > 0)
    return positive_count == 2

input_place = input("Hello, Input the three integers and see the output (e.g. 2, 3, 4): ")
numbers = [int(num) for num in input_place.split(',')]
print(two_positive_integers(numbers))
