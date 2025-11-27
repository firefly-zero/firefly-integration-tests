from ..manager import Manager


def test_rect_w1_filled(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(4, 3), Style{ColorWhite, ColorRed, 1})',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRR●●●
        ●R○○R●●●
        ●RRRR●●●
        ●●●●●●●●
    """)


def test_rect_w1_solid(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(4, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRR●●●
        ●RRRR●●●
        ●RRRR●●●
        ●●●●●●●●
    """)
