def find_back_edges():
    verts = [0, 1, 2, 3, 4]
    edges = {0: [1, 2], 1: [3], 2: [3, 1], 3: [4, 1], 4: [2]}
    explored = set()
    source = verts[0]
    current_path = set([source])
    def DFS(u): 
        explored.add(u)
        for v in edges[u]:
            if v in current_path:
                print(u, v)
            if not(v in explored):
                current_path.add(v)
                DFS(v)
        current_path.remove(u)
    DFS(source)

find_back_edges()