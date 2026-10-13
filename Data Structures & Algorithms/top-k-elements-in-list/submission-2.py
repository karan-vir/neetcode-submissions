class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap of the numbers and frequency
        freq = defaultdict(int)

        for num in nums: #--Time Complexity of O(n)
            freq[num] += 1

        # sort the dictionary basis the values --O(log(n))
        sort_index = sorted(freq.items(), key = lambda item: item[1] , reverse = True) 
        

        # Loop over to find the elements upto k -- O(k)
        out_lst = []
        for i in range(k):
            out_lst.append(sort_index[i][0])
        
        return out_lst

    # Overall Time complexity of O(n)
    # Space Complexity of O(n)