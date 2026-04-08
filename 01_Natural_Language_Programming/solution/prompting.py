class PromptManager:
    def __init__(self, system_prompt: str, context_prompt: str, role_prompt: str):
        self.system_prompt = system_prompt
        self.context_prompt = context_prompt
        self.role_prompt = role_prompt

    def _assemble_full_prompt(self, user_query: str) -> str:
        """Helper to assemble the full prompt from components."""
        return f"""
        System: {self.system_prompt}
        Context: {self.context_prompt}
        Role: {self.role_prompt}
        User Query: {user_query}
        """

    def generate_react_prompt(self, thought: str, action: str) -> str:
        """
        Formats a prompt according to the ReAct framework.
        Thought: The reasoning step of the agent.
        Action: The action the agent will take.
        """
        react_block = f"Thought: {thought}\nAction: {action}"
        # In a real scenario, this would be part of a larger prompt
        # that includes the full conversation history.
        return self._assemble_full_prompt(react_block)

    def call_llm(self, prompt: str, temperature: float, top_p: float) -> str:
        """
        Simulates a call to a language model, printing the sampling parameters.
        """
        print(f"--- Simulating LLM Call ---")
        print(f"Prompt sent to LLM:\n{prompt}")
        print(f"Sampling Parameters: Temperature={temperature}, Top-P={top_p}")
        print(f"--------------------------")
        
        # In a real call, you would use an API (e.g., OpenAI's) here.
        # For the simulation, we return a deterministic response.
        return "Simulating LLM call with specified parameters. In a real scenario, this would be the model's response."

# Example Usage:
manager = PromptManager(
    system_prompt="You are a helpful assistant designed to answer questions.",
    context_prompt="The user is asking about the weather in a specific city.",
    role_prompt="You are a friendly and knowledgeable meteorologist."
)

react_prompt = manager.generate_react_prompt(
    thought="The user wants to know the weather. I should use the weather tool.",
    action="get_weather(city='London')"
)

response = manager.call_llm(react_prompt, temperature=0.7, top_p=0.9)

assert "Simulating LLM call" in response
print("Solution for Module 1 is correct.")
