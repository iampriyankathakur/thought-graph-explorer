# 🧠 Thought Graph Explorer

## Overview

Thought Graph Explorer is a semantic reasoning system that transforms unstructured text into a graph of interconnected concepts and performs multi-hop reasoning to answer complex queries.

Instead of traditional keyword search, this system explores relationships between ideas and generates reasoning paths.

---

## Features

- Concept extraction from raw text
- Semantic embedding using Sentence Transformers
- Graph construction using similarity + co-occurrence
- Multi-hop reasoning engine
- Explainable reasoning paths
- Graph visualization

---

## Architecture

Text → Concepts → Embeddings → Graph → Reasoning → Answer

---

## Installation

```bash
git clone https://github.com/yourusername/thought-graph-explorer.git
cd thought-graph-explorer
pip install -r requirements.txt
```

## Run

python main.py

## Example Query

How does climate change affect the economy?

## Output
Answer
Reasoning path
Graph visualization

## Future Work
Graph Neural Networks
Persistent memory graph
LLM-based reasoning synthesis
Web interface

# 📦 requirements.txt
spacy
networkx
matplotlib
scikit-learn
sentence-transformers
keybert


---

# 🚫 .gitignore

pycache/
*.pyc


---

# 📄 data/sample.txt

```text
Climate change affects agriculture and food production. 
Reduced crop yields lead to supply shortages. 
Supply shortages increase prices and cause inflation. 
Inflation impacts economic stability and growth. 
Economic instability affects employment and global markets.
```

