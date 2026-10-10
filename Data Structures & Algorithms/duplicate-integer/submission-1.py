class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a Frequency dictionary, if any value in frequency dictionary is 
        # greater than 1, return True else False
        
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        if len(nums_dict) == 0:
            return False
        elif max(nums_dict.values()) > 1:
            return True
        else:
            return False

        