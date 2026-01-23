from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        L = len(beginWord)
        wordSet = set(wordList)
        wordSet.add(beginWord)

        # Build pattern -> words mapping, e.g. "*ot" -> ["hot","dot","lot"]
        pattern_map = defaultdict(list)
        for w in wordSet:
            for i in range(L):
                pattern = w[:i] + '*' + w[i+1:]
                pattern_map[pattern].append(w)

        # BFS to build parents map (predecessors)
        parents = defaultdict(list)  # child_word -> list of parent words
        level = {beginWord: 0}
        q = deque([beginWord])
        found_level = None

        while q:
            curr = q.popleft()
            curr_level = level[curr]
            # stop exploring deeper than the first time we reach endWord
            if found_level is not None and curr_level >= found_level:
                continue

            for i in range(L):
                pattern = curr[:i] + '*' + curr[i+1:]
                for nei in pattern_map[pattern]:
                    if nei not in level:  # first time visited -> set level and parent
                        level[nei] = curr_level + 1
                        parents[nei].append(curr)
                        q.append(nei)
                        if nei == endWord:
                            found_level = curr_level + 1
                    else:
                        # if this neighbor is at the same level as we'd assign now,
                        # it is another shortest-path parent
                        if level[nei] == curr_level + 1:
                            parents[nei].append(curr)

        # If endWord never reached
        if endWord not in parents and endWord != beginWord:
            return []

        # Backtrack (DFS) from endWord to beginWord using parents map
        res = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                res.append(path[::-1])  # reverse path
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        # Special case: beginWord == endWord
        if beginWord == endWord:
            return [[beginWord]]

        # If endWord has parents, call dfs
        if parents.get(endWord):
            dfs(endWord)
        return res
