# Copyright (C) 2021-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import functools
import logging
from typing import Any
from typing import Awaitable
from typing import Callable

import fastapi

from .abortable import Abortable
from .iauthorizationcontextfactory import IAuthorizationContextFactory
from .iprincipal import IPrincipal
from .iroutable import IRoutable
from .forbidden import Forbidden
from .notauthorized import NotAuthorized


class IEndpoint:
    __module__: str = 'cbra.types'
    allowed_http_methods: list[str]
    context_factory: IAuthorizationContextFactory
    handlers: list[IRoutable]
    include_in_schema: bool = True
    logger: logging.Logger = logging.getLogger('uvicorn')

    #: The set of permissions supported by this endpoint. These must be
    #: defined beforehand to limit the number of calls to remote IAM
    #: systems.
    permissions: set[str]

    principal: IPrincipal
    request: fastapi.Request
    response: fastapi.Response
    router: fastapi.APIRouter

    #: Indicates if all requests to the endpoint must be authenticated.
    require_authentication: bool = False

    @staticmethod
    def require_permission(name: str) -> Callable[..., Any]:
        """Decorate a method on an :class:`~cbra.types.IEndpoint` implementation
        to require the given permission. If the request does not have permission
        `name`, then :class:`~cbra.types.Forbidden` is raised.
        """
        def decorator_factory(
            func: Callable[..., Any]
        ) -> Callable[['IEndpoint'], Awaitable[Any]]:
            @functools.wraps(func)
            async def f(self: 'IEndpoint', *args: Any, **kwargs: Any) -> Any:
                if not await self.is_authorized(name):
                    raise Forbidden
                return await func(self, *args, **kwargs)
            return f
        return decorator_factory

    def get_success_headers(self, data: Any) -> dict[str, Any]:
        """Return a mapping holding the headers to add on a successful
        request based on the return value of the request handler.
        """
        return {}

    async def run_handler(
        self,
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any
    ):
        try:
            self.ctx = await self.context_factory.authenticate(self.request, self.principal)
            if self.require_authentication and not self.ctx.is_authenticated():
                raise NotAuthorized
            return await func(self, *args, **kwargs)
        except Abortable as exc:
            return await exc.as_response()

    async def is_authorized(self, name: str) -> bool:
        """Return a boolean if the given authorization context has a
        certain permission.
        """
        await self.ctx.authorize()
        return self.has_permission(name)

    def has_permission(self, name: str) -> bool:
        """Return a boolean if the request has the given permission."""
        return self.ctx.has_permission(name)