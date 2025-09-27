class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        visited={(0,0)}
        for point in path:
            if point=='N':
                y+=1
            elif point=='S':
                y-=1
            elif point=='E':
                x+=1
            elif point=='W':
                x-=1
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False
        