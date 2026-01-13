from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        q = deque()
        visited = set()
        visited.add(start)
        q.append([start, 0])

        while q:

            curr, step = q.popleft()

            if curr == goal:
                return step

            if curr < 0 or curr > 1000:
                continue

            for i in nums:

                # addition
                nxt = curr + i
                if nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, step + 1])

                # subtraction
                nxt = curr - i
                if nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, step + 1])

                # xor
                nxt = curr ^ i
                if nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, step + 1])

                
        return -1