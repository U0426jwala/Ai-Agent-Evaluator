from pydantic import BaseModel, Field
from typing import List, Dict, Any

class AgentRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=1000)

class AgentResponse(BaseModel):
    response: str
    tools_used: List[str]
    metadata: Dict[str, Any]