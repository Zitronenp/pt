def print_way(w,v):
    print(end="   ")
    for i in v: print(i,end=" ")
    print("\n")
    for i in v:
        print(i,end=": ")
        for j in v:
            if (i,j) in w: print(1,end=" ")
            else: print(0,end=" ")
        print("\n")





graf = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}

visit = set()
way = set()
def dfs(p):
    if p in visit:
        return
    visit.add(p)
    for i in graf[p]:
        way.add((p, i))
        if i not in visit:
            dfs(i)
dfs(1)
print_way(way,visit)





visit2 = set()
way2 = set()
q=[]

def bfs(p):
    if p in visit2: return
    visit2.add(p)
    for i in graf[p]:
        way2.add((p,i))
        if i not in visit2:
            q.append(i)
    while q:
        bfs(q.pop(0))
bfs(1)
print_way(way2,visit2)














