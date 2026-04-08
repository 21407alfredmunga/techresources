# Core Challenge for Module 02
import numpy as np

class SimpleRAG:
    def __init__(self):
        self.vector_store = {}

    def _get_embedding(self, text: str) -> np.ndarray:
        # Simple character-based vectorization for simulation
        vector = np.zeros(128)
        for char in text.lower():
            if 'a' <= char <= 'z':
                vector[ord(char) - ord('a')] += 1
        norm = np.linalg.norm(vector)
        return vector / norm if norm > 0 else vector

    def add_document(self, text: str):
        # Implement document addition
        pass

    def retrieve(self, query: str, top_k: int) -> list[str]:
        # Implement document retrieval
        pass

    def generate_augmented_prompt(self, query: str) -> str:
        # Implement prompt augmentation
        pass

# Example Usage:
# rag = SimpleRAG()
# rag.add_document("The first AI agent was named Shakey.")
# rag.add_document("The Turing test evaluates a machine's ability to exhibit intelligent behavior.")
# augmented_prompt = rag.generate_augmented_prompt("What was the name of the first AI agent?")
# assert "Shakey" in augmented_prompt
