def calculate_average(numbers):
    if not numbers:
        return 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("Input list must contain only numbers.")
    return sum(numbers) / len(numbers)