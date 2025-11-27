import pytest
from .manager import Manager


def test_unreachable(manager: Manager) -> None:
    msg = "error calling boot: wasm `unreachable` instruction executed."
    with pytest.raises(RuntimeError, match=msg):
        manager.build_and_render(boot='panic("")')


def test_log_debug(manager: Manager) -> None:
    manager.build_and_render(boot='LogDebug("hello")')


def test_get_random(manager: Manager) -> None:
    manager.build_and_render(boot="""
        if GetRandom() == GetRandom() {
            panic("")
        }
    """)


def test_get_name(manager: Manager) -> None:
    manager.build_and_render(boot="""
        name := GetName(GetMe())
        if len(name) < 4 {
            panic("")
        }
        if len(name) > 16 {
            panic("")
        }
    """)
