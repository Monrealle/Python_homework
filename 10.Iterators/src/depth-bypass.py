class Graph:
    def __init__(self):
        self._adjacency_list = {}
        self._start_vertex = None

    def add_vertex(self, vertex):
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = []
            if self._start_vertex is None:
                self._start_vertex = vertex
        return self

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self._adjacency_list[vertex1]:
            self._adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self._adjacency_list[vertex2]:
            self._adjacency_list[vertex2].append(vertex1)
        return self

    def set_start_vertex(self, vertex):
        if vertex in self._adjacency_list:
            self._start_vertex = vertex
        return self

    def dfs(self, start_vertex=None):
        if not self._adjacency_list:
            return []

        if start_vertex is None:
            start_vertex = self._start_vertex

        if start_vertex not in self._adjacency_list:
            raise ValueError(f"Вершина {start_vertex} не существует в графе")

        visited = []
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in reversed(self._adjacency_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

    def __iter__(self):
        self._dfs_visited = []
        self._dfs_stack = []

        if self._start_vertex and self._adjacency_list:
            self._dfs_stack.append(self._start_vertex)

        return self

    def __next__(self):
        while self._dfs_stack:
            vertex = self._dfs_stack.pop()
            if vertex not in self._dfs_visited:
                self._dfs_visited.append(vertex)
                for neighbor in reversed(self._adjacency_list.get(vertex, [])):
                    if neighbor not in self._dfs_visited:
                        self._dfs_stack.append(neighbor)
                return vertex

        for vertex in self._adjacency_list:
            if vertex not in self._dfs_visited:
                self._dfs_stack.append(vertex)
                return self.__next__()

        raise StopIteration


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B').add_edge('B', 'C').add_edge('A', 'D')

    print("DFS обход от A:", g.dfs('A'))

    print("Итерация по графу:")
    for vertex in g:
        print(vertex)
