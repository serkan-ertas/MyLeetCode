class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxVal = 0
        for index, currentLetter in enumerate(s):
            print("beginning for ",currentLetter)
            temp_maxVal = 1
            letterSet = set()
            letterSet.add(currentLetter)
            for j in range(index+1, length):
                print("j is:",s[j])
                if s[j] in letterSet:
                    print("letterSet in break:",letterSet)
                    break
                else:
                    temp_maxVal += 1
                    letterSet.add(s[j])
                print("letter set:",letterSet,"and tempVal:",temp_maxVal)
            if temp_maxVal > maxVal:
                maxVal = temp_maxVal
        return maxVal
