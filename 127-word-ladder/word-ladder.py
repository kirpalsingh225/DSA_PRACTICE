from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        if endWord not in wordList:
            return 0

        test = "abcdefghijklmnopqrstuvwxyz"

        q = deque()
        visited = set(wordList)
        visited.add(beginWord)
        q.append(beginWord)
        level = 1

        while q:
            n = len(q)

            for i in range(n):
                curr_word = q.popleft()

                if curr_word == endWord:
                    return level

                for i in range(len(curr_word)):
                    for c in test:
                        copy_curr_word = curr_word

                        copy_curr_word = curr_word[:i] + c + curr_word[i+1:]
                        
                        if copy_curr_word in visited:
                            q.append(copy_curr_word)
                            visited.remove(copy_curr_word)

            level+=1

        return 0





            
