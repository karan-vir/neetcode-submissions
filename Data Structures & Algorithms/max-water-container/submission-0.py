class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # volume width * height (maximize)
        l = 0 
        r = len(heights)-1
        maxV = 0

        while r > l:
            width = r -l
            height = min(heights[l], heights[r])
            volume = height * width
            maxV = max(volume, maxV)

            if heights[l] == height:  #left is the min
                l += 1
            else:  #right is the min
                r -= 1

        return maxV
