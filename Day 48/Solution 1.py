class Solution:
    def cloneGraph(self, node):
        if node == None:
            return None
        clone_root = UndirectedGraphNode(node.label)
        visited = {node: clone_root}
        stk = [(node, clone_root)]
        while stk:
            curr_node, clone_node = stk.pop()
            for node in curr_node.neighbors:
                if node in visited:
                    clone_node.neighbors.append(visited[node])
                else:
                    new_node = UndirectedGraphNode(node.label)
                    visited[node] = new_node
                    clone_node.neighbors.append(new_node)
                    stk.append((node, new_node))

    return clone_root
