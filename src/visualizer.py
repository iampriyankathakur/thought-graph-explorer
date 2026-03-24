import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G):
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title("Thought Graph")
    plt.show()
