from app.agent import process_prompt
from app.models import AgentResponse
import asyncio
import json

TEST_CASES = [
    {"prompt": "Calculate 2 + 3 * 4", "expected_tool": "math_tool", "expected_contains": "14"},
    {"prompt": "Search for latest AI news", "expected_tool": "search_tool", "expected_contains": "AI"},
    {"prompt": "Calculate sqrt(16)", "expected_tool": "math_tool", "expected_contains": "4"},
    {"prompt": "Who is the president of the US in 2025?", "expected_tool": "search_tool", "expected_contains": "president"},
    {"prompt": "Hello world", "expected_tool": None, "expected_contains": "clarification_needed"},
    {"prompt": "Calculate 1/0", "expected_tool": "math_tool", "expected_contains": "error"},
    {"prompt": "Search for !@#$%", "expected_tool": "search_tool", "expected_contains": "error"},
    {"prompt": "What is the weather like?", "expected_tool": "search_tool", "expected_contains": "weather"},
]

async def evaluate_test_case(test_case: dict) -> dict:
    result = await process_prompt(test_case["prompt"])
    passed = True
    errors = []
    
    # Check tool usage
    if test_case["expected_tool"] and test_case["expected_tool"] not in result.tools_used:
        passed = False
        errors.append(f"Expected tool {test_case['expected_tool']} but got {result.tools_used}")
    
    # Check response content
    if test_case["expected_contains"].lower() not in result.response.lower() and test_case["expected_contains"] not in result.metadata.get("status", ""):
        passed = False
        errors.append(f"Response did not contain expected content: {test_case['expected_contains']}")
    
    return {"prompt": test_case["prompt"], "passed": passed, "errors": errors, "response": result.dict()}

async def run_evaluation():
    results = []
    for test_case in TEST_CASES:
        result = await evaluate_test_case(test_case)
        results.append(result)
    
    with open("evaluation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    pass_count = sum(1 for r in results if r["passed"])
    print(f"Evaluation completed: {pass_count}/{len(TEST_CASES)} test cases passed")

if __name__ == "__main__":
    asyncio.run(run_evaluation())