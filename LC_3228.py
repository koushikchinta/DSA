'''
3228. Maximum Number of Operations to Move Ones to the End
(https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/)

Intuition:
    1. Maximum number of operations to move all '1' to the end. In one operation select any index i such that
    s[i] == '1' and s[i + 1] == '0' and move '1' to end or last '1'
    2. To maximize the moves we have to greedily group the '1's together and perform operation on each '1' in the current group

Time Complexity:
    1. We Iterate through whole string - O(N)

Space Complexity:
    1. No extra space used - O(1)

'''
import doctest

def maxOperations(s: str) -> int:
    '''
    >>> maxOperations('1001101')
    4
    >>> maxOperations('00111')
    0
    >>> maxOperations('110')
    2
    '''
    size = len(s)

    n_ones = 0
    result = 0
    for i in range(size):
        if s[i] == '1':
            if i > 0 and s[i - 1] == '0':
                result += n_ones
            n_ones += 1

    if s[-1] == '0':
        result += n_ones
        
    return result

if __name__ == "__main__":
    doctest.testmod()