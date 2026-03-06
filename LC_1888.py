'''
1888. Minimum Number of Flips to Make the Binary String Alternating
(https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)
'''

import doctest

def minFlips(s: str) -> int:
    '''
    >>> minFlips("111000001010101001001001001001001")
    11
    >>> minFlips("010")
    0
    >>> minFlips("1110")
    1
    '''
    size = len(s)
    flips_count_if_started_with_1 = [0] * size
    if s[-1] == "0":
        flips_count_if_started_with_1[-1] = 1

    for idx in range(size - 2, -1, -1):
        # no_of_zeros_flips = size of subarray - no_of_ones_flips
        flips_count_if_started_with_1[idx] = size - idx - 1 -flips_count_if_started_with_1[idx + 1]
        if s[idx] == "0":
            flips_count_if_started_with_1[idx] += 1

    s *= 2

    flips = min(flips_count_if_started_with_1[0], size - flips_count_if_started_with_1[0])
    if flips == 0:
        return 0
    
    for left_len in range(1, size):
        right_len = size - left_len

        n_flips_if_started_with_1 = 0

        if left_len % 2:
            # odd
            # ends with 1 
            n_flips_if_started_with_1 = flips_count_if_started_with_1[0] - (right_len - flips_count_if_started_with_1[left_len])
        else:
            # even
            # ends with 0
            n_flips_if_started_with_1 = flips_count_if_started_with_1[0] - flips_count_if_started_with_1[left_len]
        
        curr = 0
        if right_len % 2:
            curr = flips_count_if_started_with_1[left_len] + (left_len - n_flips_if_started_with_1)
        else:
            curr = flips_count_if_started_with_1[left_len] + n_flips_if_started_with_1
        
        flips = min(flips, curr, size - curr)

    return flips

if __name__ == "__main__":
    doctest.testmod()