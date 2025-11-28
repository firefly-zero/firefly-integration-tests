from .manager import Manager


def test_file_roundtrip(manager: Manager) -> None:
    manager.build_and_render(
        boot="""
            old := "hello"
            DumpFile("fname", []byte(old))
            new := LoadFile("fname", nil)
            assert(string(new.Raw) == old)
        """,
    )
