class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxVal = 0
        for index, currentLetter in enumerate(s):
            temp_maxVal = 1
            letterSet = set()
            letterSet.add(currentLetter)
            for j in range(index+1, length):
                if s[j] in letterSet:
                    break
                else:
                    temp_maxVal += 1
                    letterSet.add(s[j])
            if temp_maxVal > maxVal:
                maxVal = temp_maxVal
        return maxVal