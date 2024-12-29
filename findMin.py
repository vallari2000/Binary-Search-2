class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = low + (high-low) //2
            if nums[low]<= nums[high]:
                return nums[low]
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[low] <= nums[mid]:
                low = mid +1
            elif nums[mid]<=nums[high]:
                high = mid-1

        