class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final = set(nums)
        if len(final) != len(nums):
            return True
        return False
        