import heapq

# Определение графа в виде словаря смежности
graph = {
    1: [(2, 2), (3, 13), (4, 25), (5, 17)],
    2: [(4, 3), (5, 6)],
    3: [(6, 7),(4,5)], #Последнюю скобку сделал по своему желанию, тк не было инфрмации в графе
    4: [(7, 35), (6, 4),(5,20)],  #Последнюю скобку сделал по своему желанию, тк не было инфрмации в графе
    5: [(7, 20)],
    6: [(7, 5)],
    7: []
}

def spis (graph, start, end):
    # Начальная инициализация
    queue = [(0, start)]  # (стоимость, вершина)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}  # Для восстановления пути

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Если мы достигли конечной вершины, можно завершить
        if current_node == end:
            break

        # Проверяем всех соседей текущей вершины
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Если найден более короткий путь к соседу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Восстановление пути
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()

    return distances[end], path

# Пример поиска кратчайшего пути от вершины 1 к вершине 6
shortest_distance, shortest_path = spis(graph, 1, 7)
print("Кратчайшее расстояние:", shortest_distance)

print("Кратчайший путь:", shortest_path)
