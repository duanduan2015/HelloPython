class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                if i - start + 1 > maxLength:
                    maxLength = i - start + 1
            else:
                index = dic[s[i]]
                for j in range(start, index + 1):
                    if s[j] in dic:
                        del dic[s[j]]
                start = index + 1
                dic[s[i]] = i
        
        return maxLength
