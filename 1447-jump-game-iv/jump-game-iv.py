from collections import deque
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1:  # Added edge case
            return 0
        
        map_freq = {}

        # Fixed: Remove nested loop
        for i in range(n):
            if arr[i] not in map_freq:
                map_freq[arr[i]] = []
            map_freq[arr[i]].append(i)

        q = deque()
        visited = set()
        q.append(0)  # Changed: Only store index
        visited.add(0)

        steps = 0  # Changed: Track steps outside queue

        while q:
            n = len(q)

            for i in range(n):
                curr = q.popleft()  # Changed: Only get index

                if curr == len(arr)-1:
                    return steps

                prev = curr-1
                next_step = curr+1

                if prev >= 0 and prev not in visited:
                    q.append(prev)  # Changed: Only append index
                    visited.add(prev)

                if next_step < len(arr) and next_step not in visited:
                    q.append(next_step)  # Changed: Only append index
                    visited.add(next_step)

                # Changed: Check if value exists in map before accessing
                if arr[curr] in map_freq:
                    for idx in map_freq[arr[curr]]:  # Changed: Renamed variable
                        if idx not in visited:
                            q.append(idx)  # Changed: Only append index
                            visited.add(idx)
                    
                    # CRITICAL: Delete after using to avoid TLE
                    del map_freq[arr[curr]]

            steps += 1  # Changed: Moved inside while loop

        return -1