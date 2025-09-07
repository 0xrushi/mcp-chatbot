"""
MyLLM - A Python package for MCP (Model Context Protocol) chatbot interactions.

This package provides tools for connecting to MCP servers and interacting with LLMs
through a unified interface.
"""

from .core import Configuration, Server, Tool, LLMClient, ChatSession
from .cli import main

__version__ = "0.1.0"

__all__ = [
    "Configuration",
    "Server", 
    "Tool",
    "LLMClient",
    "ChatSession",
    "main"
]
