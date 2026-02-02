"""
Word Count Program

This program identifies all distinct words and their frequency
from a file containing words.

Usage: python wordCount.py fileWithData.txt
"""

import sys
import time


def read_words_from_file(filename):
    """Read words from a file, handling invalid data."""
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            line_words = line.split()
            for word in line_words:
                cleaned_word = ""
                for char in word:
                    if char.isalnum():
                        cleaned_word += char
                if cleaned_word:
                    words.append(cleaned_word.lower())
                else:
                    print(f"Warning: Invalid word '{word}' at line {line_num}.")
    return words


def count_word_frequency(words):
    """Count the frequency of each word."""
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def sort_by_frequency(frequency):
    """Sort words by frequency (descending) then alphabetically."""
    items = []
    for word, count in frequency.items():
        items.append((word, count))
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
            elif items[j][1] == items[j + 1][1]:
                if items[j][0] > items[j + 1][0]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    return items


def main():
    """Main function to count words."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    try:
        words = read_words_from_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)

    if not words:
        print("Error: No valid words found in the file.")
        sys.exit(1)

    frequency = count_word_frequency(words)
    sorted_words = sort_by_frequency(frequency)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = []
    header = f"{'WORD':<30}{'COUNT':<10}"
    results.append(header)
    results.append("-" * 40)

    for word, count in sorted_words:
        line = f"{word:<30}{count:<10}"
        results.append(line)

    results.append("-" * 40)
    results.append(f"Total distinct words: {len(frequency)}")
    results.append(f"Total words: {len(words)}")
    results.append(f"Elapsed Time: {elapsed_time:.6f} seconds")

    for line in results:
        print(line)

    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        for line in results:
            result_file.write(line + '\n')

    print("\nResults saved to WordCountResults.txt")


if __name__ == "__main__":
    main()
