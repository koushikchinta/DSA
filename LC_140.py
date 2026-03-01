'''
140. Word Break II
(https://leetcode.com/problems/word-break-ii/description/)

Time Complexity:

Space Complexity:
'''

from typing import List
import doctest

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    '''
    >>> wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    ['cat sand dog', 'cats and dog']
    >>> wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
    >>> wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    []
    '''
    size = len(s)
    dictionary = set(wordDict)

    # we can cache the results
    def _wordBreak(start: int) -> List[str]:
        if start >= size:
            return [""]
        
        result: List[str] = []

        prefix = ""
        for i in range(start, size):
            prefix += s[i]

            if prefix in dictionary:
                for suffix in _wordBreak(i + 1):
                    result.append(f"{prefix} {suffix}".strip())
        
        return result
    
    return _wordBreak(0)

if __name__ == "__main__":
    doctest.testmod()