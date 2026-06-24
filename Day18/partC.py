def dfs(self, start):
        visited = set()
        dfs_order = []
        
        def dfs_helper(node):
            visited.add(node)
            dfs_order.append(node)
            
            # Recursively visit unvisited neighbors
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
                    
        if start in self.adj_list:
            dfs_helper(start)
        return dfs_order