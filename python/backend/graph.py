from collections import deque

class Graph:
    def __init__(self, n: int):
        self.num_emails = n
        self.adj = [[] for _ in range(n)]  

    def add_edge(self, from_email: int, to_email: int):
        self.adj[from_email].append(to_email)

    def get_neighbours(self, email_id: int):
        return self.adj[email_id]

    def bfs(self, start_email: int):
        visited = [False] * self.num_emails
        q = deque()

        visited[start_email] = True
        q.append(start_email)

        while q:
            email = q.popleft()
            print(email, end=" ")

            for neighbour in self.adj[email]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True
        print()

    def dfs(self, start_email: int):
        visited = [False] * self.num_emails

        def dfs_helper(email: int):
            visited[email] = True
            print(email, end=" ")

            for neighbour in self.adj[email]:
                if not visited[neighbour]:
                    dfs_helper(neighbour)

        dfs_helper(start_email)
        print()
