class Garden:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id, data):
        self.nodes[node_id] = data

    def remove_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
