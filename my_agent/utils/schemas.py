from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

class GraphConfig(TypedDict):
    model_name: Literal["openai"]
    thread_id: str
    user_id: str
