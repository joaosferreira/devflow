from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini

from .config import retry_config, DEFAULT_MODEL
from .tools import github_tools

AGENT_MODEL = DEFAULT_MODEL

github_agent = Agent(
    name="github_agent",
    model=Gemini(model=AGENT_MODEL, retry_options=retry_config),
    instruction="Help users get information from GitHub.",
    tools=[github_tools],
)

root_agent = github_agent
