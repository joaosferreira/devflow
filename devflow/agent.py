from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini

from .config import AGENT_MODEL, retry_config
from .tools import github_tools

github_agent = Agent(
    name="github_agent",
    model=Gemini(model=AGENT_MODEL, retry_options=retry_config),
    instruction="""You are a GitHub assistant that helps users interact with their GitHub account.
    
    You have access to GitHub tools that allow you to search for repositories, issues, pull requests, retrieve user information, etc.
    When the user asks about their own resources, first use the get_me tool to retrieve the user's GitHub information.
    Chain as many tools as necessary to retrieve the information needed to answer the user's query.""",
    tools=[github_tools],
)

root_agent = github_agent
