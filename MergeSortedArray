# link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # make copy of nums1 to nums1_copy
        # m is len(nums1_copy)
        # n is len(nums2)
        p1 = 0
        p2 = 0
        nums1_copy = nums1[:m]
        nums1 = []
        if n == 0:
            return nums1
        if m == 0:
            for num in nums2:
                nums1.append(num)
        if n == 1 and m == 1:
            if nums1_copy[0] > nums2[0]:
                nums1.append(nums2[0])
                nums1.append(nums1_copy[0])
            else:
                nums1.append(nums1_copy[0])
                nums1.append(nums2[0])
            return nums1
        # if n == 1:
        #     nums1[0] = nums2[0]
        #     return nums1

        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 = p1 + 1
            elif nums1_copy[p1] >= nums2[p2]:
                nums1.append(nums2[p2])
                p2 = p2 + 1
        # copy the rest

        if p1 is not len(nums1_copy) - 1:  # if p1 isn't at the end, copy rest of nums1_copy
            for j in range(p1, len(nums1_copy)):
                nums1.append(nums1_copy[p1])
                p1 = p1 + 1
        if p2 is not len(nums2) - 1:
            for j in range(p2, len(nums2)):
                nums1.append(nums2[p2])
                p2 = p2 + 1
        return nums1


prob1 = Solution()
n1 = [1, 2, 3, 0, 0, 0]
m = 3
n2 = [2, 5, 6]
n = 3
print(n1)
print(n2)
result = prob1.merge(n1, m, n2, n)
print(result)
print("\n")

n1 = [0]
m = 0
n2 = [1]
n = 1
print(n1)
print(n2)
result = prob1.merge(n1, m, n2, n)
print(result)
print("\n")

n1 = [2, 0]
m = 1
n2 = [1]
n = 1
print(n1)
print(n2)
result = prob1.merge(n1, m, n2, n)
print(result)

n1 = [0, 0]
m = 0
n2 = [4, 7]
n = 2
print(n1)
print(n2)
result = prob1.merge(n1, m, n2, n)
print(result)

n1 = [4, 0, 0, 0, 0, 0]
m = 1
n2 = [1, 2, 3, 5, 6]
n = 5
print(n1)
print(n2)
result = prob1.merge(n1, m, n2, n)
print(result)
