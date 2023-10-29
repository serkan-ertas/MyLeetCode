# Taking sqrt of a number with Newton-Raphson Method
from random import randint


class Solution:
    def mySqrt(self, x: int) -> int:
        randNum = randint(1, 50)
        while True:
            root = 0.5 * (randNum + (x/randNum))
            if abs(root - randNum) < 1:
                break
            randNum = root
        return int(root//1)