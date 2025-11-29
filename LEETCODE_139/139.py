
# Variant 1
class Solution1:
    '''
    We keep two pointers: START, END that points to s
    START: current position in s
    END: end of the sub string 
    we check if substring exists in given word dictionary then we again check substring starting from END.
    Check until we get true or else false
    '''
    def wordBreak(self, s:str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict) # for quick lookup
        cache = {} # for storing sub problems result
        return self._wordBreak(s, wordSet, cache, 0)
        
    def _wordBreak(self, s: str, wordSet: set[str], cache: dict[int,bool], start: int) -> bool:
        if start >= len(s):
            return True
        
        if start in cache:
            return cache[start]
        
        subStr = ''
        for end in range(start,len(s)):
            subStr+=s[end]
            # OR 
            # subStr = s[start: end+1]
            if subStr in wordSet:
                # check if rest of string is possible to break
                if self._wordBreak(s, wordSet, cache, end+1):
                    cache[start] = True
                    # return as we need only atmost one possibility to check 
                    return True
        
        cache[start] = False
        return False
                

# Variant 2
class Solution2:
    '''
    Same Logic as above instead of checking only possibility we now return all possible splits
    s: 'ilovemath'
    wordDict: ['i','love','math','il','ove']
    Result:
    'i love math'
    'il ove math'
    '''
    def wordBreak(self, s:str, wordDict:list[str]) -> list[str]:
        wordSet = set(wordDict)
        cache = {}
        return self._wordBreak(s, wordSet, cache, 0)
    
    def _wordBreak(self, s:str, wordDict: set[str], cache:dict[int,list[str]], start:int) -> list[str]:
        if start >= len(s):
            # FOR COUNT
            # return 0
            # END FOR COUNT

            # FOR LIST
            return [""]
            # END FOR LIST
        
        if start in cache:
            return cache[start]
        
        subStr = ""
        # FOR COUNT
        # ans = 0
        # END FOR COUNT

        # FOR LIST
        ans = []
        # END FOR LIST
        for end in range(start,len(s)):
            subStr+=s[end]
            if subStr in wordDict:
                # FOR COUNT
                # ans += self._wordBreak(s, wordDict, cache, end+1)
                # END FOR COUNT

                # FOR LIST
                for other in self._wordBreak(s, wordDict, cache, end+1):
                    ans.append(f'{subStr} {other}'.strip())
                # END FOR LIST
        
        cache[start] = ans
        return ans
    
if __name__ == "__main__":
    # (s, wordDict, ...variantsExpectedResults)
    TEST_CASES = [
        ("leetcode",["leet","code"],True,['leet code']),
        ("applepenapple",["apple","pen"],True, ['apple pen apple']),
        ("catsandog",["cats","dog","sand","and","cat"],False,[]),
        ('ilovemath',['i','love','math','meth','il','ove'],True,['i love math','il ove math']),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],False,[])
    ]

    variant1 = Solution1()
    variant2 = Solution2()
    for i,testcase in enumerate(TEST_CASES,1):
        s, wordDict, *expected = testcase
        assert variant1.wordBreak(s,wordDict) == expected[0]
        ans = variant2.wordBreak(s,wordDict)
        assert len(ans) == len(expected[1]), f'Expected size of {len(expected[1])} but found {len(ans)}'
        assert set(ans) == set(expected[1]), f'Expected {expected[1]} but found {ans}'
        print(f'Test Case {i}: Passed')