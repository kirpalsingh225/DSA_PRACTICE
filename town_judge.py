def findJudge(n, trust):
    indegree = [0] * (n + 1)
    outdegree = [0] * (n + 1)

    for a, b in trust:
        outdegree[a] += 1   # a trusts someone
        indegree[b] += 1    # b is trusted by someone

    for person in range(1, n + 1):
        if indegree[person] == n - 1 and outdegree[person] == 0:
            return person

    return -1


# Example
n = 3
trust = [[1, 3], [2, 3]]

print(findJudge(n, trust))
