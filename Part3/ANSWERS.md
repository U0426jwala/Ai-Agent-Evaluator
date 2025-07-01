Part 3: Conceptual Understanding

1. Agent Evaluation & Correctness

Measuring Correct Action:





Tool Selection: Verify the agent selects the appropriate tool (e.g., math_tool for calculations, search_tool for queries) by logging tools_used in the response.



Response Accuracy: Use rule-based checks (e.g., expected keywords in response) and LLM-as-judge for semantic correctness.



Consistency: Compare responses across similar prompts to ensure consistent behavior.

Detecting Conflicting or Stale Results:





Conflict Detection: Implement a cache of recent responses and compare new results against cached ones for similar prompts. Flag discrepancies if the same prompt yields different tools or contradictory outputs.



Staleness Check: For search results, include a timestamp in metadata and reject results older than a threshold (e.g., 24 hours) for time-sensitive queries.



Validation Layer: Use a secondary API call or cross-reference with a trusted source to validate critical responses.

2. Prompt Engineering Proficiency

Designing System Prompts:





Clarity: Use precise language to define the agent's role, tone (professional, friendly), and constraints (e.g., no speculation).



Structure: Include numbered guidelines for prioritization (e.g., tool selection, fallback behavior).



Constraints: Enforce safety (avoid harmful content), conciseness, and tool-specific routing logic.



Tone: Specify a consistent tone (e.g., formal for calculations, conversational for clarifications).

Testing Prompts:





Unit Tests: Test prompt effects using pytest to verify tone (e.g., keyword analysis for professionalism) and tool usage.



Edge Cases: Evaluate prompts with ambiguous, off-topic, or malicious inputs to ensure fallback logic works.



A/B Testing: Compare responses with different prompt variations to optimize clarity and effectiveness.