"""
Convert Numbers Program

This program converts numbers to binary and hexadecimal representation.

Usage: python convertNumbers.py fileWithData.txt
"""

import sys
import time


def read_numbers_from_file(filename):
    """Read numbers from a file, handling invalid data."""
    numbers = []
    errors = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                number = int(line)
                numbers.append((line_num, number))
            except ValueError:
                print(f"Error: Invalid data '{line}' at line {line_num}. Skipping.")
                errors.append((line_num, line))
    return numbers, errors


def int_to_binary(number):
    """Convert an integer to binary string using basic algorithm."""
    if number == 0:
        return "0"
    if number < 0:
        binary = int_to_binary_twos_complement(number)
        return binary
    result = ""
    temp = number
    while temp > 0:
        remainder = temp % 2
        result = str(remainder) + result
        temp = temp // 2
    return result


def int_to_binary_twos_complement(number):
    """Convert negative number to binary using two's complement (10-bit)."""
    if number >= 0:
        return int_to_binary(number)
    bits = 10
    twos_complement = (1 << bits) + number
    result = ""
    temp = twos_complement
    for _ in range(bits):
        remainder = temp % 2
        result = str(remainder) + result
        temp = temp // 2
    return result


def int_to_hex(number):
    """Convert an integer to hexadecimal string using basic algorithm."""
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    if number < 0:
        hex_val = int_to_hex_twos_complement(number)
        return hex_val
    result = ""
    temp = number
    while temp > 0:
        remainder = temp % 16
        result = hex_chars[remainder] + result
        temp = temp // 16
    return result


def int_to_hex_twos_complement(number):
    """Convert negative number to hex using two's complement (32-bit)."""
    if number >= 0:
        return int_to_hex(number)
    twos_complement = (1 << 32) + number
    hex_chars = "0123456789ABCDEF"
    result = ""
    temp = twos_complement
    while temp > 0:
        remainder = temp % 16
        result = hex_chars[remainder] + result
        temp = temp // 16
    return result


def main():
    """Main function to convert numbers."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    try:
        numbers, _ = read_numbers_from_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    results = []
    header = f"{'INDEX':<8}{'NUMBER':<15}{'BINARY':<35}{'HEXADECIMAL':<15}"
    results.append(header)
    results.append("-" * 73)

    for idx, (_, number) in enumerate(numbers, 1):
        binary = int_to_binary(number)
        hexadecimal = int_to_hex(number)
        line = f"{idx:<8}{number:<15}{binary:<35}{hexadecimal:<15}"
        results.append(line)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results.append("-" * 73)
    results.append(f"Total numbers converted: {len(numbers)}")
    results.append(f"Elapsed Time: {elapsed_time:.6f} seconds")

    for line in results:
        print(line)

    with open("ConvertionResults.txt", 'w', encoding='utf-8') as result_file:
        for line in results:
            result_file.write(line + '\n')

    print("\nResults saved to ConvertionResults.txt")


if __name__ == "__main__":
    main()
