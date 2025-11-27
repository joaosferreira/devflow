import os
from google.genai import types

# Application configuration
APP_NAME = os.getenv("APP_NAME", "devflow")
USER_ID = os.getenv("USER_ID", "default_user")
SESSION_ID = os.getenv("SESSION_ID", "default_session")

# Model configuration
AGENT_MODEL = os.getenv("AGENT_MODEL", "gemini-2.5-flash")

# Retry configuration for API calls
retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)
