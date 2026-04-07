from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        length_at_index = [0] * (n + 2)
        count_of_length = [0] * (n + 1)

        res = -1

        for step, index in enumerate(arr):
            left = length_at_index[index - 1]
            right = length_at_index[index + 1]

            new_len = left + right + 1

            # update boundaries
            length_at_index[index] = new_len
            length_at_index[index - left] = new_len
            length_at_index[index + right] = new_len

            # remove old groups
            if left > 0:
                count_of_length[left] -= 1
            if right > 0:
                count_of_length[right] -= 1

            # add new group
            count_of_length[new_len] += 1

            # check condition
            if count_of_length[m] > 0:
                res = step + 1

        return res