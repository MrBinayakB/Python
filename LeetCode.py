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

#Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        target_pos=0
        for index in range (len(nums)):
            if nums[index]==target:
                return index
            elif nums[index]>target:
                return target_pos
            else:
                target_pos+=1
        return target_pos
    
#longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return""

        base=strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i]!= base[i]:
                    return base[0:i]

        return base