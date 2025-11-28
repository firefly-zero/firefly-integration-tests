from firefly_test import Input
from .manager import Manager


def test_buttons__none_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            if b.AnyPressed() {
                panic("")
            }
        """,
    )
    manager.app.start()
    manager.app.update()


def test_buttons__s_pressed(manager: Manager) -> None:
    manager.build(
        update="""
            b := ReadButtons(GetMe())
            if !b.S || !b.AnyPressed() {
                panic("")
            }
            if b.E || b.W || b.N {
                panic("")
            }
        """,
    )
    manager.app.start()
    manager.app.update(Input(s=True))
