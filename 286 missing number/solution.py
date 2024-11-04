from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    return n*(n+1)//2 - sum(nums)
