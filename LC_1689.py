'''
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
(https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/)

Intuition:
    1. Given a number return the minimum number of ways we can split such that each partition is deci-binary number.
    2. So deci-binary number is a number whose digits are only 1 and 0.
    3. 

Time Complexity:
    1. In worst case we need to traverse whole string - O(N)

Space Complexity:
    2. No extra space used - O(1)

'''

import doctest

def minPartitions(n: str) -> int:
    '''
    >>> minPartitions('3')
    3
    >>> minPartitions('53562893983662')
    9
    >>> minPartitions('838837')
    8
    '''
    prev_max_digit = '0'

    for digit in n:
        if digit == '9':
            return 9
        
        if digit > prev_max_digit:
            prev_max_digit = digit
    
    return int(prev_max_digit)

if __name__ == "__main__":
    doctest.testmod()