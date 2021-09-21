# Dictionary Format: {Node:data}

class Node:
    def __init__(self, data):
        self.neighbors = {}

    def __repr__(self):
        return f"NODE"


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data):
        self.nodes[Node(data)] = data

    # Gets node for given value
    def get_node(self,val):
        for node in self.nodes:
            if self.nodes[node] == val:
                return node
        print("[Error] Node not found")
        return None

    def add_edge(self, value1, value2):
        node1 = self.get_node(value1)
        node2 = self.get_node(value2)
        if node1 and node2:
            node1.neighbors[node2] = value2
            node2.neighbors[node1] = value1
        else:
            print("[Error] Both nodes were not found")

    def dfs(self,val,node=None,prev_node=None):
        if node is None: node = list(self.nodes.keys())[0]
        print(node,self.nodes[node])
        if self.nodes[node] == val: return True

        children = node.neighbors
        if prev_node: del children[prev_node]

        found_flag = False
        for child_node in children:
            found_flag = self.dfs(val,child_node,node)
            if found_flag is True: return True
        return False

    def bfs(self,val,node=None):
        if node is None: node = list(self.nodes.keys())[0]
        if self.nodes[node] == val: return True
        found_nodes = {node: self.nodes[node]}

        is_done = False
        while not is_done:
            is_done = True
            print(found_nodes)
            for found_node in list(found_nodes):
                child_nodes = dict(found_node.neighbors.items() - found_nodes.items())
                if child_nodes: is_done = False
                for child_node in child_nodes:
                    if child_nodes[child_node] == val: return True
                    found_nodes[child_node] = child_nodes[child_node]
        return False



