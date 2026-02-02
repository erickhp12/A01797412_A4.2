"""
Compute Statistics Program

This program computes descriptive statistics (mean, median, mode,
standard deviation, and variance) from a file containing numbers.

Usage: python computeStatistics.py fileWithData.txt
"""

import sys
import time


def read_numbers_from_file(filename):
    """Read numbers from a file, handling invalid data."""
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                number = float(line)
                numbers.append(number)
            except ValueError:
                print(f"Error: Invalid data '{line}' at line {line_num}. Skipping.")
    return numbers


def calculate_mean(numbers):
    """Calculate the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return None
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = 0
    for count in frequency.values():
        max_count = max(max_count, count)
    if max_count == 1:
        return "N/A"
    modes = []
    for num, count in frequency.items():
        if count == max_count:
            modes.append(num)
    if len(modes) == 1:
        return modes[0]
    return modes[0]


def calculate_variance(numbers, mean):
    """Calculate the variance of a list of numbers."""
    if len(numbers) < 2:
        return 0
    sum_squared_diff = 0
    for num in numbers:
        diff = num - mean
        sum_squared_diff += diff * diff
    return sum_squared_diff / (len(numbers) - 1)


def calculate_std_deviation(variance):
    """Calculate the standard deviation from variance."""
    if variance < 0:
        return 0
    result = variance
    if result == 0:
        return 0
    guess = result / 2
    for _ in range(100):
        new_guess = (guess + result / guess) / 2
        if abs(new_guess - guess) < 0.0000001:
            break
        guess = new_guess
    return guess


def format_number(value):
    """Format a number for display."""
    if isinstance(value, str):
        return value
    if isinstance(value, float):
        if value == int(value):
            return str(int(value))
        return f"{value:.10f}".rstrip('0').rstrip('.')
    return str(value)


def main():
    """Main function to compute statistics."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    try:
        numbers = read_numbers_from_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    count = len(numbers)
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_std_deviation(variance)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = [
        f"COUNT: {count}",
        f"MEAN: {format_number(mean)}",
        f"MEDIAN: {format_number(median)}",
        f"MODE: {format_number(mode)}",
        f"SD: {format_number(std_dev)}",
        f"VARIANCE: {format_number(variance)}",
        f"Elapsed Time: {elapsed_time:.6f} seconds"
    ]

    for line in results:
        print(line)

    with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
        for line in results:
            result_file.write(line + '\n')

    print("\nResults saved to StatisticsResults.txt")


if __name__ == "__main__":
    main()
