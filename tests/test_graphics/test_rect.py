from firefly_test import Color
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


def test_rect_solid_w1(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(1, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●R●●●●●●
        ●R●●●●●●
        ●R●●●●●●
        ●●●●●●●●
    """)


def test_rect_solid_w2(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(2, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RR●●●●●
        ●RR●●●●●
        ●RR●●●●●
        ●●●●●●●●
    """)


def test_rect_solid_w3(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(3, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRR●●●●
        ●RRR●●●●
        ●RRR●●●●
        ●●●●●●●●
    """)


def test_rect_solid_w4(manager: Manager) -> None:
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


def test_rect_solid_w5(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(5, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRRR●●
        ●RRRRR●●
        ●RRRRR●●
        ●●●●●●●●
    """)


def test_rect_solid_w6(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(6, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRRRR●
        ●RRRRRR●
        ●RRRRRR●
        ●●●●●●●●
    """)


def test_rect_solid_w7(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(7, 3), Solid(ColorRed))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●●
        ●RRRRRRR●
        ●RRRRRRR●
        ●RRRRRRR●
        ●●●●●●●●●
    """)


def test_rect_w1_outlined(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(4, 3), Outlined(ColorRed, 1))',
    )
    sub = manager.app.frame.get_sub(x=11, y=12)
    sub.assert_match("""
        ●●●●●●●●
        ●RRRR●●●
        ●R●●R●●●
        ●RRRR●●●
        ●●●●●●●●
    """)


def test_rect_w2_outlined(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(5, 4), Outlined(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=10, y=11)
    # For even line width, outline has the additional pixels on the inside.
    sub.assert_match("""
        ●●●●●●●●●●
        ●RRRRRRR●●
        ●RRRRRRR●●
        ●RR●●●RR●●
        ●RR●●●RR●●
        ●RRRRRRR●●
        ●RRRRRRR●●
        ●●●●●●●●●●
    """)


def test_rect_w3_outlined(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(6, 5), Outlined(ColorRed, 3))',
    )
    sub = manager.app.frame.get_sub(x=10, y=11)
    # For width over 1, outline grows equally inside and outside.
    sub.assert_match("""
        ●●●●●●●●●●●
        ●RRRRRRRR●●
        ●RRRRRRRR●●
        ●RRRRRRRR●●
        ●RRR●●RRR●●
        ●RRRRRRRR●●
        ●RRRRRRRR●●
        ●RRRRRRRR●●
        ●●●●●●●●●●●
    """)


def test_rect_w1_ident_vert(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(3, 0), Outlined(ColorRed, 1))',
    )
    for color in manager.app.frame:
        assert color == Color.BLACK


def test_rect_w2_ident_vert(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(3, 0), Outlined(ColorRed, 2))',
    )
    sub = manager.app.frame.get_sub(x=10, y=12)
    sub.assert_match("""
        ●●●●●●●
        ●RRRRR●
        ●RRRRR●
        ●●●●●●●
    """)


def test_rect_w3_ident_vert(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(3, 0), Outlined(ColorRed, 3))',
    )
    sub = manager.app.frame.get_sub(x=10, y=12)
    sub.assert_match("""
        ●●●●●●●
        ●RRRRR●
        ●RRRRR●
        ●●●●●●●
    """)


def test_rect_w1_ident_hor(manager: Manager) -> None:
    manager.build_and_render(
        boot='DrawRect(P(12, 13), S(0, 3), Outlined(ColorRed, 1))',
    )
    for color in manager.app.frame:
        assert color == Color.BLACK
