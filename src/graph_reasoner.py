import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

def find_relevant_nodes(query_embedding, concept_embeddings, concepts):
    sims = cosine_similarity([query_embedding], concept_embeddings)[0]
    ranked = sorted(zip(concepts, sims), key=lambda x: x[1], reverse=True)
    return [r[0] for r in ranked[:3]]

def find_paths(graph, start_nodes, max_depth=3):
    paths = []
    for node in start_nodes:
        for target in graph.nodes:
            try:
                path = nx.shortest_path(graph, source=node, target=target)
                if len(path) <= max_depth:
                    paths.append(path)
            except:
                continue
    return paths
