class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#    Approach is
        # [4,5,6] target = 10
        # if 10-4 = 6 is in hash map  it is not, store 4
        # move to 5
        # if 10-5 = 5 is in hash map if not store 5 {}
        # if 10-6 is in has set, yes return indexs

        # algo is check if the diff is in hashmap, if not store the element
        diff = defaultdict(int)
        
        for index, i in enumerate(nums):
            if target - i not in diff:
                diff[i] = index
            else:
                return [diff[target-i], index]


        
            
# # Efficeint BRUTE FORCE
#          i =0
#          j = i + 1

#          for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i!= j and nums[i] +nums[j] == target:
#                     return [i,j]