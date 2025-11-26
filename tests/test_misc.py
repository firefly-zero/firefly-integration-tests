from pathlib import Path
from .manager import Manager


def test_log_debug(tmp_path: Path) -> None:
    manager = Manager(tmp_path)
    code = manager.render(boot='firefly.LogDebug("hello")')
    manager.build(code)
    manager.app.start()
