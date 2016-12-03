
#http://www.cs.cmu.edu/~ckingsf/class/02713-s13/src/mst.py
#=======================================================================
# Union-Find
#=======================================================================

class ArrayUnionFind:
    """Holds the three "arrays" for union find"""
    def __init__(self, S):
        self.group = dict((s,s) for s in S) # group[s] = id of its set
        self.size = dict((s,1) for s in S) # size[s] = size of set s
        self.items = dict((s,[s]) for s in S) # item[s] = list of items in set s
        
def make_union_find(S):
    """Create a union-find data structure"""
    return ArrayUnionFind(S)
    
def find(UF, s):
    """Return the id for the group containing s"""
    return UF.group[s]

def union(UF, a,b):
    """Union the two sets a and b"""
    assert a in UF.items and b in UF.items
    # make a be the smaller set
    if UF.size[a] > UF.size[b]:
        a,b = b,a
    # put the items in a into the larger set b
    for s in UF.items[a]:
        UF.group[s] = b
        UF.items[b].append(s)
    # the new size of b is increased by the size of a
    UF.size[b] += UF.size[a]
    # remove the set a (to save memory)
    del UF.size[a]
    del UF.items[a]

#=======================================================================
# Kruskal MST
#=======================================================================

def kruskal_mst(G, Edges):
    """Return a minimum spanning tree using kruskal's algorithm"""
    # sort the list of edges in G by their length
    #Edges = [(u, v, G[u][v]['length']) for u,v in G.edges()]
    #Edges.sort(cmp=lambda x,y: cmp(x[2],y[2]))

    UF = make_union_find(G)  # union-find data structure

    # for edges in increasing weight
    mst = [] # list of edges in the mst
    for e in Edges:
        setu = find(UF, e[0])
        setv = find(UF, e[1])
        # if u,v are in different components
        if setu != setv:
            mst.append((e[0],e[1]))
            union(UF, setu, setv)
            #snapshot_kruskal(G, mst)
	if len(mst)==len(G)-1:
	    return mst	
    return mst
