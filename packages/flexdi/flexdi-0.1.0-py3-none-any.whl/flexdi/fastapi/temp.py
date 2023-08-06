from dataclasses import dataclass
from typing import AsyncIterator

from fastapi import FastAPI
from starlette.testclient import TestClient

from flexdi.fastapi import FastAPIFlexPack, FlexDepends

app = FastAPI()
flex = FastAPIFlexPack(app)


@dataclass
class Foo:
    def __init__(self) -> None:
        print("init")

    pass


@flex.bind(target=Foo, eager=True)
async def foo_getter() -> AsyncIterator[Foo]:
    print("start getter")
    yield Foo()
    print("finish getter")


@app.get("/")
def endpoint(foo: Foo = FlexDepends(Foo), foo2: Foo = FlexDepends(Foo)) -> str:
    print(f"foo endpoint {id(foo)} {id(foo2)}")
    return str(foo)


with TestClient(app) as client, flex:
    print(client.get("/").content)
    print(client.get("/").content)
