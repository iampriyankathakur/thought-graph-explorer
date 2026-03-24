import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

def build_graph(concepts, embeddings, threshold=0.5):
    G = nx.Graph()

    for i, concept in enumerate(concepts):
        G.add_node(concept)

    sim_matrix = cosine_similarity(embeddings)

    for i in range(len(concepts)):
        for j in range(i+1, len(concepts)):
            if sim_matrix[i][j] > threshold:
                G.add_edge(concepts[i], concepts[j], weight=sim_matrix[i][j])

    return G
