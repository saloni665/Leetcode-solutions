class Solution:
    def findFloor(self, arr, x):
        # code here
        n = len(arr)
        low = 0 
        high = n-1
        ans = -1
        
        while low <= high:
            mid = (low + high)//2
            if arr[mid] <= x:
                ans = mid
                low = mid + 1
                
                
            else:
                high = mid - 1
            
        return ans   

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna