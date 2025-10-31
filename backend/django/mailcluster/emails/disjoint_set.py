# backend/src/disjoint_set.py

class DisjointSet:
    def __init__(self, n: int):
        # parent[i] = parent of node i
        # rank[i]   = rank for union by rank
        # size[i]   = size for union by size
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        

    def find_upar(self, node: int) -> int:
        """Find ultimate parent with path compression"""
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u: int, v: int):
        """Union by rank"""
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)
        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

 
