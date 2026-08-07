class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # take the first number
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if ((nums[i] + nums[j]) == target) and i != j:
                    return [i, j]
        # add it with the second number
        # check to see if the sum equals target
        # return indices of the two numbers