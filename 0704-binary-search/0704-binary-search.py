class Solution(object):
    def search(self, nums, target):
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, low, high, target):
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, high, target)

        else:
            return self.binarySearch(nums, low, mid - 1, target)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna