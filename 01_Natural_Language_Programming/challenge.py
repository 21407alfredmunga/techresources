# Core Challenge for Module 01

class PromptManager:
    def __init__(self, system_prompt: str, context_prompt: str, role_prompt: str):
        self.system_prompt = system_prompt
        self.context_prompt = context_prompt
        self.role_prompt = role_prompt

    def generate_react_prompt(self, thought: str, action: str) -> str:
        # Implement the ReAct prompt generation
        pass

    def call_llm(self, prompt: str, temperature: float, top_p: float) -> str:
        # Simulate the LLM call
        pass

# Example Usage:
# manager = PromptManager("You are a helpful assistant.", "The user is asking about weather.", "Act as a meteorologist.")
# react_prompt = manager.generate_react_prompt("I need to find the weather in a city.", "search_weather(city='London')")
# response = manager.call_llm(react_prompt, temperature=0.7, top_p=0.9)
# assert "Simulating LLM call" in response
