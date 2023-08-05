from contextlib import AsyncExitStack
from typing import Any

from fastapi import Depends, FastAPI, Request

from flexdi import Injector


def FlexDepends(target: Any) -> Any:
    async def depends(request: Request) -> Any:
        if not (injector := getattr(request, "_injector", None)):
            raise Exception("Request Injector instance was not initialized")
        return await injector.ainvoke(target)

    return Depends(depends)


class FastAPIInjector(Injector):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()

        async def request_injector(request: Request):
            async with self.chain() as sub_injector:
                setattr(request, "_injector", sub_injector)
                yield

        app.router.dependencies.insert(0, Depends(request_injector))

        @app.on_event("startup")
        async def startup():
            await self._enter()

        @app.on_event("shutdown")
        async def shutdown():
            async with self:
                pass
