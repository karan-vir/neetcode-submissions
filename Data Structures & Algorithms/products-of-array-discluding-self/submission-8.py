class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # bruteforce approach
        # 1. Remove the value at that index to create a sublist. 
        # 2. Then use the sublist to calculate the product
        # 3. Store the product into the output list

        def cal_prd_lst(lst):
            prod_out = 1

            for num in lst:
                prod_out *= num
                
            return prod_out

        prod_const = cal_prd_lst(nums)
        lst_out = []

        for index in range(len(nums)):
            if nums[index] == 0:
                lst = nums.copy()
                lst.pop(index)
                prod = cal_prd_lst(lst)
            else:
                prod = int(prod_const/nums[index])
            lst_out.append(prod)
        
        return lst_out


   
    
    # out_lst = []
    # for i in range(len(nums)): # Time Complexity: O(n) 
    #     if i == 0:
    #         lst = nums[1:]
    #     elif i == len(nums)-1:
    #         lst = nums[:(len(nums)-1)]
    #     else:
    #         lst = nums[0:i] + nums[i+1:] # SC :  O(n)


    #     prod_out = cal_prd_lst(lst) # TC: O(n-1) 

    #     out_lst.append(prod_out) 

    
    # return out_lst
    # Time Complexity = O(n^2)
    # space Complexity = O(n^2) -> Storing a separate list of every run