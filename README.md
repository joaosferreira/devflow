# DevFlow

An AI-powered development assistant agent that streamlines software development workflows by automating routine tasks such as creating Jira tickets, opening GitHub issues, drafting pull requests, and reviewing code. Built as a capstone project for the [5-Day AI Agents Intensive Course with Google](https://www.kaggle.com/learn-guide/5-day-agents).

## Problem

Software development teams face significant challenges in managing repetitive, time-consuming tasks that interrupt their core development work:

1. **Manual Task Management**: Developers spend considerable time creating and managing Jira tickets, GitHub issues, and tracking project tasks manually.

2. **Inconsistent Documentation**: Pull requests and code reviews often lack consistent formatting and comprehensive descriptions, leading to communication gaps and slower review processes.

3. **Context Switching**: Developers frequently switch between their IDE, project management tools (Jira), version control (GitHub), and communication platforms, reducing productivity and focus.

4. **Repetitive Workflows**: Common tasks like drafting PR descriptions, creating tickets from bug reports, and formatting code review comments follow predictable patterns that could be automated.

5. **Knowledge Fragmentation**: Information about issues, tickets, and code changes is scattered across multiple platforms, making it difficult to maintain context and make informed decisions.

These challenges result in:
- Reduced developer productivity
- Increased time-to-market for features
- Higher likelihood of human error in task management
- Inconsistent quality in documentation and communication

## Solution

DevFlow addresses these challenges by providing an intelligent, conversational AI assistant that integrates seamlessly with development tools. The solution leverages Google's Agent Development Kit (ADK) and Gemini language models to:

1. **Automate Task Creation**: Generate Jira tickets and GitHub issues from natural language descriptions, extracting relevant information and formatting it appropriately.

2. **Streamline Pull Request Workflows**: Automatically draft comprehensive PR descriptions by analyzing code changes, commit history, and related issues.

3. **Enhance Code Reviews**: Provide intelligent code analysis and suggestions, ensuring consistency and quality in review feedback.

4. **Unified Interface**: Offer a single conversational interface that eliminates context switching between multiple tools.

5. **Context-Aware Operations**: Maintain conversation context and project history to provide relevant, informed responses and actions.

### Key Capabilities

- **Natural Language Interface**: Interact with development tools using conversational language
- **Multi-Tool Integration**: Seamlessly work with GitHub, Jira, and other development platforms
- **Intelligent Automation**: Understand user intent and execute appropriate actions
- **Context Preservation**: Maintain session context for coherent multi-turn conversations
- **Error Handling**: Robust retry logic and error recovery for reliable operations

## Setup Instructions

### Prerequisites

Before setting up DevFlow, ensure you have:

1. **Python 3.8 or higher** installed on your system
2. **Google API Key** for Gemini API access ([get one here](https://makersuite.google.com/app/apikey))
3. **GitHub Personal Access Token** with appropriate permissions
4. **pip** package manager

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/joaosferreira/devflow.git
    cd devflow
    ```

2. Install ADK:

    ```bash
    pip install google-adk
    ```

### Configuration

Create a _.env_ file from the example environment file and fill in your credentials.

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
```

### Running the Agent

You can run the agent using the `adk` command.

```bash
adk run
```

## Contributing

This project is developed as part of the [Agents Intensive Capstone Project](https://www.kaggle.com/competitions/agents-intensive-capstone-project). Contributions, feedback, and suggestions are welcome!
