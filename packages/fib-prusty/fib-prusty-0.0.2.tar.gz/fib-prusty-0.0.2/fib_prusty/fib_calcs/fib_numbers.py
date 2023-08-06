from .fib_number import recurring_fibonacci_number
from typing import List


def calculate_numbers(numbers: List[int]) -> List[int]:
    return [recurring_fibonacci_number(number=i) for i in numbers]