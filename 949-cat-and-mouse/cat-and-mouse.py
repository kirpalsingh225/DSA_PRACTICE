class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        
        # color[mouse][cat][turn] = outcome
        # turn: 0 = mouse's turn, 1 = cat's turn
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        
        # Calculate degrees (number of possible moves from each state)
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len([x for x in graph[c] if x != 0])
        
        # Queue for BFS
        queue = deque()
        
        # Initialize winning/losing states
        for i in range(n):
            for t in range(2):
                # Mouse wins
                color[0][i][t] = MOUSE_WIN
                queue.append((0, i, t, MOUSE_WIN))
                
                # Cat wins (cat catches mouse, but not at hole)
                if i > 0:
                    color[i][i][t] = CAT_WIN
                    queue.append((i, i, t, CAT_WIN))
        
        # BFS to propagate results
        while queue:
            mouse, cat, turn, result = queue.popleft()
            
            if mouse == 1 and cat == 2 and turn == 0:
                return result
            
            # Work backwards: who could have moved to this state?
            if turn == 0:  # Current state is mouse's turn, so previous was cat's turn
                for prev_cat in graph[cat]:
                    if prev_cat == 0:
                        continue
                    if color[mouse][prev_cat][1] > 0:
                        continue
                    
                    if result == CAT_WIN:
                        color[mouse][prev_cat][1] = CAT_WIN
                        queue.append((mouse, prev_cat, 1, CAT_WIN))
                    else:
                        degree[mouse][prev_cat][1] -= 1
                        if degree[mouse][prev_cat][1] == 0:
                            color[mouse][prev_cat][1] = MOUSE_WIN
                            queue.append((mouse, prev_cat, 1, MOUSE_WIN))
            else:  # Current state is cat's turn, so previous was mouse's turn
                for prev_mouse in graph[mouse]:
                    if color[prev_mouse][cat][0] > 0:
                        continue
                    
                    if result == MOUSE_WIN:
                        color[prev_mouse][cat][0] = MOUSE_WIN
                        queue.append((prev_mouse, cat, 0, MOUSE_WIN))
                    else:
                        degree[prev_mouse][cat][0] -= 1
                        if degree[prev_mouse][cat][0] == 0:
                            color[prev_mouse][cat][0] = CAT_WIN
                            queue.append((prev_mouse, cat, 0, CAT_WIN))
        
        return color[1][2][0]