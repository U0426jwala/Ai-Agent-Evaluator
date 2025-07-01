# AI Agent Evaluator - Technical Implementation Answers

## Part 3: Conceptual Understanding

### 1. Agent Evaluation & Correctness

#### A. Measuring Correct Action

**Tool Selection Verification:**
- **Implementation**: Log `tools_used` field in every `AgentResponse` and compare against expected tools based on prompt analysis
- **Validation Logic**: 
  ```python
  def validate_tool_selection(prompt, response):
      math_keywords = ["calculate", "+", "-", "*", "/", "^", "sqrt"]
      search_keywords = ["search", "find", "what is", "who is", "latest"]
      
      if any(keyword in prompt.lower() for keyword in math_keywords):
          return "math_tool" in response.tools_used
      elif any(keyword in prompt.lower() for keyword in search_keywords):
          return "search_tool" in response.tools_used
      return True  # For clarification requests
  ```
- **Metrics**: Track accuracy as `correct_tool_selections / total_requests`

**Response Accuracy Assessment:**
- **Rule-based Checks**: 
  - Math responses: Validate numerical results against expected calculations
  - Search responses: Check for presence of search indicators ("found", "according to", "based on")
  - Format validation: Ensure structured response format
- **LLM-as-Judge**: Use GPT-4/Claude to evaluate semantic correctness on 1-5 scale for accuracy, relevance, and completeness
- **Implementation**:
  ```python
  async def evaluate_response_accuracy(prompt, response):
      # Rule-based validation
      if "math_tool" in response.tools_used:
          return validate_math_result(prompt, response)
      elif "search_tool" in response.tools_used:
          return validate_search_content(response)
      
      # LLM judge for complex cases
      return await llm_judge_evaluate(prompt, response)
  ```

**Consistency Monitoring:**
- **Implementation**: Maintain cache of recent responses and compare similar prompts
- **Similarity Detection**: Use embedding similarity (cosine similarity > 0.8) to identify related prompts
- **Inconsistency Detection**: Flag when similar prompts yield different tools or contradictory responses
- **Tracking**: Log inconsistencies with confidence scores and response variations

#### B. Detecting Conflicting or Stale Results

**Conflict Detection:**
- **Cache Implementation**: Store responses with timestamps and prompt hashes
- **Comparison Logic**: 
  ```python
  def detect_conflicts(prompt, new_response):
      cached_response = get_cached_response(prompt)
      if cached_response:
          conflicts = []
          
          # Tool usage conflicts
          if cached_response.tools_used != new_response.tools_used:
              conflicts.append("tool_usage_conflict")
          
          # Content conflicts (semantic difference > 0.7)
          if semantic_difference(cached_response.response, new_response.response) > 0.7:
              conflicts.append("content_conflict")
          
          return conflicts
      return []
  ```
- **Flagging System**: Alert when same prompt yields different tools or contradictory information

**Staleness Management:**
- **Time-sensitive Keywords**: ["latest", "current", "today", "news", "weather", "stock price"]
- **Threshold Configuration**:
  - News queries: 1 hour
  - Weather: 3 hours
  - Stock prices: 15 minutes
  - General search: 24 hours
- **Implementation**:
  ```python
  def check_staleness(prompt, response_metadata):
      if is_time_sensitive(prompt):
          age = current_time - response_metadata["timestamp"]
          threshold = get_staleness_threshold(categorize_query(prompt))
          return age > threshold
      return False
  ```

**Validation Layer:**
- **Cross-reference Sources**: For critical information, validate against multiple trusted APIs
- **Math Validation**: Use Wolfram Alpha API to verify complex calculations
- **Fact Checking**: Cross-check factual claims with Wikipedia/Wikidata APIs
- **Implementation**: Secondary API calls for high-stakes responses with confidence scoring

### 2. Prompt Engineering Proficiency

#### A. Designing System Prompts

**Clarity Guidelines:**
- **Precise Language**: Use specific, actionable instructions instead of vague descriptions
  - Good: "If prompt contains mathematical operators (+, -, *, /, ^), use math_tool"
  - Bad: "Handle math stuff with the math tool"
- **Role Definition**: Clearly define agent capabilities and limitations
- **Scope Boundaries**: Explicitly state what the agent can and cannot do

**Structured Guidelines:**
```
You are an AI agent designed to provide accurate responses. Follow these prioritized guidelines:

1. TOOL SELECTION (Critical Priority):
   - Mathematical expressions/calculations → math_tool
   - Search queries/factual questions → search_tool
   - Unclear/off-topic requests → request clarification

2. RESPONSE FORMATTING (High Priority):
   - Provide direct answer first
   - Include supporting details from tool outputs
   - Offer additional assistance if appropriate

3. ERROR HANDLING (High Priority):
   - Acknowledge tool failures clearly
   - Suggest alternative approaches
   - Never fabricate information when tools fail

4. FALLBACK BEHAVIOR (Standard Priority):
   - Request clarification with specific examples
   - Redirect politely for out-of-scope requests
   - Maintain helpful, professional tone
```

**Constraint Implementation:**
- **Safety Constraints**: Refuse harmful, illegal, or unethical requests
- **Response Limits**: Maximum 500 words unless specifically requested
- **Source Attribution**: Always cite sources for factual claims
- **Tone Requirements**: Professional but friendly across all interactions

**Tone Specification:**
- **Mathematical Responses**: Precise, methodical, step-by-step explanations
- **Search Responses**: Informative, conversational, well-sourced
- **Clarifications**: Helpful, patient, with specific examples
- **Error Cases**: Apologetic but solution-focused

#### B. Testing Prompts

**Unit Testing Framework:**
```python
@pytest.mark.asyncio
async def test_tone_consistency():
    """Verify professional tone across response types"""
    test_cases = [
        ("Calculate 2+2", "mathematical"),
        ("Search for AI news", "informational"),
        ("Help me please", "clarification")
    ]
    
    for prompt, expected_tone in test_cases:
        response = await process_prompt(prompt)
        assert validate_tone(response.response, expected_tone)
        assert not contains_unprofessional_language(response.response)

def validate_tone(text, expected_tone):
    tone_indicators = {
        "mathematical": ["calculate", "result", "equals", "solution"],
        "informational": ["found", "according", "based on", "sources"],
        "clarification": ["clarify", "specific", "help", "provide"]
    }
    return any(indicator in text.lower() for indicator in tone_indicators[expected_tone])
```

**Edge Case Testing:**
- **Ambiguous Prompts**: "Help me", "I need information" → Should request clarification
- **Off-topic Requests**: "Tell me a joke", "What's your favorite color" → Polite redirection
- **Malicious Inputs**: Injection attempts, harmful requests → Safe refusal
- **Tool Failures**: API errors, network issues → Graceful error handling

**A/B Testing Implementation:**
```python
async def run_ab_test(prompt_variations, test_prompts):
    """Compare different prompt variations for effectiveness"""
    results = {}
    
    for variation_name, system_prompt in prompt_variations.items():
        results[variation_name] = await test_variation(system_prompt, test_prompts)
    
    # Analyze metrics: accuracy, response time, user satisfaction
    winner = analyze_results(results)
    return winner

def analyze_results(results):
    # Statistical significance testing
    # Confidence intervals
    # Performance metrics comparison
    return best_performing_variation
```

**Testing Metrics:**
- **Accuracy**: Percentage of correct tool selections and responses
- **Response Time**: Average time to generate responses
- **User Satisfaction**: Simulated user feedback scores
- **Consistency**: Variance in responses to similar prompts
- **Error Rate**: Frequency of tool failures and error handling

**Continuous Improvement:**
- **Performance Monitoring**: Track metrics over time
- **Prompt Iteration**: Regular updates based on test results
- **User Feedback Integration**: Incorporate real user interactions
- **Automated Testing**: CI/CD pipeline with prompt effectiveness tests

## Implementation Best Practices

1. **Comprehensive Logging**: Log all tool selections, response times, and error cases
2. **Monitoring Dashboard**: Real-time visibility into agent performance metrics
3. **Feedback Loops**: Continuous improvement based on evaluation results
4. **Version Control**: Track prompt changes and their impact on performance
5. **Stakeholder Communication**: Regular reports on agent effectiveness and improvements
