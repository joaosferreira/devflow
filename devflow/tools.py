from google.adk.tools import ToolContext
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams

from .config import agent_config

try:
    github_tools = McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://api.githubcopilot.com/mcp/",
            headers={
                "Authorization": f"Bearer {agent_config.github_personal_access_token}",
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
