"""OAuth module configuration."""

__all__ = ["oauth2config"]

from pydantic import BaseModel, Field
from typing import Callable


callback_description = """Callback to be called when a user logs in.

This callback is called with the user's Oauth data, and should return a
coroutine that resolves to a dict-like object containing the response.
e.g. session id, local user data etc.
"""


class OAuth2ProviderConfig(BaseModel):
    provider: str
    client_id: str
    client_secret: str
    additional_scopes: list[str] = Field(
        default_factory=list,
        description="Additional scopes",
    )


class OAuth2Config(BaseModel):
    """OAuth module configuration."""

    providers: list[OAuth2ProviderConfig] = Field(
        default_factory=list, description="List of OAuth providers to enable."
    )

    login_callback: Callable | None = Field(None, description=callback_description)
    login_response_model: BaseModel | None = None

    enable_redirect_endpoint: bool = True

    def add_provider(self, name: str, client_id: str, client_secret: str, additional_scopes: list[str] = None):
        if additional_scopes is None:
            additional_scopes = []
        self.providers.append(
            OAuth2ProviderConfig(
                provider=name, client_id=client_id, client_secret=client_secret, additional_scopes=additional_scopes,
            )
        )


oauth2config = OAuth2Config()
