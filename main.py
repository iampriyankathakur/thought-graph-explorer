from src.text_processor import extract_concepts
from src.embedding_engine import Embedder
from src.graph_builder import build_graph
from src.graph_reasoner import find_relevant_nodes, find_paths
from src.answer_generator import generate_answer
from src.visualizer import visualize_graph

# Load text
with open("data/sample.txt", "r") as f:
    text = f.read()

# Step 1: Extract concepts
concepts = extract_concepts(text)

# Step 2: Embed concepts
embedder = Embedder()
embeddings = embedder.encode(concepts)

# Step 3: Build graph
G = build_graph(concepts, embeddings)

# Step 4: Query
query = input("Enter your query: ")

query_embedding = embedder.encode([query])[0]

# Step 5: Find relevant nodes
start_nodes = find_relevant_nodes(query_embedding, embeddings, concepts)

# Step 6: Find reasoning paths
paths = find_paths(G, start_nodes)

# Step 7: Generate answer
answer, path = generate_answer(paths)

print("\nAnswer:")
print(answer)

print("\nReasoning Path:")
print(" → ".join(path))

# Step 8: Visualize graph
visualize_graph(G)
