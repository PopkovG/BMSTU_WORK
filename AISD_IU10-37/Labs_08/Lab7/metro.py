import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Данные о линиях метро и времени движения между станциями
metro_map = {
    "Линия 1": {
        "Станция А": {"Станция Б": 3},
        "Станция Б": {"Станция А": 3, "Станция В": 4, "Станция Ш": 9},
        "Станция В": {"Станция Г": 4, "Станция Б": 4, "Станция Д": 2, "Станция Ю": 10},
        "Станция Г": {"Станция В": 4}
    },
    "Линия 2": {
        "Станция Д": {"Станция В": 2, "Станция Ж": 3, "Станция Т": 8},
        "Станция Ж": {"Станция Е": 4, "Станция Д": 3, "Станция Н": 7},
        "Станция Е": {"Станция Ж": 4, "Станция И": 6},
        "Станция И": {"Станция Е": 6}
    },
    "Линия 3": {
        "Станция К": {"Станция Л": 3, "Станция М": 4},
        "Станция Л": {"Станция К": 3, "Станция Н": 5},
        "Станция М": {"Станция К": 4, "Станция О": 6},
        "Станция Н": {"Станция Л": 5, "Станция Ж": 7}
    },
    "Линия 4": {
        "Станция П": {"Станция Р": 3, "Станция С": 5},
        "Станция Р": {"Станция П": 3, "Станция Т": 4},
        "Станция С": {"Станция П": 5, "Станция У": 7},
        "Станция Т": {"Станция Р": 4, "Станция Д": 8}
    },
    "Линия 5": {
        "Станция Ф": {"Станция Х": 4, "Станция Ц": 6},
        "Станция Х": {"Станция Ф": 4, "Станция Ч": 3},
        "Станция Ц": {"Станция Ф": 6, "Станция Ш": 7},
        "Станция Ш": {"Станция Ц": 7, "Станция Б": 9},
        "Станция Ч": {"Станция Х": 3}
    },
    "Линия 6": {
        "Станция Ы": {"Станция Ь": 5, "Станция Ю": 3},
        "Станция Ь": {"Станция Ы": 5, "Станция Я": 4},
        "Станция Ю": {"Станция Ы": 3, "Станция В": 10},
        "Станция Я": {"Станция Ь": 4}
    }
}


# Функция для поиска минимального времени между станциями
def find_travel_time(metro_map, start_station, end_station):
    queue = [(0, start_station)]
    shortest_paths = {start_station: 0}

    while queue:
        current_time, current_station = heapq.heappop(queue)

        if current_station == end_station:
            return current_time

        for line in metro_map:
            if current_station in metro_map[line]:
                for neighbor, travel_time in metro_map[line][current_station].items():
                    new_time = current_time + travel_time
                    if neighbor not in shortest_paths or new_time < shortest_paths[neighbor]:
                        shortest_paths[neighbor] = new_time
                        heapq.heappush(queue, (new_time, neighbor))

    return None


def draw_metro_map(metro_map):
    G = nx.Graph()

    line_colors = {
        "Линия 1": "blue",
        "Линия 2": "red",
        "Линия 3": "green",
        "Линия 4": "purple",
        "Линия 5": "orange",
        "Линия 6": "black"
    }

    # Добавляем станции и ребра графа
    for line, stations in metro_map.items():
        for station, connections in stations.items():
            for neighbor, time in connections.items():
                color = line_colors.get(line, "gray")
                G.add_edge(station, neighbor, weight=time, color=color)

    # Позиции для визуализации
    pos = nx.spring_layout(G, seed=42)  # Используем фиксированное расположение для красоты

    label_mapping = {station: station[-1] for station in G.nodes()}

    edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Увеличиваем размер графика
    plt.figure(figsize=(20, 26))

    # Рисуем граф
    nx.draw(G, pos, labels=label_mapping, with_labels=True, node_size=700, node_color="lightblue", font_size=12,
            edge_color=edge_colors, width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3)

    plt.title("Карта метро с пересадками")
    plt.show()


# Пример использования
start = "Станция Ч"
end = "Станция О"
travel_time = find_travel_time(metro_map, start, end)

if travel_time is not None:
    print(f"Минимальное время в пути от {start} до {end}: {travel_time} минут")
else:
    print(f"Нет пути от {start} до {end}")

# Отображаем карту метро
draw_metro_map(metro_map)
