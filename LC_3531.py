'''
3531. Count Covered Buildings
(https://leetcode.com/problems/count-covered-buildings/description/)

Intuition:

Time Complexity:

Space Complexity:


'''

from typing import List, Dict
import doctest

def countCoveredBuildings1(n: int, buildings: List[List[int]]) -> int:
    '''
    >>> countCoveredBuildings1(3, [[1,2],[2,2],[3,2],[2,1],[2,3]])
    1
    >>> countCoveredBuildings1(3, [[1,1],[1,2],[2,1],[2,2]])
    0
    >>> countCoveredBuildings1(5, [[1,3],[3,2],[3,3],[3,5],[5,3]])
    1
    >>> countCoveredBuildings1(3, [[1,2],[3,1],[1,1],[3,2],[1,3]])
    0
    '''
    ys: Dict[int, List[int]] = {} # This keep track for every y what is the minX and maxX p

    for x, y in buildings:
        if not y in ys:
            ys[y] = [n, 0]
        
        ys[y][0] = min(ys[y][0], x)
        ys[y][1] = max(ys[y][1], x)
    
    buildings.sort()

    res = 0
    n_buildings = len(buildings)

    for i in range(1, n_buildings - 1):
        if buildings[i-1][0] ==  buildings[i][0] == buildings[i+1][0]:
            x, y = buildings[i]
            minX, maxX = ys[y]
            if x > minX and x < maxX:
                res += 1
    
    return res


def countCoveredBuildings2(n: int, buildings: List[List[int]]) -> int:
        '''
        >>> countCoveredBuildings2(3, [[1,2],[2,2],[3,2],[2,1],[2,3]])
        1
        >>> countCoveredBuildings2(3, [[1,1],[1,2],[2,1],[2,2]])
        0
        >>> countCoveredBuildings2(5, [[1,3],[3,2],[3,3],[3,5],[5,3]])
        1
        >>> countCoveredBuildings2(3, [[1,2],[3,1],[1,1],[3,2],[1,3]])
        0
        '''
        ys: Dict[int, List[int]] = {} 
        xs: Dict[int, List[int]] = {}

        for x, y in buildings:
            if not y in ys:
                ys[y] = [n, 0]
            
            if not x in xs:
                xs[x] = [n, 0]
            
            ys[y][0] = min(ys[y][0], x)
            ys[y][1] = max(ys[y][1], x)

            xs[x][0] = min(xs[x][0], y)
            xs[x][1] = max(xs[x][1], y)

        res = 0
        for x,y in buildings:
            minX, maxX = ys[y]
            minY, maxY = xs[x]

            if x > minX and x < maxX and y > minY and y < maxY:
                res += 1
        
        return res

if __name__ == "__main__":
    doctest.testmod()