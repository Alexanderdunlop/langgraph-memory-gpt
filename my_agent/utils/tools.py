# from langchain_community.tools.tavily_search import TavilySearchResults

# tools = [TavilySearchResults(max_results=1)]

from datetime import datetime
from typing import Annotated, TypedDict, Union

from langchain_core.tools import tool

@tool
def get_now(format: str = "%Y-%m-%d %H:%M:%S"):
    """
    Get the current time
    """
    return datetime.now().strftime(format)


tools = [get_now]