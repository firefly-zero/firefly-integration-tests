from firefly_test import Color
from ..manager import Manager


def test_point_basic(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawPoint(P(12, 14), ColorRed)',
    )
    assert manager.app.frame.at(12, 14) == Color.RED
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        ●●●
        ●R●
        ●●●
    """)


def test_point_out_of_bounds(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawPoint(P(260, 14), ColorRed)',
    )
    for color in manager.app.frame:
        assert color == Color.BLACK


def test_point_colors(manager: Manager) -> None:
    manager.build_and_render(
        boot="""
            DrawPoint(P(12, 14), ColorBlack)
            DrawPoint(P(13, 14), ColorPurple)
            DrawPoint(P(14, 14), ColorRed)
            DrawPoint(P(15, 14), ColorOrange)
            DrawPoint(P(16, 14), ColorYellow)
            DrawPoint(P(17, 14), ColorLightGreen)
            DrawPoint(P(18, 14), ColorGreen)
            DrawPoint(P(19, 14), ColorDarkGreen)

            DrawPoint(P(12, 15), ColorDarkBlue)
            DrawPoint(P(13, 15), ColorBlue)
            DrawPoint(P(14, 15), ColorLightBlue)
            DrawPoint(P(15, 15), ColorCyan)
            DrawPoint(P(16, 15), ColorWhite)
            DrawPoint(P(17, 15), ColorLightGray)
            DrawPoint(P(18, 15), ColorGray)
            DrawPoint(P(19, 15), ColorDarkGray)
        """,
    )
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        ●●●●●●●●●●
        ●KPROYgGD●
        ●dBbCW◔◑◕●
        ●●●●●●●●●●
    """)
