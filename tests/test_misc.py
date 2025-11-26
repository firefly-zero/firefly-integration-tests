from pathlib import Path
from .manager import Manager


def test_log_debug(tmp_path: Path) -> None:
    manager = Manager(tmp_path)
    manager.build(boot='LogDebug("hello")')
    manager.app.start()
