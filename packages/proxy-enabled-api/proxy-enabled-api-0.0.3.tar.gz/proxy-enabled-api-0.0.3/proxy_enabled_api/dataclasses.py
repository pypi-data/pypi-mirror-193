
from dataclasses import dataclass
from datetime import datetime
from typing import Coroutine

from .taxonomies import (
    ServerType,
    BodyType,
    HTTPMethod,
    EC2State,
)


@dataclass
class Server:
    """Server information."""

    caught: datetime
    sent: datetime
    type: ServerType


@dataclass
class Runnable:
    """Single runnable information."""
    
    coro: HTTPMethod
    url: str
    body_type: BodyType


@dataclass
class Proxy:

    ip_address: str
    url: str 
    state: EC2State
    created: datetime
    terminated: datetime
    timeout: int
    max_usage: int
    

