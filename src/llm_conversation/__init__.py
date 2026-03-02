'''
Functionality for example namespace:

import template

ns = template.item_1()
'''
from __future__ import annotations
from typing import TYPE_CHECKING


# Public, supported “namespaces”.
__all__ = ("Conversation")


# Helps IDEs/type-checkers know these exist and what they are,
# without importing them at runtime.
if TYPE_CHECKING:
    from .main import Conversation


def __getattr__(name: str):
    if name == 'Conversation':
        from .main import Conversation
        globals()[name] = Conversation  # Recommended for smoother checking.
        return Conversation

    raise AttributeError(f'Module "<lib name>" has no attribute {name!r}!')  # TODO: Edit your library name.


def __dir__() -> list[str]:
    # Makes dir(llm) include your lazy “namespaces”.
    return sorted(set(globals().keys()) | set(__all__))