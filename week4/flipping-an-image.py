class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        for r in range(rows):
            image[r].reverse()
        for r in range(rows):
            for c in range(cols):
                if image[r][c]==1:
                    image[r][c]=0
                else:
                    image[r][c]=1
        return image

        