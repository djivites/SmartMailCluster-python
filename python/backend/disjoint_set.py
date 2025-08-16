class DisjointSet:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.size = [1] * size
        self.n = size

    def find_upar(self, x: int) -> int:
        
        if self.parent[x] != x:
            self.parent[x] = self.find_upar(self.parent[x])
        return self.parent[x]

    def union_by_rank(self, u: int, v: int):
        
        root_u = self.find_upar(u)
        root_v = self.find_upar(v)

        if root_u == root_v:
            return

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_v] < self.rank[root_u]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

    def union_by_size(self, u: int, v: int):
        
        root_u = self.find_upar(u)
        root_v = self.find_upar(v)

        if root_u == root_v:
            return 

        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
