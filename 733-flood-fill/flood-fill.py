class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r, c = len(image), len(image[0])


        for i in range(r):
            for j in range(c):
                if sr == i and sc == j:
                    prevColor = image[i][j]
                    if prevColor == color:
                        return image
                    self.dfs(image, i, j, color, prevColor, r, c)

        return image


    def dfs(self, image, i, j, color, prevColor, r, c):
        if i >= r or i < 0 or j >= c or j < 0 or image[i][j]!=prevColor:
            return

        image[i][j] = color
        self.dfs(image, i+1, j, color, prevColor, r, c)
        self.dfs(image, i-1, j, color, prevColor, r, c)
        self.dfs(image, i, j+1, color, prevColor, r, c)
        self.dfs(image, i, j-1, color, prevColor, r, c)
