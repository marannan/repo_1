class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            #water can be held by base lenght * min height of the sides
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
    
if __name__ == "__main__":
    solution = Solution()
    print solution.maxArea([1,2,3,4,5,6])