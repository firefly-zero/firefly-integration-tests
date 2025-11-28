import pytest
from .manager import Manager


def test_unreachable(manager: Manager) -> None:
    msg = "error calling boot: wasm `unreachable` instruction executed."
    with pytest.raises(RuntimeError, match=msg):
        manager.build_and_render(boot='assert(false)')


def test_log_debug(manager: Manager) -> None:
    manager.build_and_render(boot='LogDebug("hello")')


def test_get_random(manager: Manager) -> None:
    manager.build_and_render(boot="assert(GetRandom() != GetRandom())")


def test_get_name(manager: Manager) -> None:
    manager.build_and_render(boot="""
        name := GetName(GetMe())
        assert(len(name) >= 4)
        assert(len(name) <= 16)
        // In the offline mode, any peer ID (even invalid one)
        // returns the current device name.
        assert(GetName(60) == name)
    """)
