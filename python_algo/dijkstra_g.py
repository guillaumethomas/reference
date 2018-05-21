from math import inf
import random
import string
from graphviz import Digraph


class Vertex():
    def __init__(self, name):
        self._name = name
        self.adjacent = {}

        # these attribute are specific to find the shortest of a graph

        self._dist_dij = inf
        self._visited_dij = False
        self._previous_dij = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dist_dij(self):
        return self._dist_dij

    @dist_dij.setter
    def dist_dij(self, dist):
        self._dist_dij = dist

    @property
    def visited_dij(self):
        return self._visited_dij

    @visited_dij.setter
    def visited_dij(self, Bool):
        self._visited_dij = Bool

    @property
    def previous_dij(self):
        return self._previous_dij

    @previous_dij.setter
    def previous_dij(self, Vertex):
        self._previous_dij = Vertex

    def connections(self):
        return self.adjacent.keys()

    def add_adjacent(self, name, distance=0):
        self.adjacent[name] = distance

    def __gt__(self, Vertex):
        if self.dist_dij > Vertex.dist_dij:
            return self
        return Vertex

    def __lt__(self, Vertex):
        if self.dist_dij < Vertex.dist_dij:
            return self
        return Vertex

    def __str__(self):
        lst = list(self.adjacent.keys())
        ret_str = '{} adjacent {}'.format(self.name, ", ".join(lst))
        return ret_str


class Graph():

    def __init__(self, Vertices={}):
        for Vert in Vertices.values():
            if isinstance(Vert, Vertex):
                self.vertices = Vertices
                self.edges = self.get_edges()
            else:
                self.vertices = {}
                self.edges = {}
                raise ValueError("Not a dic of Vertex")
        self.nb_vertices = len(self.vertices)

    def add_vertex(self, node):
        Vert = Vertex(node)
        self.vertices[node] = Vert
        self.nb_vertices += 1

    def get_vertices(self):
        return '\n'.join(list(self.vertices.keys()))

    def add_edge(self, start, to, dist):
        if start not in self.vertices.keys():
            self.add_vertex(start)
        if to not in self.vertices.keys():
            self.add_vertex(to)

        self.vertices[start].add_adjacent(to, dist)
        self.vertices[to].add_adjacent(start, dist)
        self.edges = self.get_edges()

    def get_edges(self):
        # return '\n'.join([str(i) for i in list(self.vertices.values())])
        edges = {}
        for vert in self.vertices.values():
            for key, value in vert.adjacent.items():
                str_a = '{}-{}'.format(vert.name, key)
                str_b = '{}-{}'.format(key, vert.name)
                if str_a not in edges.keys() and str_b not in edges.keys():
                    edges[str_a] = [(vert.name, key), value]
        return edges

    # def __repr__():
    #    pass

    def __iter__(self):
        return iter(self.vertices.values())

    def digraph(self, title, filename, dijs=None):
        f = Digraph(title, filename)
        f.attr(rankdir='LR', size='8.5')
        f.attr('node', shape='circle')
        f.attr('edge', arrowhead='none', weight='2')

        for vertex in self.vertices.keys():
            f.node(vertex)

        for edge in self.edges.values():
            f.edge(edge[0][0], edge[0][1], label=str(edge[1]))

        if dijs is not None:
            f.attr('edge', arrowhead='none', weight='2', color='red')
            new = [[dijs[i], dijs[i + 1]] for i in range(len(dijs) - 1)]
            for e in new:
                f.edge(e[0], e[1])

        f.view()

    def dijkstra(self, start, target):
        if isinstance(start, str):
            start = self.vertices[start]
        if isinstance(target, str):
            target = self.vertices[target]

        queue = self.vertices.copy()
        visited = {}
        # distance init is taking care by the object vertex
        start.dist_dij = 0
        while queue != {}:
            # work because of __iter__ method being set
            tmp = {i.name: i.dist_dij for i in queue.values()}
            # u = min(queue, key=queue.get)
            u = min(tmp, key=tmp.get)
            current = queue[u]
            current.visited_dij = True
            visited[u] = current
            queue.pop(u)

            for neigbhor, dist in current.adjacent.items():

                alt = current.dist_dij + dist
                if alt < self.vertices[neigbhor].dist_dij:
                    self.vertices[neigbhor].dist_dij = alt
                    self.vertices[neigbhor].previous_dij = current.name

        tmp = {key: [value.previous_dij, value.dist_dij]
               for key, value in self.vertices.items()}
        distance = tmp[target.name][1]
        bool = True
        path = [target.name, tmp[target.name][0]]
        c = tmp[target.name][0]
        while bool:
            if c != start.name:
                c = tmp[c][0]
                path.append(c)
            else:
                bool = False
        path.reverse()
        self.digraph('dij', 'dij.gv', path)

        return path, distance

'''
Test functions
'''


def random_name(length):
    char_set = string.ascii_letters + string.digits
    random_n = ''.join([random.choice(char_set) for n in range(length)])
    return random_n


def random_lst_vert(number):
    res = {}
    for _ in range(number):
        stop = True
        while stop:
            name = random_name(2)
            if name not in res.keys():
                stop = False
                vert = Vertex(name)
                res[name] = vert
    return res


def random_lst_connect(vertexs, nb_connections, max_length):
    lst_vertexs = list(vertexs.keys())
    for _ in range(nb_connections):
        vert_a = random.choice(lst_vertexs)
        tmp = lst_vertexs.copy()
        tmp.remove(vert_a)
        vert_b = random.choice(tmp)
        distance = random.randrange(1, max_length)
        vertexs[vert_a].add_adjacent(vert_b, distance)
        vertexs[vert_b].add_adjacent(vert_a, distance)
    return vertexs


def random_graph(nb_vert, nb_connection, max_distance):
    lst_vert = random_lst_vert(nb_vert)
    lst_vert = random_lst_connect(lst_vert, nb_connection, max_distance)
    graph = Graph(lst_vert)
    return graph


def get_2_rd_vertices(graph):
    a = list(graph.vertices.keys()).copy()
    vert1 = random.choice(a)
    a.remove(vert1)
    vert2 = random.choice(a)
    return [vert1, vert2]


def print_res(vertices, distance):
    print("\nDijsktra's shortest Path")
    print(' -> '.join(vertices))
    print('total distance {}\n'.format(distance))


if __name__ == "__main__":
    '''
    graph = random_graph(5, 4, 10)
    print(graph.get_vertices())
    print(graph.get_edges())
    graph.digraph('test', 'test.gv')
    rdm_verts = get_2_rd_vertices(graph)
    a, b = graph.dijkstra(*rdm_verts)

    print_res(a, b)
    '''

    vert_list = [Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d'),
                 Vertex('e'), Vertex('f'), Vertex('g')]
    vert_dict = {i.name: i for i in vert_list}

    graphb = Graph(vert_dict)
    graphb.add_edge('a', 'b', 5)
    graphb.add_edge('c', 'd', 3)
    graphb.add_edge('b', 'c', 4)
    graphb.add_edge('b', 'e', 1)
    graphb.add_edge('c', 'd', 2)
    graphb.add_edge('c', 'e', 1)
    graphb.add_edge('a', 'e', 12)
    graphb.add_edge('f', 'g', 8)
    graphb.add_edge('e', 'f', 4)
    graphb.add_edge('d', 'g', 1)
    graphb.add_edge('a', 'f', 1)

    graphb.digraph('b', 'b.gv')
    e, f = graphb.dijkstra('a', 'f')

    print_res(e, f)

