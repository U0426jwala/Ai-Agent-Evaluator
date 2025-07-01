from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models import AgentRequest, AgentResponse
from app.agent import process_prompt
import uvicorn

app = FastAPI(title="AI Agent Service")

@app.post("/agent", response_model=AgentResponse)
async def agent_endpoint(request: AgentRequest):
    try:
        result = await process_prompt(request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)