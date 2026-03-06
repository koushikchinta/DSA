'''
386. Lexicographical Numbers
(https://leetcode.com/problems/lexicographical-numbers/description/)
'''

from typing import List
import doctest

def lexicalOrder(n: int) -> List[int]:
    '''
    >>> lexicalOrder(13)
    [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> lexicalOrder(2)
    [1, 2]
    '''
    result: List[int] = []
    def dfs(m: int):
        if m > n:
            return
        result.append(m)
        m *= 10
        for digit in range(0, 10): 
            if (p := m + digit) <= n:
                dfs(p)

    for digit in range(1, 10):
        dfs(digit)
    
    return result

if __name__ == "__main__":
    doctest.testmod()
