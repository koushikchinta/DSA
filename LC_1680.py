'''
1680. Concatenation of Consecutive Binary Numbers
(https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/)

Intuition:
    1. Given an integer N, we need to concatenate the binary representation of each element from 1 to N. Since the answer can be huge
    mod it with 10^9 + 7
    2. Every number will be grouped between 2^(n-1) and 2^n where n is number of bits
    3. So any number before concatenating to the result, left shift the result to n bits and bitwise_OR with the number.
    This will equivalent to concatenating.
        Example: let say our current result is of form 1011 and current number is of form 101. so to concatenate
        shift the result bits to 3 positions (3 is the bit_length of current number). This results in 1011000.
        Performing bitwise_OR results in 1011101.
    
    4. Repeat this until > N

Time Complexity:
    1. We iterate through each number once - O(N)

Space Complexity:
    1. No extra space used - O(1)
'''

import doctest

def concatenatedBinary1(n: int) -> int:
    '''
    >>> concatenatedBinary1(1)
    1
    >>> concatenatedBinary1(3)
    27
    >>> concatenatedBinary1(12)
    505379714
    '''
    MOD = 10**9+7

    start = 1
    result = 0
    current_bit_length = 1

    while start <= n:
        end = min(n + 1, start << 1)

        # All these number contain bit_length of (current_bit_length) 
        for current_number in range(start, end):
            result = (result << current_bit_length | current_number) % MOD
        
        current_bit_length += 1
        start = end
    
    return result


def concatenatedBinary2(n: int) -> int:
    '''
    >>> concatenatedBinary2(1)
    1
    >>> concatenatedBinary2(3)
    27
    >>> concatenatedBinary2(12)
    505379714
    '''
    MOD = 10**9+7

    result = 0
    current_bit_length = 0

    for num in range(1, n+1):
        # if current num is power of 2
        if (num & (num - 1)) == 0:
            current_bit_length += 1
        
        result = (result << current_bit_length | num) % MOD
    
    return result

if __name__ == "__main__":
    doctest.testmod()              