from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # solution bfs
        if len(rooms) == 1:
            return True

        visited = set()
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            node = q.popleft()

            for neighbor in rooms[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        
        if len(visited) == len(rooms):
            return True

        return False
        