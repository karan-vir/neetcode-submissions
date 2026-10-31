class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0
        r = l +1

        while r < len(prices):
            print(l,r)
            if prices [r] < prices[l]:
                l += 1
                r = l +1
            else:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
                
                r += 1

        # [2,1,2,1,0,1,2]
        # [a,b,c,d,e,f,g]
        # l = a, r = b
        # l=b , r = c p, 1
        # l =b, r =d p =0
        # l = b r = e l = c r =d
        # l = d, r = e
        # l = e , r=f
                    
            

        return maxProfit



# Bruteforce Algo
# maxProfit = 0

#         for i in range(len(prices)):
#             for j in range(i+1,len(prices)):
#                 profit = prices[j]-prices[i]
#                 if profit > maxProfit:
#                     maxProfit = profit

#         return maxProfit

#         TC: O(n2)
       