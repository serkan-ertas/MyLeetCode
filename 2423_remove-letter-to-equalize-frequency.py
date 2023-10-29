# returns true when the number of all letters is the same if exactly one letter is removed
class Solution:
    def equalFrequency(self, word: str) -> bool:
        # dictionary's keys = letters ,, values = occurrences
        letterHM = {}
        for i in word:
            if i in letterHM:
                letterHM[i] += 1
            else:
                letterHM[i] = 1

        # for every char
        # checks if all number of occurrences are the same
        # when the number of a letter is decremented by one
        for letter in letterHM:
            letterHM[letter] -= 1
            valueSet = set(letterHM.values())
            if 0 in valueSet:
                valueSet.remove(0)
            if len(valueSet) == 1:
                return True
            letterHM[letter] += 1
        return False
