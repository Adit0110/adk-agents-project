'''from . import agent'''

# getting_agent/__init__.py
"""Expose the Agent instance at package level so ADK entrypoint 'getting_agent.agent' works."""
from .agent import agent

__all__ = ["agent"]
