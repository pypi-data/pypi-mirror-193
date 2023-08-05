from dataclasses import dataclass

from fastapi import FastAPI
from starlette.testclient import TestClient

from flexdi.fastapi.injector import FastAPIInjector, FlexDepends

app = FastAPI()
injector = FastAPIInjector(app)


@dataclass
class Foo:
    def __init__(self):
        print("init")

    pass


@injector.binding(bind_to=Foo, scope="singleton")
async def foo_getter():
    print("start getter")
    yield Foo()
    print("finish getter")


@app.get("/")
def endpoint(foo: Foo = FlexDepends(Foo), foo2: Foo = FlexDepends(Foo)):
    print(f"foo endpoint {id(foo)} {id(foo2)}")
    return str(foo)


with TestClient(app) as client, injector:
    print(client.get("/").content)
    print(client.get("/").content)
