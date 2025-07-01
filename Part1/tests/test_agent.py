from app.agent import process_prompt
from app.models import AgentRequest, AgentResponse
import pytest
from pydantic import ValidationError

@pytest.mark.asyncio
async def test_math_tool():
    request = AgentRequest(prompt="Calculate 2 + 2")
    response = await process_prompt(request.prompt)
    assert response.tools_used == ["math_tool"]
    assert "4" in response.response

@pytest.mark.asyncio
async def test_search_tool():
    request = AgentRequest(prompt="Search for AI trends")
    response = await process_prompt(request.prompt)
    assert response.tools_used == ["search_tool"]
    assert "AI" in response.response

@pytest.mark.asyncio
async def test_invalid_input():
    with pytest.raises(ValidationError):
        AgentRequest(prompt="")  # Raises error at model creation

@pytest.mark.asyncio
async def test_off_topic():
    request = AgentRequest(prompt="Hello world")
    response = await process_prompt(request.prompt)
    assert response.metadata["status"] == "clarification_needed"
