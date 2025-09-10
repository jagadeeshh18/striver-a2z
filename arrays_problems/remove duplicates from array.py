class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        writeindex = 1
        for i in range(1,len(nums)):
         if nums[i] != nums[i-1]:
            nums[writeindex]=nums[i]
            writeindex+=1
        return writeindex 

nums = [1,1,2]
sol = Solution()
k = sol.removeDuplicates(nums)  # k = 2
print(k)          # prints: 2
print(nums[:k])

        
