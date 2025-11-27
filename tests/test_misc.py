from .manager import Manager


def test_log_debug(manager: Manager) -> None:
    manager.build_and_render(boot='LogDebug("hello")')


def test_get_random(manager: Manager) -> None:
    manager.build_and_render(boot="""
        if GetRandom() == GetRandom() {
            panic("")
        }
    """)
