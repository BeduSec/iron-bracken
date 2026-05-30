class NetworkTopology:
    def __init__(self):
        self.graph = {}

    def add_link(self, src, dst):
        if src not in self.graph:
            self.graph[src] = []
        self.graph[src].append(dst)

    def is_accessible(self, target):
        return target in self.graph
