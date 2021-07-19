# link to problem: https://leetcode.com/problems/group-anagrams/


def groupAnagrams(strs):
    # variables
    dict = {}
    output = []
    for i in strs:  # loop through ["eat", "aet",...]
        list = []
        for j in i:
            list.append(j)  # string to list of chars
        list.sort()  # [a,e,t]
        s = "".join(list)  # aet
        if s in dict:
            dict[s].append(i)  # if [a,e,t] is in the list, add "eat" in
        else:
            dict[s] = []  # create new key
            dict[s].append(i)  # add that word to the list
    # result
    for i in dict:
        output.append(dict[i])
    return output


s1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(s1))

s2 = []
print(groupAnagrams(s2))
