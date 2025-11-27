from ..manager import Manager


def test_line_w1_hor(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(17, 14), L(ColorRed, 1))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●●●●●●●●
        ●RRRRRR●
        ●●●●●●●●
    """)


def test_line_w1_hor_inverse(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(17, 14), P(12, 14), L(ColorRed, 1))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●●●●●●●●
        ●RRRRRR●
        ●●●●●●●●
    """)


def test_line_w2_hor(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(17, 14), L(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRRRR●
        ●RRRRRR●
        ●●●●●●●●
    """)


def test_line_w2_hor_inverse(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(17, 14), P(12, 14), L(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    # The order of points when drawing the line affects
    # on which side the "extra" pixels will be drawn
    # when the line width is odd.
    sub.assert_match("""
        ●●●●●●●●
        ●●●●●●●●
        ●RRRRRR●
        ●RRRRRR●
        ●●●●●●●●
    """)


def test_line_w3_hor(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(17, 14), L(ColorRed, 3))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRRRR●
        ●RRRRRR●
        ●RRRRRR●
        ●●●●●●●●
    """)


def test_line_w1_vert(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(12, 17), L(ColorRed, 1))',
    )
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        ●●●●
        ●R●●
        ●R●●
        ●R●●
        ●R●●
        ●●●●
    """)


def test_line_w2_vert(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(12, 17), L(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        ●●●●
        ●RR●
        ●RR●
        ●RR●
        ●RR●
        ●●●●
    """)


def test_line_w1_tl2br_45deg(manager: Manager) -> None:
    """Draw a 1-pixel wide line from top-left to bottom right with 45 degrees incline.
    """
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(15, 17), L(ColorRed, 1))',
    )
    sub = manager.app.frame.get_sub(x=11, y=13)
    sub.assert_match("""
        ●●●●●●
        ●R●●●●
        ●●R●●●
        ●●●R●●
        ●●●●R●
        ●●●●●●
    """)


def test_line_w2_tl2br_45deg(manager: Manager) -> None:
    """Draw a 2-pixel wide line from top-left to bottom right with 45 degrees incline.
    """
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(15, 17), L(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=11, y=13)
    # Interesting!
    sub.assert_match("""
        ●●●●●●●
        ●RR●●●●
        ●●RR●●●
        ●●●RR●●
        ●●●●R●●
        ●●●●●●●
    """)


def test_line_w1_identity(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(12, 14), L(ColorRed, 1))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●
        ●●●
        ●R●
        ●●●
    """)


def test_line_w2_identity(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawLine(P(12, 14), P(12, 14), L(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●
        ●R●
        ●R●
        ●●●
    """)
