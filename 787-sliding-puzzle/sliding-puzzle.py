from collections import deque 
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        start = ""
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])

        target = "123450"

        q = deque()
        q.append(start)

        swap = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        visited = set()
        visited.add(start)
        level = 0

        while q:
            n = len(q)

            for i in range(n):
                curr = q.popleft()

                if curr == target:
                    return level

                idx = curr.index('0')

                for swap_idx in swap[idx]:  # Changed variable name from 'i' to 'swap_idx'
                    s_list = list(curr)  # Create list from curr, not new_state

                    s_list[idx], s_list[swap_idx] = s_list[swap_idx], s_list[idx]

                    new_state = "".join(s_list)

                    if new_state not in visited:
                        visited.add(new_state)
                        q.append(new_state)

            level += 1  # Moved inside while loop, outside for loop

        return -1