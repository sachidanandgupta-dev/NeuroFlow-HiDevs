from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncGenerator

@dataclass
class ChatMessage:
    role: str
    content: str | list

@dataclass
class GenerationResult:
    content: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    cost_usd: float
    finish_reason: str

class BaseLLMProvider(ABC):
    @abstractmethod
    async def complete(self, messages: list[ChatMessage], **kwargs) -> GenerationResult: ...

    @abstractmethod
    async def stream(self, messages: list[ChatMessage], **kwargs) -> AsyncGenerator[str, None]: ...

    @abstractmethod
    async def embed(self, texts: list[str]) -> list[list[float]]: ...
