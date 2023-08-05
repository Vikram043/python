def sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average

numbers = [10, 20, 30, 40]
total_sum, average = sum_and_average(numbers)
print(f"Sum: {total_sum}, Average: {average}")
