# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        
        while left < right:
            mid = left + (right-left)/2
            if(isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return left
        

#[1,2,3,4,5] - 4 is bad version
#left = 1, 4
#right = 5, 4
#mid = 1 + (5-1)/2 = 3
#mid = 4 + (5-4)/2 = 4.5 = 4
#isbadversion(3) = false
#isbadversion(4) = true
#left = right = 4 --> return 4




			
			
			
			
        