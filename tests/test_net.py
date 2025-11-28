from .manager import Manager


def test_get_me__offline(manager: Manager) -> None:
    manager.build_and_render(boot="assert(GetMe() == 0)")
