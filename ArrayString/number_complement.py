# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
# Input: 5 (101) --> Output: 2(010)
class Solution:
    def findComplement(self, num):
    	# convert num to a binary
    	binary = bin(num).replace("0b", "")
    	#calculte length of binary
    	length = len(binary)
    	# create flip bits from num: if length = 3, create 1000 (3 zeroes), then 1000 - 1 = 0111 = 111
    	bit_mask = (1 << length) - 1
    	# perform XOR
    	result = num ^ bit_mask
    	return result


s = Solution()
print(s.findComplement(0))
print(s.findComplement(5))
print(s.findComplement(32))