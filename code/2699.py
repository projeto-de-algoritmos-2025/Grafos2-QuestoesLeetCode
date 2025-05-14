from collections import defaultdict
import heapq
from typing import List

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(dict)
        negative_edges = set()

        for u, v, w in edges:
            if w == -1:
                negative_edges.add((u, v))
                negative_edges.add((v, u))
                w = 1  
            graph[u][v] = w
            graph[v][u] = w

        def find_path():
            heap = [(0, 0, [source])] 
            while heap:
                neg_count, total_value, path = heapq.heappop(heap)
                current = path[-1]

                if current == destination:
                    if total_value == target or neg_count > 0:
                        return path, total_value
                    break

                for neighbor in graph[current]:
                    if neighbor in path:  
                        continue
                    new_neg_count = neg_count + (1 if (current, neighbor) in negative_edges else 0)
                    new_value = total_value + graph[current][neighbor]
                    if new_value <= target:
                        heapq.heappush(heap, (new_neg_count, new_value, path + [neighbor]))

            return None, 0

        
        valid_path, path_value = find_path()
        if not valid_path:
            return []

       
        remaining = target - path_value
        path_edges = set()
        for i in range(len(valid_path) - 1):
            path_edges.add((valid_path[i], valid_path[i + 1]))
            path_edges.add((valid_path[i + 1], valid_path[i]))

        result = []
        for u, v, w in edges:
            if w != -1:
                result.append([u, v, w])  
            elif (u, v) in path_edges:
                result.append([u, v, 1 + remaining]) 
                remaining = 0
            else:
                result.append([u, v, 2 * (10**9)]) 
        return result