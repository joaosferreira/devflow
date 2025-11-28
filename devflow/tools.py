import os

from google.adk.tools import AgentTool, google_search, McpToolset
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams
from google.adk.tools.tool_context import ToolContext

github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
if not github_token:
    raise ValueError(
        "GITHUB_PERSONAL_ACCESS_TOKEN environment variable is not set. "
        "Please set it in your .env file or environment."
    )

try:
    github_tools = McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://api.githubcopilot.com/mcp/",
            headers={
                "Authorization": f"Bearer {github_token}",
                "X-MCP-Toolsets": "default",
                "X-MCP-Readonly": "true",
            },
        ),
    )
except Exception as e:
    raise e


def store_github_username(username: str, tool_context: ToolContext):
    """
    Store the GitHub username in the session state.

    Args:
        username: The GitHub username to store
    """
    tool_context.state["user:github_username"] = username

    return {"status": "success"}
