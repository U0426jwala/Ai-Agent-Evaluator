from app.tools.search_tool import search_web
from app.tools.math_tool import calculate_expression
from app.models import AgentResponse
from typing import List, Dict, Any

SYSTEM_PROMPT = """
You are an AI agent designed to provide accurate and helpful responses. Follow these guidelines:
1. Maintain a professional and friendly tone.
2. Use the search tool for factual or real-time information queries.
3. Use the math tool for calculations or mathematical questions.
4. If the prompt is off-topic or unclear, respond with a polite clarification request.
5. Avoid speculative or unsafe content.
6. Structure responses clearly with concise explanations.
"""

async def process_prompt(prompt: str) -> AgentResponse:
    tools_used = []
    metadata = {}
    response = ""

    if "calculate" in prompt.lower() or any(op in prompt for op in ["+", "-", "*", "/", "^"]):
        try:
            result = calculate_expression(prompt)
            response = f"Calculation result: {result}"
            tools_used.append("math_tool")
            metadata["calculation"] = result
        except Exception as e:
            response = "Error in calculation. Please provide a valid mathematical expression."
            metadata["error"] = str(e)
    elif any(keyword in prompt.lower() for keyword in ["search", "find", "what is", "who is"]):
        try:
            search_results = await search_web(prompt)
            response = f"Search results: {search_results[:500]}"  # Truncate for brevity
            tools_used.append("search_tool")
            metadata["search_results"] = search_results
        except Exception as e:
            response = "Error performing search. Please try again."
            metadata["error"] = str(e)
    else:
        response = "I'm not sure how to handle this request. Could you clarify or provide a specific question?"
        metadata["status"] = "clarification_needed"

    return AgentResponse(response=response, tools_used=tools_used, metadata=metadata)