#TC:O(n)
#SC:O(1)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[] #initialize the result 
        for i in range(len(nums)): #traverse through the array
            index=abs(nums[i])-1 #index is going to be the abs val minus one
            if nums[index]>0: #mark the lements visited by making it as negative numbers
                nums[index]*=-1
        for i in range(len(nums)): #now traverse through the array and find where the numbers disappeared
            if nums[i]>0:
                result.append(i+1)
        return result 

        