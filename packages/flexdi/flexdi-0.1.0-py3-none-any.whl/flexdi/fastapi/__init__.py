from typing import Any, AsyncIterator

from fastapi import Depends, FastAPI, Request

from flexdi import FlexPack


def FlexDepends(target: Any) -> Any:
    async def depends(request: Request) -> Any:
        if not (flex := getattr(request, "_flex", None)):
            raise Exception("FlexPack instance was not initialized")
        return await flex.ainvoke(target)

    return Depends(depends)


class FastAPIFlexPack(FlexPack):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        app.router.dependencies.insert(0, Depends(self.attach_flex))
        app.on_event("startup")(self.aopen)
        app.on_event("shutdown")(self.aclose)

    async def attach_flex(self, request: Request) -> AsyncIterator[None]:
        async with self.chain() as flex:
            setattr(request, "_flex", flex)
            yield


__all__ = ["FlexDepends", "FastAPIFlexPack"]
