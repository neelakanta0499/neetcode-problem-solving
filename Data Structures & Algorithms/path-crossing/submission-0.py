class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
            "N": [0,1],
            "S": [0,-1],
            "E": [1,0],
            "W": [-1,0]
        }
        seen = set()
        x = y = 0
        for d in path:
            seen.add((x, y))
            dx, dy = dir[d]
            x, y = dx+x, dy+y
            if (x, y) in seen:
                return True
        return False