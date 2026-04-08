import json
import time
from typing import Callable, Dict, List, Any

# Simplified AgentState from previous modules
class AgentState:
    def __init__(self): self.history: List[str] = []
    def add_to_history(self, msg: str): self.history.append(msg)
    def get_full_history(self) -> str: return "\n".join(self.history)

class SimpleTracer:
    """
    A simple tracer to capture spans of operations for observability.
    This is a manual implementation of concepts found in OpenTelemetry.
    """
    def __init__(self):
        self.spans: List[Dict[str, Any]] = []

    def add_span(self, span_name: str, metadata: dict):
        """Records a single operation (span) with associated metadata."""
        span = {
            "name": span_name,
            "timestamp": time.time(),
            "metadata": metadata,
        }
        self.spans.append(span)
        print(f"Tracer: Recorded span '{span_name}'")

class LLMAsJudge:
    """
    Simulates using an LLM to evaluate the quality of an agent's output.
    """
    def evaluate(self, prompt: str, agent_output: str) -> Dict[str, Any]:
        """
        Simulates a call to an LLM to score the agent's output based on a rubric.
        """
        print("\n--- LLM as Judge Evaluating ---")
        print(f"Prompt: {prompt}")
        print(f"Agent Output: {agent_output}")
        
        # Simulated evaluation logic
        score = 10 if "12:00 PM" in agent_output else 2
        reasoning = "The agent correctly identified the time." if score == 10 else "The agent failed to provide the correct time."
        
        evaluation = {"score": score, "reasoning": reasoning}
        print(f"Evaluation: {evaluation}")
        print("-----------------------------")
        return evaluation

class ObservableOrchestrator:
    def __init__(self, model: Callable, tool_registry: Dict, tracer: SimpleTracer, judge: LLMAsJudge):
        self.model = model
        self.tool_registry = tool_registry
        self.tracer = tracer
        self.judge = judge

    def run(self, initial_prompt: str, max_loops: int = 5) -> Dict[str, Any]:
        """
        A modified run loop that includes tracing and final evaluation.
        """
        state = AgentState()
        state.add_to_history(f"User: {initial_prompt}")

        for i in range(max_loops):
            prompt = state.get_full_history()
            
            # Trace the LLM call
            self.tracer.add_span("llm_call", {"prompt": prompt, "loop": i})
            model_output = self.model(prompt)

            try:
                tool_call = json.loads(model_output)
                tool_name = tool_call.get("tool_name")
                if tool_name in self.tool_registry:
                    # Trace the tool execution
                    self.tracer.add_span("tool_execution", {"tool_name": tool_name})
                    result = self.tool_registry[tool_name]()
                    state.add_to_history(f"Tool Result: {result}")
                    continue
            except json.JSONDecodeError:
                # It's a final answer
                final_answer = model_output
                # Evaluate the final answer
                evaluation = self.judge.evaluate(initial_prompt, final_answer)
                return {"answer": final_answer, "evaluation": evaluation}
        
        return {"answer": "Agent failed to complete.", "evaluation": self.judge.evaluate(initial_prompt, "No output.")}

# --- Simulation Components ---
def simulated_llm(prompt: str) -> str:
    if "time" in prompt.lower() and "Tool Result" not in prompt:
        return json.dumps({"tool_name": "get_time"})
    return "The time is 12:00 PM."
def get_time() -> str: return "12:00 PM"

# --- Main Execution ---
tracer = SimpleTracer()
judge = LLMAsJudge()
orchestrator = ObservableOrchestrator(simulated_llm, {"get_time": get_time}, tracer, judge)

result = orchestrator.run("What time is it?")

print(f"\nFinal Result: {result}")
print(f"\nTrace Spans Captured: {json.dumps(tracer.spans, indent=2)}")

assert result["evaluation"]["score"] == 10
assert len(tracer.spans) == 3 # llm_call -> tool_execution -> llm_call
print("\nSolution for Module 4 is correct.")
