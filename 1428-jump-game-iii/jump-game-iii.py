from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        q = deque()
        visited = set()

        q.append(start)
        visited.add(start)

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            next_step = arr[curr] + curr
            prev_step = curr - arr[curr]

            if next_step not in visited and 0 <= next_step <= len(arr)-1 :
                visited.add(next_step)
                q.append(next_step)

            if prev_step not in visited and 0 <= prev_step <= len(arr)-1 :
                visited.add(prev_step)
                q.append(prev_step)

        
        return False