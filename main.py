from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums = list(filter(lambda x: x < target, nums))
    result = []
    for i in range(0, len(nums)):
        a = nums[i]
        for j in range(i + 1, len(nums)):
            b = nums[j]
            print(j)
            if a + b == target:
                result.extend([i, j])
                break
        else:
            continue
        break
    return result
