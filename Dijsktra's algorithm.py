from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
        

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")
if __name__ == "__main__":
    edges = [
        ("A", "B", 2),
        ("A", "G", 6),
        ("B", "C", 7),
        ("B", "E", 2),
        ("B", "A", 2),
        ("C", "F", 3), 
        ("C", "D", 3),
        ("E", "F", 2),
        ("E", "G", 1),
        ("E", "B", 2),
        ("F", "E", 2),
        ("F", "H", 2),
        ("G", "H", 4),
        ("H", "D", 2),
        ("H", "F", 2),
        ("D", "C", 3),
        ("D", "H", 2)
    ]
    for x in range (len(edges)):
        print "Path:",edges[x] 
    print "A -> D:"
    print dijkstra(edges, "A", "D")
