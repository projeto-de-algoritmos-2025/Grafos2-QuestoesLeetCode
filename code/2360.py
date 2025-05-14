from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        length = -1
        time = 1
        visited = [0] * len(edges)

        for i in range(len(edges)):
            if visited[i]:
                continue
            start = time
            u = i
            while u != -1 and not visited[u]: 
                visited[u] = time  
                time += 1  
                u = edges[u]  
            if u != -1 and visited[u] >= start:  
                length = max(length, time - visited[u])  

        return length 
        
        