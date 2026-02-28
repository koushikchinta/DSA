'''
3371. Identify the Largest Outlier in an Array
(https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/)

Intuition:
    1. Given an array of size N, there are N / 2 special elements. Among the remaining two elements, 
    one is equal to the sum of the special elements (let's call this the integral element), and the other is the outlier.
    2. If we assume that a particular element is the outlier, then the remaining elements should contain:
        i. The N / 2 special elements, and
        ii. One element equal to their total sum (the integral element).
    3. After removing the outlier, the sum of the remaining elements should be equal to:
                2 x (integral element)
        This is because the remaining elements consist of the special elements plus their total sum.
    4. Therefore, we iterate through each element, assuming it is the outlier.
        i. If removing it results in an odd sum, we can immediately skip it because it cannot be split into two equal parts.
        ii. If the remaining sum is even, then the integral element must be equal to half of that sum.
    5. To efficiently check whether this integral element exists, we use a hash map (frequency dictionary) instead of a set.
        i. This is necessary because the outlier could be equal to the integral element.
        ii. In that case, we must ensure that the element appears at least twice in the array to be valid.

Time Complexity:
    1. we iterate through whole array twice, one to build counter and total sum and other to check outlier
    So, O(2N) -> O(N)

Space Complexity:
    1. We need to store frequencies of element, in worst case all elements are unique so O(N)
'''

from typing import List, Dict
import doctest

def getLargestOutlier(nums: List[int]) -> int:
    '''
    >>> getLargestOutlier([-108,-108,-517])
    -517
    >>> getLargestOutlier([752,678,-483,-583,201,0,-886,-474,-171])
    0
    >>> getLargestOutlier([2,3,5,10])
    10
    >>> getLargestOutlier([-2,-1,-3,-6,4])
    4
    >>> getLargestOutlier([1,1,1,1,1,5,5])
    5
    '''
    total_sum = 0
    counter: Dict[int, int] = {}

    for num in nums:
        total_sum += num
        counter[num] = counter.get(num, 0) + 1

    max_outlier = -1001 # 1000 <= nums[i] <= 1000

    # Assuming each element as outlier
    for outlier in counter:
        excluded_sum = total_sum - outlier

        # must be even since sum of n - 2 special element and other element are same
        if excluded_sum % 2:
            # odd sum, cannot contain integral element
            continue
        

        integral_element = excluded_sum // 2
        if integral_element in counter:
            # if integral_element and outlier are same, check whether we have multiple occurences
            if (integral_element != outlier) or (counter[integral_element] > 1): 
                max_outlier = max(max_outlier, outlier)
    
    return max_outlier

if __name__ == "__main__":
    doctest.testmod()
