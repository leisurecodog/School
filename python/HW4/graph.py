class Graph():
    def __init__(self):
        self.lst_vertex = []
        self.lst_edge = []
        self.paths = []

    def add_vertex(self, name):
        if name in self.lst_vertex:
            print('A vertex with name ' + name + ' already exists')
        else:
            self.lst_vertex.append(name)

    def vertices(self):
        return sorted(self.lst_vertex)

    def add_edge(self, start, end):
        if start not in self.lst_vertex:
            self.lst_vertex.append(start)
        if end not in self.lst_vertex:
            self.lst_vertex.append(end)
        strtmp = (start, end)
        self.lst_edge.append(strtmp)

    def remove_vertex(self, name):
        if name not in self.lst_vertex:
            return
        del self.lst_vertex[self.lst_vertex.index(name)]
        for edge in sorted(self.lst_edge):
            if name in edge:
                del self.lst_edge[self.lst_edge.index(edge)]

    def print_edges(self):
        for edge in sorted(self.lst_edge):
            print(edge[0] + ' -> ' + edge[1])

    def remove_edge(self, start, end):
        if (start, end) not in self.lst_edge:
            return
        del self.lst_edge[self.lst_edge.index((start, end))]

    def is_connected(self, start, end):
        return (start, end) in self.lst_edge

    def print_paths(self, start, end):
        if start == end:
            print(' -> '.join(self.paths + [end]))
            return
        for edge in sorted(self.lst_edge):
            if edge[0] == start and start not in self.paths:
                self.paths.append(start)
                self.print_paths(edge[1], end)
                self.paths.pop()


class UndirectedGraph():
    def __init__(self):
        self.lst_vertex = []
        self.lst_edge = []
        self.paths = []

    def add_vertex(self, name):
        if name in self.lst_vertex:
            print('A vertex with name ' + name + ' already exists')
        else:
            self.lst_vertex.append(name)

    def vertices(self):
        return sorted(self.lst_vertex)

    def add_edge(self, start, end):
        if start not in self.lst_vertex:
            self.lst_vertex.append(start)
        if end not in self.lst_vertex:
            self.lst_vertex.append(end)
        if start > end:
            start, end = end, start
        strtmp = (start, end)
        self.lst_edge.append(strtmp)

    def remove_vertex(self, name):
        if name not in self.lst_vertex:
            return
        del self.lst_vertex[self.lst_vertex.index(name)]
        for edge in sorted(self.lst_edge):
            if name in edge:
                del self.lst_edge[self.lst_edge.index(edge)]

    def print_edges(self):
        for edge in sorted(self.lst_edge):
            print(edge[0] + ' <-> ' + edge[1])

    def remove_edge(self, start, end):
        if start > end:
            start, end = end, start
        if (start, end) not in self.lst_edge:
            return
        del self.lst_edge[self.lst_edge.index((start, end))]

    def is_connected(self, start, end):
        return (start, end) in self.lst_edge or (end, start) in self.lst_edge

    def print_paths(self, start, end):
        if start == end:
            print(' <-> '.join(self.paths + [end]))
            return
        for edge in sorted(self.lst_edge):
            if edge[0] == start and start not in self.paths:
                self.paths.append(start)
                self.print_paths(edge[1], end)
                self.paths.pop()
