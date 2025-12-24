import sys
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from game.router import router
from fastmcp import FastMCP



app = FastAPI(
    title="Game Sales API",
    description="Standard HTTP API + MCP Server",
    version="1.0.0",
)

app.include_router(router)

@app.get("/")
def main():
    return {"message": "Hello World"}


mcp = FastMCP.from_fastapi(app=app)

if __name__ == "__main__":
    mcp.run()

