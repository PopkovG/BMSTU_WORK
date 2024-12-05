import requests
import matplotlib.pyplot as plt
import networkx as nx

# Fetch metro data
url = "https://api.hh.ru/metro"
response = requests.get(url)
data = response.json()

# Prepare the map using NetworkX
G = nx.Graph()

# Add stations and lines
for line in data['lines']:
    for station in line['stations']:
        G.add_node(station['name'], line=line['name'])
        for connection in station.get('connections', []):
            G.add_edge(station['name'], connection['station_name'])

# Plot the map
pos = nx.spring_layout(G)  # Optional: Adjust layout for better visualization
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
plt.title('Moscow Metro Map')
plt.show()
