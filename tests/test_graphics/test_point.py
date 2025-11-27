from pathlib import Path

from firefly_test import Color
from ..manager import Manager


def test_point_1(tmp_path: Path) -> None:
    manager = Manager(tmp_path)
    manager.build(boot='DrawPoint(P(12, 14), ColorRed)')
    manager.app.start()
    manager.app.update()
    manager.app.update()
    assert manager.app.frame.at(12, 14) == Color.RED
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        KKK
        KRK
        KKK
    """)
