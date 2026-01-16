class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        if x==y:
            return 0

        
        visited = set()
        q = deque()

        q.append(x)
        visited.add(x)
        levels = 0

        while q:

            n = len(q)

            for i in range(n):
                curr = q.popleft()

                if curr==y:
                    return levels

                if curr%11==0 and curr%11 not in visited:
                    visited.add(curr//11)
                    q.append(curr//11)

                if curr%5==0 and curr%5 not in visited:
                    visited.add(curr//5)
                    q.append(curr//5)

                if curr+1 not in visited:
                    visited.add(curr+1)
                    q.append(curr+1)

                if curr-1 not in visited:
                    visited.add(curr-1)
                    q.append(curr-1)

            levels+=1


        return levels