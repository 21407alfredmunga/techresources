import numpy as np
from typing import List, Dict

class SimpleRAG:
    def __init__(self):
        """
        A simple, from-scratch implementation of a Retrieval-Augmented Generation pipeline.
        """
        self.vector_store: Dict[str, np.ndarray] = {}

    def _get_embedding(self, text: str) -> np.ndarray:
        """
        Simulates generating a text embedding. In a real system, this would
        use a pre-trained model like BERT or a service like OpenAI's embedding API.
        """
        # Simple character-based vectorization for simulation
        vector = np.zeros(128)
        for char in text.lower():
            if 'a' <= char <= 'z':
                vector[ord(char) - ord('a')] += 1
        norm = np.linalg.norm(vector)
        return vector / norm if norm > 0 else vector

    def add_document(self, text: str):
        """
        Adds a document and its embedding to the in-memory vector store.
        """
        if text in self.vector_store:
            return  # Avoid duplicates
        self.vector_store[text] = self._get_embedding(text)
        print(f"Added document: '{text}'")

    def retrieve(self, query: str, top_k: int) -> List[str]:
        """
        Retrieves the top_k most relevant documents from the vector store
        based on cosine similarity.
        """
        query_vector = self._get_embedding(query)
        
        # Calculate cosine similarities
        similarities = {
            text: np.dot(query_vector, stored_vector)
            for text, stored_vector in self.vector_store.items()
        }
        
        # Sort by similarity and return the top_k results
        sorted_docs = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
        
        return [text for text, score in sorted_docs[:top_k]]

    def generate_augmented_prompt(self, query: str) -> str:
        """
        Retrieves the most relevant document and augments the user's query
        to provide context to the LLM.
        """
        retrieved_docs = self.retrieve(query, top_k=1)
        if not retrieved_docs:
            return query # Return original query if no relevant docs are found

        context = retrieved_docs[0]
        
        augmented_prompt = f"""
        Context: {context}

        Based on the context above, please answer the following question:
        Question: {query}
        """
        return augmented_prompt.strip()

# Example Usage:
rag = SimpleRAG()
rag.add_document("The first AI agent, developed in the late 1960s, was named Shakey the Robot.")
rag.add_document("The Turing test, proposed by Alan Turing in 1950, is a test of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.")
rag.add_document("A Large Language Model (LLM) is a type of AI model trained on vast amounts of text data.")

query = "What was the name of the very first AI agent?"
augmented_prompt = rag.generate_augmented_prompt(query)

print("\n--- Augmented Prompt ---")
print(augmented_prompt)
print("------------------------")

assert "Shakey" in augmented_prompt
assert "Context:" in augmented_prompt
print("\nSolution for Module 2 is correct.")
