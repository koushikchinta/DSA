'''
3175. Find The First Player to win K Games in a Row
(https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/description/)

Intuition:
    1. Each time a player wins, the loser moves to the end of the queue.
    2. Since the player with the higher skill always wins, the game continues only until 
    we encounter the player with the maximum skill.
    3. If any player manages to win k consecutive games before we reach the maximum-skilled player, we return that player’s index. 
    Otherwise, we return the index of the player with the maximum skill, since they will eventually achieve k consecutive wins.

Time Complexity:
    1. We iterate through whole array once - O(N)

Space Complexity:
    1. No extra space used - O(1)
'''

from typing import List
import doctest


def findWinningPlayer(skills: List[int], k: int) -> int:
    '''
    >>> findWinningPlayer([4,2,6,3,9], 2)
    2
    >>> findWinningPlayer([2,5,4], 3)
    1
    >>> findWinningPlayer([19,3,6,16,10,9,2], 422917785)
    0
    '''
    n_players = len(skills)

    curr_winner = 0
    n_won = 0
    for curr_player in range(1, n_players):
        if skills[curr_winner] > skills[curr_player]:
            n_won += 1
        else:
            n_won = 1
            curr_winner = curr_player
        
        if n_won == k:
            return curr_winner
    
    # This will always be the player with maximum skill 
    return curr_winner
    

if __name__ == "__main__":
    doctest.testmod()
