import re
import random
def load_graph():
    graph ={}
    with open('./kargerMinCut.txt') as f:
        lines = f.readlines()
    lines = map(lambda s: re.sub('\s+',' ',str(s.strip('\r\n'))).strip(),lines)

    lines = map(lambda s: s.split(' '),lines)
    for i in lines:
        graph[int(i[0])] = list(map(lambda l:int(l),i[1:]))
    return graph

def get_random_edge(graph):
    v0 = list(graph.keys())[random.randint(0,len(graph)-1)]
    v1 = graph[v0][random.randint(0,len(graph[v0])-1)]
    return [v0,v1]

def contract_edge():
    global graph
    v = get_random_edge(graph)
    vlist = graph[v[0]]
    vlist.extend(graph[v[1]])
    del graph[v[1]]
    for k in graph:
        '''for j in range(len(graph[k])):
            if graph[k][j] == v[1]:
                graph[k][j] = v[0]'''
                
        graph[k] = [v[0] if x==v[1] else x for x in graph[k]]
    graph[v[0]] = [x for x in graph[v[0]] if x!=v[0]]



minlist = []

for i in range(20):
    graph = load_graph()
    while len(graph)>2:
        contract_edge()
    minlist.append(len(graph[list(graph.keys())[0]]))
print(min(minlist))
