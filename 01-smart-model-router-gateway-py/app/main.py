import asyncio
import logging
import sys
from contextlib import asynccontextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from services.config import load_config
from services.openRouterService import OpenRouterService

logger = logging.getLogger(__name__)
service = OpenRouterService(load_config())

class ChatBody(BaseModel):
    question: str = Field(..., min_length=5)

app = FastAPI()


@app.post("/chat")
async def chat(body: ChatBody, request: Request):
    try:
        result = await asyncio.wait_for(
            service.generate(body.question),
            timeout=30,
        )
        return {"response": result}
    except asyncio.TimeoutError:
        logger.warning("Timeout on /chat request")
        raise HTTPException(status_code=504, detail="Gateway Timeout")
    except Exception as exc:
        logger.exception("Error handling /chat request: %s", exc)
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    cfg = load_config()
    print(f"Server is running on port {cfg.port}")
    uvicorn.run(app, host="0.0.0.0", port=cfg.port)
