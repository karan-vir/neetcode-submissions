class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left_index = 0
        right_index = n-1

        for i in range(n):
            # print(right_index, numbers[right_index])
            if numbers[left_index]+numbers[right_index] > target:
                right_index -= 1
            elif numbers[left_index]+numbers[right_index] < target:
                 # [1,2,3,5] target = 5 1+5, 1+3
                 left_index += 1
            else:
                return [left_index+1, right_index+1]







# Brute Force
#   for i in range(len(numbers)):
#         for j in range():
#             if i!= j and numbers[i] + numbers[j] == target:
#                 return [i+1,j+1]