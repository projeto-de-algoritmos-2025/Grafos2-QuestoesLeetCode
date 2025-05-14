from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [False] * n
        for edge in edges:
            from_node = edge[0]
            to_node = edge[1]
            incoming[to_node] = True

        result = []
        for i in range(n):
            if not incoming[i]:  
                result.append(i)

        return result
    