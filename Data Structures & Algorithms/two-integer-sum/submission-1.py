class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compare = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in compare:
                return [compare[diff], i]
            compare[n] = i