# Module 02: Embeddings & Retrieval-Augmented Generation (RAG)

This module focuses on grounding the model in factual, up-to-date data. We will build a simple RAG pipeline from scratch to understand the core mechanics of document retrieval and context expansion.

## Core Concepts
*   **Embedding Fundamentals:** Creating numerical representations of data.
*   **The RAG Architecture:** Combining document retrieval with prompt expansion.
*   **Approximate Nearest Neighbor (ANN):** The idea behind efficient large-scale retrieval.

## Core Challenge
Your task is to implement a `SimpleRAG` class that can ingest documents, create embeddings, and retrieve relevant documents to augment a prompt.

1.  Create a `SimpleRAG` class that maintains an in-memory "vector store" (a dictionary will suffice).
2.  Implement an `add_document(text: str)` method. This method should simulate generating an embedding (you can use a simple character-based vectorization function) and store the text and its vector.
3.  Implement a `retrieve(query: str, top_k: int) -> list[str]` method that finds the `top_k` most relevant documents using cosine similarity.
4.  Implement a `generate_augmented_prompt(query: str) -> str` method that retrieves the most relevant document and combines it with the original query into a new prompt.

## Beyond the Code: Supplemental Learning

| Resource Type | Topic | Link/Description |
| :--- | :--- | :--- |
| Concept | Retrieval Augmented Generation (RAG) | [Video Title Placeholder](https://www.youtube.com/watch?v=dV7vbBjPcno) <br> *Why this matters: This video explains the core concepts of RAG, providing the foundational knowledge needed to implement your own retrieval systems in plain Python.* |
| Deep Dive | Vector Math | [Video Title Placeholder](https://www.youtube.com/watch?v=g-Fa1GQeCRc) <br> *Why this matters: Understanding the vector mathematics behind embeddings is crucial for first-principles engineering of search and retrieval systems.* |
| Concept | HNSW/ScaNN | [Video Title Placeholder](https://www.youtube.com/watch?v=wZn9XvXBnU4) <br> *Why this matters: This video introduces advanced indexing strategies, which are key to scaling retrieval systems beyond simple cosine similarity searches.* |
