from collections import deque


class Graph:
    def __init__(self, adj_list=None):
        self.adj_list = adj_list or {}

    def bfs(self, start):
        if start not in self.adj_list:
            return []

        visited = set()
        queue = deque([start])
        visited.add(start)
        bfs_order = []

        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            # Check neighbors
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_order