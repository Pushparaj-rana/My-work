class graph:
    def __init__ (self,edges):
        self.edges = edges
        self.graph_dic = {}
        for start, end in edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start] = [end]
        print ("Graph routs :", self.graph_dic)

    def get_paths(self,start,end,path =[]):
        path = path + [start]

        if start == end:
            return [path]
        if start not in self.graph_dic:
            return []
        paths = []
        for node in self.graph_dic[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)

                for p in new_path:
                    paths.append(p)

        return paths
    
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dic:
            return []
        shortest_path = None
        for node in self.graph_dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)

                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
    






if __name__ == "__main__":

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = graph(routes)

    print(route_graph.get_paths("Mumbai","New York"))
    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

    

