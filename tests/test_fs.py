from .manager import Manager


def test_load_file(manager: Manager) -> None:
    manager.build_and_render(
        boot="""
            old := "hello"
            DumpFile("fname", []byte(old))
            new := LoadFile("fname", nil)
            assert(string(new.Raw) == old)
        """,
    )


def test_get_file_size(manager: Manager) -> None:
    manager.build_and_render(
        boot="""
            assert(GetFileSize("fname") == 0)
            assert(!FileExists("fname"))
            DumpFile("fname", []byte("hello"))
            assert(GetFileSize("fname") == 5)
            assert(FileExists("fname"))
        """,
    )


def test_remove_file(manager: Manager) -> None:
    manager.build_and_render(
        boot="""
            DumpFile("fname", []byte("hello"))
            RemoveFile("fname")
            assert(!FileExists("fname"))
        """,
    )
