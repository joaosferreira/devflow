from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import AgentTool

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
    instruction=f"""You are a GitHub assistant that helps users interact with GitHub.
    
    You have access to GitHub tools that allow you to search for GitHub resources (e.g., repositories, issues, pull requests).
    
    Task:
    Help the user by answering questions about GitHub resources.
    Use GitHub tools to retrieve information relevant to the user's query.
    
    Infer from the conversation history if the user's query is about their own GitHub resources, and if so, use the GitHub username stored in context when calling other tools.
    If the username is not in context, use the get_me tool to retrieve the user's GitHub login information, and store the GitHub username using the store_github_username tool.""",
    tools=[github_tools, store_github_username],
)


coordinator_agent = Agent(
    name="coordinator_agent",
    model=model,
    instruction="""You are a coordinator agent that routes requests to specialized agent tools.
    
    You have access to other agent tools that allow you to get answers from specialized agents.
    
    Task:
    Route user requests to the appropriate specialized agent tool.
    
    For GitHub-related queries, call the github_agent tool.""",
    tools=[AgentTool(agent=github_agent)],
)


root_agent = coordinator_agent
