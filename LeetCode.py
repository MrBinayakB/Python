#Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    a.append(i)
                    a.append(j)
                    break
                else:
                    continue
        return a

#Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        num=x
        a=0
        while x>0:
            a=a*10+x%10
            x=x//10
        return a == num