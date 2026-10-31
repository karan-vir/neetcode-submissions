class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in numSet:
                length = 0

                while (num+length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

                


















# Attempt 1
        # nums_sort = sorted(nums)
        # nums_set = list(set(nums_sort))
        # diff = []

        # for i in range(len(nums_set)-1):
        #     diff.append(nums_set[i+1] - nums_set[i])

        # print(diff)
        # start_index = 0 
        # end_index = 0
        # one_counter = 0
        # max_counter = 0
        # out_arr = []


        # for index, i in enumerate(diff):
        #     if one_counter > 0:
        #         if i == 1:
        #             end_index += 1
        #             one_counter += 1
        #         else:
        #             max_counter = one_counter
        #             print(start_index,end_index )
        #             out_arr = nums_set[start_index:end_index+2]
        #             one_counter = 0

        #     elif i == 1: 
        #         start_index = index
        #         end_index = start_index
        #         one_counter += 1
        #     else:
        #        pass
           
        
        # return len(out_arr)

