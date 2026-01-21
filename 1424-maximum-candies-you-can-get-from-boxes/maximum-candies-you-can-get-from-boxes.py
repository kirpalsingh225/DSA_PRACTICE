from collections import deque
from typing import List
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        visited = set()
        q = deque()
        keys_list = set()
        found_boxes = set()
        total_Candies = 0

        for i in initialBoxes: # inserted those which we can open 
            found_boxes.add(i)
            if status[i] == 1:
                q.append(i)
                visited.add(i)
                total_Candies+=candies[i]

        


        while q:

            curr = q.popleft()


            for neighbor in containedBoxes[curr]:
                found_boxes.add(neighbor)
                if status[neighbor] == 1 and neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                    total_Candies+=candies[neighbor]

            
            for key in keys[curr]:
                status[key] = 1 #can be opened in future

                if key in found_boxes and key not in visited:
                    q.append(key)
                    visited.add(key)
                    total_Candies+=candies[key]



        return total_Candies