'''
648. Replace Words
(https://leetcode.com/problems/replace-words/description/)

Time Complexity:
    1. W : word length
    2. N : Number of words in dictionary
    3. For building trie we iterate through each character from each word - O(W * N)
    4. M : Number of words in sentence
    5. For retreiving the shortest root, at worst case we iterate through whole word - O(W * M)
    Overall - O(N * W)

Space Complexity:
    1. W: Max word length
    2. for each node we have 26 children
    3. O(26 ^ W)
'''


from typing import List, Optional
import doctest

class Trie:
    def __init__(self) -> None:
        self.isEnd = False
        self.children: List[Optional[Trie]] = [None] * 26

    def add_word(self, word: str) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            assert node is not None

            if node.children[idx] is None:
                node.children[idx] = Trie()
            
            node = node.children[idx]
        
        assert node is not None
        node.isEnd = True
        
    def get_shortest_root(self, word: str) -> str:
        node = self

        res = ''
        for char in word:
            idx = ord(char) - ord('a')

            assert node is not None
            childNode = node.children[idx]
            
            if childNode is None:
                return word

            res += char
            if childNode.isEnd:
                return res
            
            node = childNode
        
        return word

def replaceWords(dictionary: List[str], sentence: str) -> str:
    '''
    >>> replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
    'the cat was rat by the bat'
    >>> replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")
    'a a b c'
    >>> replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
    'a a a a a a a a bbb baba a'
    >>> replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery")
    'the cat was rat by the bat'
    '''

    trie = Trie()
    for word in dictionary:
        trie.add_word(word)
    
    return " ".join(map(trie.get_shortest_root, sentence.split()))

if __name__ == "__main__":
    doctest.testmod()