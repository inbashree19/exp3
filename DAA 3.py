import heapq

# ---------- Union Find for Kruskal ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        self.parent[py] = px
        return True


# ---------- Kruskal's Algorithm ----------
def kruskal(n, edges):
    edges.sort()  # Sort by weight

    mst = []
    cost = 0
    uf = UnionFind(n)

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

    return mst, cost


# ---------- Prim's Algorithm ----------
def prim(n, adj):
    visited = [False] * n
    pq = [(0, 0, -1)]  # (weight, vertex, parent)

    mst = []
    cost = 0

    while pq:
        w, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, w))
            cost += w

        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (wt, v, u))

    return mst, cost


# ---------- Runtime Input ----------
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
adj = {i: [] for i in range(n)}

print("\nEnter Edge Details:")

for i in range(e):
    print(f"\nEdge {i+1}:")
    u = int(input("Source Vertex = "))
    v = int(input("Destination Vertex = "))
    w = int(input("Weight = "))

    edges.append((w, u, v))
    adj[u].append((v, w))
    adj[v].append((u, w))


# ---------- Kruskal Output ----------
k_mst, k_cost = kruskal(n, edges[:])

print("\n===== KRUSKAL'S MST =====")
for u, v, w in k_mst:
    print(f"Edge ({u} - {v}) Weight = {w}")

print("Total MST Cost =", k_cost)


# ---------- Prim Output ----------
p_mst, p_cost = prim(n, adj)

print("\n===== PRIM'S MST =====")
for u, v, w in p_mst:
    print(f"Edge ({u} - {v}) Weight = {w}")

print("Total MST Cost =", p_cost)
