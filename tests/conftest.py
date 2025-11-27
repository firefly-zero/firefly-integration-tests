
from pathlib import Path
from pytest import fixture
from .manager import Manager


@fixture
def manager(tmp_path: Path) -> Manager:
    return Manager(tmp_path)
