import os
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

@dataclass
class Message:
    """Represents a message in a conversation."""
    role: str  # "system", "user", or "assistant"
    content: str

@dataclass
class LLMConfig:
    """Configuration for LLM API calls."""
    model: str
    temperature: float = 0.7
    max_tokens: int = 500

def simple_query(prompt: str, config: LLMConfig = None) -> str:
    """
    Sends a query to the LLM and returns the response.
    """
    if config is None:
        config = LLMConfig(model="gpt-4o", temperature=0.7)

    messages = []
    if system_prompt:
        messages.append(Message(role="system", content=system_prompt))
    messages.append(Message(role="user", content=prompt))

    return create_completion(messages, config)