'''
Dice throw
(https://www.geeksforgeeks.org/problems/dice-throw5349/1)
'''

from functools import cache
import doctest

@cache
def noOfWays(m: int, n: int, x: int) -> int:
    '''
    >>> noOfWays(6, 3, 12)
    25
    >>> noOfWays(10, 3, 12)
    55
    '''
    if x == 0:
        return 1 if n == 0 else 0
    
    max_val = m * n
    min_val = n

    if x < min_val or x > max_val:
        return 0
    
    nWays = 0
    for face in range(1, m + 1):
        nWays += noOfWays(m, n - 1, x - face)
    
    return nWays

if __name__ == "__main__":
    doctest.testmod()