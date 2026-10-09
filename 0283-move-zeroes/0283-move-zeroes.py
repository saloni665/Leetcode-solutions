class Solution(object):
    def moveZeroes(self, nums):
        n =len(nums)
        temp = []
        
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])

        l = len(temp)

        for i in range(l):
            nums[i] = temp[i]

        for i in range(l, n):
            nums[i] = 0    

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna