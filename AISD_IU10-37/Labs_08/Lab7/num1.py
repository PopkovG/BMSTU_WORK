class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Количество вершин
        self.graph = {i: [] for i in range(vertices)}  # Список смежности

    # Добавление ребра
    def add_edge(self, u, v):
        if u < self.vertices and v < self.vertices:
            self.graph[u].append(v)
            self.graph[v].append(u)

    # Поиск в глубину (DFS)
    def dfs(self, start):
        visited = [False] * self.vertices
        stack = []
        result = []

        def dfs_util(v):
            visited[v] = True
            result.append(v)
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start)

        return result

    # Поиск в ширину (BFS)
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = [start]
        visited[start] = True
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    # Нахождение эйлерова цикла (если он существует)
    def find_eulerian_cycle(self):
        if not self.is_eulerian():
            return "Граф не имеет эйлерова цикла"

        stack = []
        cycle = []
        current = 0  # Начинаем с любой вершины, например 0

        stack.append(current)

        while stack:
            u = stack[-1]
            if self.graph[u]:
                v = self.graph[u].pop()  # Берем одно из ребер
                self.graph[v].remove(u)  # Убираем обратное ребро
                stack.append(v)
            else:
                cycle.append(stack.pop())

        return cycle[::-1]  # Эйлеров цикл

    # Проверка, является ли граф эйлеровым
    def is_eulerian(self):
        odd_degree_count = 0
        for v in self.graph:
            if len(self.graph[v]) % 2 != 0:
                odd_degree_count += 1
        return odd_degree_count == 0

    # Нахождение гамильтонова цикла (с использованием перебора с возвратом)
    def find_hamiltonian_cycle(self):
        path = []

        def hamiltonian_util(v, path):
            if len(path) == self.vertices:
                return path[0] in self.graph[v]  # Если последний элемент соединен с первым

            for neighbor in self.graph[v]:
                if neighbor not in path:
                    path.append(neighbor)
                    if hamiltonian_util(neighbor, path):
                        return True
                    path.pop()
            return False

        # Пробуем начать с каждой вершины
        for start in range(self.vertices):
            path = [start]
            if hamiltonian_util(start, path):
                return path + [start]

        return "Гамильтонов цикл не найден"

    # Алгоритм Дейкстры
    def dijkstra(self, start):
        import heapq
        distances = [float('inf')] * self.vertices
        distances[start] = 0
        pq = [(0, start)]  # (расстояние, вершина)

        while pq:
            current_distance, u = heapq.heappop(pq)

            if current_distance > distances[u]:
                continue

            for v in self.graph[u]:
                distance = current_distance + 1  # Для неориентированного графа вес ребра равен 1
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))

        return distances


def main():
    print("Введите количество вершин в графе: ", end="")
    vertices = int(input())

    graph = Graph(vertices)

    while True:
        print("\nМеню:")
        print("1. Добавить ребро")
        print("2. Поиск в глубину")
        print("3. Поиск в ширину")
        print("4. Нахождение эйлерова цикла")
        print("5. Нахождение гамильтонова цикла")
        print("6. Алгоритм Дейкстры")
        print("7. Выход")
        choice = int(input())

        if choice == 1:
            print("Введите вершины для добавления ребра (u v): ", end="")
            u, v = map(int, input().split())
            graph.add_edge(u, v)
            print(f"Ребро ({u}, {v}) добавлено.")

        elif choice == 2:
            print("Введите стартовую вершину для DFS: ", end="")
            start = int(input())
            print("Результат DFS:", graph.dfs(start))

        elif choice == 3:
            print("Введите стартовую вершину для BFS: ", end="")
            start = int(input())
            print("Результат BFS:", graph.bfs(start))

        elif choice == 4:
            print("Результат нахождения эйлерова цикла:", graph.find_eulerian_cycle())

        elif choice == 5:
            print("Результат нахождения гамильтонова цикла:", graph.find_hamiltonian_cycle())

        elif choice == 6:
            print("Введите стартовую вершину для алгоритма Дейкстры: ", end="")
            start = int(input())
            print("Результат алгоритма Дейкстры:", graph.dijkstra(start))

        elif choice == 7:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
