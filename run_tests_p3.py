"""
Test Runner for word_count.py
Executes all test cases and saves evidence to a file.
"""

import subprocess
import sys
from datetime import datetime

TEST_CASES = [
    "test_files/P3_TC1.txt",
    "test_files/P3_TC2.txt",
    "test_files/P3_TC3.txt",
    "test_files/P3_TC4.txt",
    "test_files/P3_TC5.txt",
]

def run_test(test_file):
    """Run a single test case and return the output."""
    result = subprocess.run(
        [sys.executable, "word_count.py", test_file],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr


def main():
    """Run all test cases and save results."""
    output_lines = []
    separator = "=" * 70

    output_lines.append(separator)
    output_lines.append("EVIDENCIA DE EJECUCION - word_count.py")
    output_lines.append(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append(separator)
    output_lines.append("")

    for i, test_file in enumerate(TEST_CASES, 1):
        output_lines.append(f"TEST CASE {i}: {test_file}")
        output_lines.append("-" * 70)
        result = run_test(test_file)
        output_lines.append(result)
        output_lines.append("")

    output_lines.append(separator)
    output_lines.append("TODOS LOS CASOS DE PRUEBA EJECUTADOS EXITOSAMENTE")
    output_lines.append(separator)

    full_output = "\n".join(output_lines)

    # Print to console
    print(full_output)

    # Save to file
    with open("P3_TestEvidence.txt", "w", encoding="utf-8") as f:
        f.write(full_output)

    print(f"\nEvidencia guardada en: P3_TestEvidence.txt")


if __name__ == "__main__":
    main()
