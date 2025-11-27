from firefly_test import Color
from ..manager import Manager


def test_point_basic(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawPoint(P(12, 14), ColorRed)',
    )
    assert manager.app.frame.at(12, 14) == Color.RED
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        KKK
        KRK
        KKK
    """)


def test_point_out_of_bounds(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawPoint(P(260, 14), ColorRed)',
    )
    for color in manager.app.frame:
        assert color == Color.BLACK
