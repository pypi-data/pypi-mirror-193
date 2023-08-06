
from aiohttp import (
    ClientSession,
    ClientTimeout,
    TCPConnector,
    ClientError,
)
from aiohttp.hdrs import (
    METH_GET as GET,
    METH_POST as POST,
    METH_PATCH as PATCH,
    METH_DELETE as DELETE,
)
import asyncio
from logging import Logger, getLogger
import ssl
from contextlib import (
    asynccontextmanager,
)
import certifi
from abc import ABC, abstractmethod
from typing import (
    Optional,
    Coroutine,
    List,
)

from .dataclasses import (
    BodyType,
    Server,
    Runnable,
    Proxy,
)
from .taxonomies import (
    EC2State,
    ServerType,
    HTTPMethod,
)


ERROR_LIST = {
    "sending": "Sending async request to '{url}'...",
    "error": (
        "Async request to '{url}' failed. "
        "The error is described as: {status} status, {error}. "
        "Retrying..."
    ),
    "failed": (
        "Async request to '{url}' could not be completed. "
        "The API stopped retrying after {num_failed} attempts."
    ),
}

LOGGER = getLogger(__name__)


class Retry:

    def __init__(self, total: int):
        self._count = 0
        self.total = total
    
    def increment(self):
        self._count += 1
    
    def done(self):
        return self._count == self.total


class AsyncAPI(ABC):

    def __init__(
            self,
            url: Optional[str] = None,
            headers: Optional[dict] = None,
            cookies: Optional[dict] = None,
            timeout: int = 10,
            retries: int = 3, limit: int = 5, limit_per_host: int = 5,
            cafile: str = certifi.where(), 
            proxy: Optional[Proxy] = None,
            logger: Optional[Logger] = LOGGER):
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.timeout = timeout
        self.retries = retries
        self.limit = limit
        self.limit_per_host = limit_per_host
        self.cafile = cafile
        self.proxy = proxy
        self.logger = logger

    @asynccontextmanager
    async def session(self):
        certificates = ssl.create_default_context(
            cafile=self.cafile)
        tcp = TCPConnector(
            limit=self.limit, limit_per_host=self.limit_per_host,
            ssl=certificates)
        timeout = ClientTimeout(total=self.timeout)
        async with ClientSession(
                self.url, connector=tcp, cookies=self.cookies,
                timeout=timeout) as s:
            yield s

    def retry(coro: Coroutine):
        async def wrapper(self, *args, **kwargs):
            _retry = Retry(self.retries)

            while not _retry.done():
                try:
                    self.logger.info(
                        ERROR_LIST["sending"].format(
                            url=args[1])
                    )
                    return await coro(self, *args, **kwargs)
                except ClientError as e:
                    self.logger.error(
                        ERROR_LIST["error"].format(
                            url=e.request_info.url, status=e.status,
                            error=e.message)
                    )

                    _retry.increment()
            
            self.logger.critical(
                ERROR_LIST["failed"].format(
                    url=args[1], num_failed=_retry.total)
            )
        return wrapper

    @retry
    async def request(
            self, coro: Coroutine, url: str, *,
            body_type: BodyType = BodyType.JSON, **kwargs):
        async with coro(
                # may delay because proxies haven't cooled
                # down for long enough
                url, **kwargs,
                proxy=await self.proxy.next() if self.proxy else None,
                raise_for_status=True) as res:
            if (body_type == BodyType.JSON
                    or body_type not in [BodyType.BYTE, BodyType.STRING]):
                return await res.json()
            elif body_type == BodyType.BYTE:
                return await res.read()
            elif body_type == BodyType.STRING:
                return await res.text()

    def run(self, runnables: List[Runnable], **kwargs):
        return asyncio.run(
            self._run(runnables)
        )

    async def _run(self, runnables: List[Coroutine], **kwargs):
        aws = []

        async with self.session() as s:
            for runnable in runnables:
                aws.append(
                    self._bridge(
                        runnable.coro, runnable.url, s=s,
                        body_type=runnable.body_type, **kwargs)
                )

            return await asyncio.gather(*aws)

    async def _bridge(
            self, coro: str, url: str,
            s: Optional[ClientSession] = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        if s is None:
            async with self.session() as s:
                return await self.request(
                    getattr(s, coro), url,
                    body_type=body_type, **kwargs)
        else:
            return await self.request(
                    getattr(s, coro), url,
                    body_type=body_type, **kwargs)

    async def get(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.GET, url, s, body_type, **kwargs)
    
    async def post(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.POST, url, s, body_type, **kwargs)

    async def put(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.PUT, url, s, body_type, **kwargs)

    async def delete(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.DELETE, url, s, body_type, **kwargs)

    async def head(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.HEAD, url, s, body_type, **kwargs)

    async def options(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.OPTIONS, url, s, body_type, **kwargs)

    async def patch(
            self, url: str, *, s: ClientSession = None,
            body_type: BodyType = BodyType.JSON, **kwargs):
        return await self._bridge(
            HTTPMethod.PATCH, url, s, body_type, **kwargs)
