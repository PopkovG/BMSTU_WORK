def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def build_graph(lines):
    graph = {}
    for line in lines:
        if '->' in line:
            node, target = line.split('->')
            if node not in graph:
                graph[node] = []
            graph[node].append(target)
            continue
        elif '-' in line:
            node1, node2 = line.split('-')
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
    return graph

class RingTopology:
