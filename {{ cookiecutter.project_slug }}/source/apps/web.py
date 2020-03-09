from typing import Dict

from fastapi import FastAPI

from .. import __version__

#: Provides the web aplication instance.
App = FastAPI()


@App.get("/version")
def version() -> Dict[str, str]:
    return {"version": __version__}
