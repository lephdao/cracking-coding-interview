# draft code: https://pastebin.com/EcXcPPbd
# link to problem: https://leetcode.com/articles/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
      if len(s) == 1:
          return 1
      if s == "" or s == " ":
          return 0

      result = 0
      countStr = ""
      i = 0
      while len(s) > 1:
          i = 1
          countStr = ""
          countStr = countStr + s[0]

          while s[i] not in countStr:
              countStr = countStr + s[i]
              if i < len(s) - 1:
                  i = i + 1

          if len(countStr) > result:
              result = len(countStr)
          s = s[1:]

      return result


s1 = "abcabcbb"
n1 = lengthOfLongestSubstring(s1)
print(n1)

s2 = "pwwkew"
n2 = lengthOfLongestSubstring(s2)
print(n2)

# two special cases
s3 = ""
n3 = lengthOfLongestSubstring(s3)
print(n3)

s4 = "f"
n4 = lengthOfLongestSubstring(s4)
print(n4)
