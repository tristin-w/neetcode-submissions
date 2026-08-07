class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        len_set = len(set(nums))
        if len_nums == len_set:
            return False
        else:
            return True