import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    n, m, q = map(int, sys.stdin.readline().split())
    total_nodes = n + m
    parent = list(range(total_nodes + 1))  # 1-based indexing
    rank = [1] * (total_nodes + 1)
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if rank[u_