import sys
from math import log10
from typing import Sequence, Dict


class BenfordAnalyzer:
    def __init__(self):
        self._first_digit_counts = [0] * 10
        self._second_digit_counts = {n: [0] * 10 for n in range(10)}

        self._expected_distribution = None

    @staticmethod
    def digit_probability(digit: int) -> float:
        """
        The probability of the occurrence of the given digit 1 to 9 inclusive.
        :param digit: A digit in the range 1..9 inclusive.
        :return: The probability of the occurrence of the given digit
        """
        if digit < 1 or digit > 9:
            raise ValueError("digit must be in the range [1..9]")

        return log10(1 + (1 / digit))

    @property
    def expected_distribution(self) -> Sequence[float]:
        if not self._expected_distribution:
            self._expected_distribution = [0.0] + [
                log10(1 + (1 / d)) for d in range(1, 10)
            ]

        return self._expected_distribution

    def add_number(self, number: float) -> None:
        """
        Add a number to the analyzer.
        :param number:
        :return:
        """

        # Ignore initial zeroes, decimal points and commas
        number_string = str(number).replace(".", "").replace(",", "").lstrip("0")
        first_digit = int(number_string[0]) if number_string else None
        second_digit = (
            int(number_string[1]) if number_string and len(number_string) > 1 else None
        )

        if first_digit:
            self._first_digit_counts[first_digit] = (
                self._first_digit_counts[first_digit] + 1
            )

        if second_digit is not None:
            self._second_digit_counts[first_digit][second_digit] = (
                self._second_digit_counts[first_digit][second_digit] + 1
            )

    def add_numbers(self, numbers: Sequence[float]) -> None:
        """
        Add a collection of numbers to the analyzer.
        :param numbers:
        :return:
        """
        if numbers:
            for number in numbers:
                self.add_number(number)

    @property
    def total_number_count(self) -> int:
        """
        The total number of numbers passed to the analyzer.
        :return:
        """
        return sum(self._first_digit_counts)

    @property
    def first_digit_counts(self) -> Sequence[int]:
        """
        The counts of each of the first digits from 0..9 for all of the numbers added to the analyzer.
        :return: A list of ten integers, representing the total counts of each first digit from 0.9
        respectively.
        """
        return [d for d in self._first_digit_counts]

    @property
    def first_digit_distribution(self) -> Sequence[float]:
        """
        The proportions of the total count of first digits for all of the numbers added to the analyzer.
        :return: A list of ten floating point numbers, representing the proportion of the total
        count represented by each digit.
        """
        total = sum(self._first_digit_counts)
        return [count / (total if total else 1) for count in self._first_digit_counts]

    @property
    def second_digit_counts(self) -> Dict[int, Dict[int, int]]:
        """
        The counts of the second digits provided to the analyzer.

        :return: A dictionary in the format: { first_digit : {0 : count0, 1: count1, etc.}, ... }
        """

        return {
            first_digit: {
                digit: self._second_digit_counts[first_digit][digit]
                for digit in range(10)
            }
            for first_digit in range(1, 10)
        }

    @property
    def second_digit_distribution(self) -> Dict[int, Dict[int, float]]:
        """
        The distribution of the second digits provided to the analyzer.

        :return: A dictionary in the format: { first_digit : {0 : distribution0, 1: distribution1, etc.}, ... }
        """

        digits = {}

        # First digit is NEVER 0, so skip it
        for first_digit in (d for d in self._second_digit_counts.keys() if d != 0):
            total = sum(self._second_digit_counts[first_digit])

            digits[first_digit] = {
                digit: self._second_digit_counts[first_digit][digit]
                / (total if total else 1)
                for digit in range(10)
            }

        return digits

    @property
    def second_digit_counts_combined(self) -> Dict[int, float]:
        """
        The total counts for each second digit in all of the numbers provided to the analyzer, regardless
        of the first digit.
        :return: A dictionary of the format { second_digit : digit_count }
        """

        overall = [0] * 10

        for d in self._second_digit_counts.keys():
            overall = [x + y for x, y in zip(overall, self._second_digit_counts[d])]

        return {d: overall[d] for d in range(10)}

    @property
    def second_digit_distribution_combined(self) -> Dict[int, float]:
        """
        The total distribution for each second digit in all of the numbers provided to the analyzer, regardless
        of the first digit.
        :return: A dictionary of the format { second_digit : digit_distribution }
        """

        second_digit_counts = self.second_digit_counts_combined
        total = sum(second_digit_counts.values())

        result = {}

        for d in second_digit_counts.keys():
            result = {
                d: (second_digit_counts[d] / total if total else 0)
                for d in second_digit_counts.keys()
            }

        return result

    def calculate_match(self) -> Dict:
        """
        Returns the expected, actual and difference percentage for each digit.

        :return:
        """
        total_numbers = sum(self.first_digit_counts)
        expected_counts = [c * total_numbers for c in self.expected_distribution]

        result = {}

        for digit in range(1, 10):
            result[digit] = {
                "expected": expected_counts[digit],
                "actual": self._first_digit_counts[digit],
                "difference": (
                    1.0 * self._first_digit_counts[digit] - expected_counts[digit]
                )
                / expected_counts[digit],
            }

        return result

    def matches_distribution(self, tolerance_percent: float = 5.0) -> bool:
        """
        Checks whether the distribution matches Benford's law.
        :param tolerance_percent:
        :return: True if the distribution matches Benford's law.
        """

        match_details = self.calculate_match()

        for d in range(1, 10):
            if abs(match_details[d]["difference"] * 100.0) > tolerance_percent:
                return False

        return True

    def write_text_report(self, tolerance: float) -> None:
        """
        Writes a text summary report about the series to stdout.

        :return:
        """
        match_details = self.calculate_match()

        max_difference = 0.0

        sys.stdout.write("\n")
        sys.stdout.write("Benford Analysis Result\n")
        sys.stdout.write("First Digits Expected vs Actual:\n")

        for d in range(1, 10):
            if abs(match_details[d]["difference"] * 100.0) > max_difference:
                max_difference = abs(match_details[d]["difference"] * 100.0)

            sys.stdout.write(
                f'{d}  {int(match_details[d]["expected"]):>10}  :  '
                f'{match_details[d]["actual"]:>6}  ->  '
                f'{(match_details[d]["difference"] * 100.0):>5.1f}%\n'
            )

        sys.stdout.write("\n")
        sys.stdout.write(f"Maximum difference: {max_difference:.1f}%\n")
        sys.stdout.write(
            f"Benford (tolerance {tolerance}%)? {self.matches_distribution(tolerance)}\n"
        )
        sys.stdout.write("\n")
        sys.stdout.flush()
