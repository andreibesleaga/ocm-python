from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `ocm.resources` module.

    This is used so that we can lazily import `ocm.resources` only when
    needed *and* so that users can just import `ocm` and reference `ocm.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("ocm.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
