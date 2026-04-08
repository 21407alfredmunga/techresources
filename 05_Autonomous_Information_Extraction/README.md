# Module 05: Agentic Data Engineering & Knowledge Construction

Welcome to the Agentic Data Engineering module. This focus area transitions past simple Retrieval-Augmented Generation (RAG) and into building agents that can autonomously manage data quality and structure.

## Topic Explanation

Rather than relying purely on vector embeddings over unstructured text chunks, Agentic Data Engineering relies on constructing deterministic structures—principally Knowledge Graphs. By incorporating Entity Resolution, agents systematically extract discrete entities (e.g., people, organizations) and relationships (edges) to form a "Data Fabric". This approach grounds the agent's logical reasoning in a highly structured, queryable knowledge lake, bridging the gap between raw enterprise data and cognitive AI operations.

## Core Challenge

For this module, your practical exploration lies primarily within the Jupyter notebook provided. 

*   **Interactive Notebook**: `agentic_data_engineering.ipynb` 
*   **Mission**: You will implement a `KnowledgeGraphBuilder` that structurally categorizes mock extracted data into deterministic Pydantic Node and Edge models. 

## Recommended Reading

To master the concepts forming the backbone of this module, the following foundational literature is heavily referenced:

*   **Essential GraphRAG** by Tomaž Bratanič & Oskar Hane 
    *   *Focus:* Chapter 6 ("Constructing Knowledge Graphs with LLMs") and Chapter 7 ("Microsoft’s GraphRAG implementation").
    *   *Why this matters:* Essential for understanding the automated extraction of entities and relationships required to build "smarter" and more rigorous retrieval systems.
*   **AI Engineering** by Chip Huyen 
    *   *Focus:* Chapter 8 ("Data Strategies").
    *   *Why this matters:* Provides deep insights into data curation, synthetic data generation using LLMs, and setting up the feedback loops inherently required to build high-quality instruction datasets.
*   **Knowledge Graphs: A Practitioner’s Guide** by Jesús Barrasa & Jim Webber
    *   *Focus:* "Data Fabric" theory and integration patterns.
    *   *Why this matters:* Delivers the necessary theory to understand exactly how autonomous agents can integrate highly diverse enterprise data sources into a unified knowledge lake.
