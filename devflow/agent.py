from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini
from google.adk.models.lite_llm import LiteLlm

from .config import agent_config, retry_config
from .tools import github_tools, store_github_username

# Check for OpenAI models
if agent_config.agent_model.startswith("openai/"):
    model = LiteLlm(model=agent_config.agent_model)
else:
    model = Gemini(model=agent_config.agent_model, retry_config=retry_config)


github_agent = Agent(
    name="github_agent",
    model=model,
    instruction="""You are a GitHub assistant that helps users interact with their GitHub account.
    
    You have access to GitHub tools that allow you to search for repositories, issues, pull requests, retrieve user information, etc.
    When the user asks about their own resources, first check if the login username is stored in the session state.
    If the login username is not in the sessiom state, use the get_me tool to retrieve the user's GitHub information and store it using the store_github_username tool.
    Use the stored GitHub username to search for the user's resources using the appropriate tools.
    Chain as many tools as necessary to retrieve the information needed to answer the user's query.""",
    tools=[github_tools, store_github_username],
)

root_agent = github_agent
