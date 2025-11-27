from .manager import Manager


def test_log_debug(manager: Manager) -> None:
    manager.build(boot='LogDebug("hello")')
    manager.app.start()
