from firefly_test import Input, Pad
from .manager import Manager


def test_buttons__none_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            assert(!b.AnyPressed())
        """,
    )
    manager.app.start()
    manager.app.update()


def test_buttons__s_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            assert(b.S)
            assert(b.AnyPressed())
            assert(!b.E && !b.W && !b.N)
        """,
    )
    manager.app.start()
    manager.app.update(Input(s=True))


def test_buttons__e_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            assert(b.E)
            assert(b.AnyPressed())
            assert(!b.S && !b.W && !b.N)
        """,
    )
    manager.app.start()
    manager.app.update(Input(e=True))


def test_buttons__w_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            assert(b.W)
            assert(b.AnyPressed())
            assert(!b.S && !b.E && !b.N)
        """,
    )
    manager.app.start()
    manager.app.update(Input(w=True))


def test_buttons__n_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            assert(b.N)
            assert(b.AnyPressed())
            assert(!b.S && !b.E && !b.W)
        """,
    )
    manager.app.start()
    manager.app.update(Input(n=True))


def test_buttons__all_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            assert(b.S && b.E && b.W && b.N)
            assert(b.AnyPressed())
        """,
    )
    manager.app.start()
    input = Input(s=True, e=True, w=True, n=True)
    manager.app.update(input)


def test_pad__not_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            _, pressed := ReadPad(GetMe())
            assert(!pressed)
        """,
    )
    manager.app.start()
    manager.app.update(Input())


def test_pad__pressed(manager: Manager) -> None:
    manager.build(
        update="""
            pad, pressed := ReadPad(GetMe())
            assert(pressed)
            assert(pad.X == 42)
            assert(pad.Y == 564)
        """,
    )
    manager.app.start()
    input = Input(pad=Pad(x=42, y=564))
    manager.app.update(input)


def test_pad__negative(manager: Manager) -> None:
    manager.build(
        update="""
            pad, pressed := ReadPad(GetMe())
            assert(pressed)
            assert(pad.X == -42)
            assert(pad.Y == -564)
        """,
    )
    manager.app.start()
    input = Input(pad=Pad(x=-42, y=-564))
    manager.app.update(input)
