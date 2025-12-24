import os
import sys
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from dotenv import load_dotenv
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))

target_script_path = os.path.abspath(os.path.join(current_dir, "..", "backend", "app", "main.py"))


print(f"Connecting to MCP Server at: {target_script_path}")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='GameSalesManager',
    instruction='You are a helpful assistant for managing game sales data.',
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='python',  
                    args=[
                        "-u",
                        target_script_path,
                        "--transport",
                        "stdio"
                    ],
                    env=os.environ.copy() 
                ),
            ),
        )
    ],
)

