from collections import defaultdict
class Sol:
    def diagonal_traverse(self,matrix):
        m,n = len(matrix),len(matrix[0])
        res = []
        elements = defaultdict(list)

        for i in range(m):
            for j in range(n):
                elements[i+j].append(matrix[i][j])

        for k,v in elements.items():
            if k % 2 == 0:
                res.extend(v[::-1])
            else:
                res.extend(v)

        return res




o = Sol()
nums = [[1,2,3],[4,5,6],[7,8,9]]

print(o.diagonal_traverse(nums))