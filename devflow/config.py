from google.genai import types
from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AgentConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    openai_api_key: str | None = None
    github_personal_access_token: str

    # Model configuration
    agent_model: str = Field(default="gemini-2.5-flash")

    @model_validator(mode="after")
    def check_openai_model(self):
        if self.agent_model.startswith(("gpt-", "o3-", "o4-")):
            if not self.openai_api_key:
                raise ValueError(
                    f"OPENAI_API_KEY environment variable is required for model '{self.agent_model}'"
                )
            self.agent_model = f"openai/{self.agent_model}"
        return self


agent_config = AgentConfig()

# Retry configuration for API calls
retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)
