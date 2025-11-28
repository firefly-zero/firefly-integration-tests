from firefly_test import Input
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
