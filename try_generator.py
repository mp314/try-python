def fibonacci_numbers(nums):
    value_a, value_b = 0, 1
    for _ in range(nums):
        value_a, value_b = value_b, value_a+value_b
        yield value_a


nums = 10
f_numbers = fibonacci_numbers(nums)
for _ in range(nums):
    print(next(f_numbers))