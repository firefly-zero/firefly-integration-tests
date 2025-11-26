from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from firefly_test import CLI, App


TEMPLATE_PATH = Path(__file__).parent / "template.go"
TEMPLATE = TEMPLATE_PATH.read_text("utf-8")


@dataclass
class Manager:
    root: Path

    @cached_property
    def app_path(self) -> Path:
        path = self.root / "app"
        path.mkdir()
        return path

    @cached_property
    def vfs_path(self) -> Path:
        path = self.root / "vfs"
        path.mkdir()
        return path

    @cached_property
    def cli(self) -> CLI:
        return CLI(vfs=self.vfs_path)

    @cached_property
    def app(self) -> App:
        return App(id="test.app", vfs_path=self.vfs_path)

    @staticmethod
    def render(
        boot: str | None = None,
        update: str | None = None,
        render: str | None = None,
    ) -> str:
        result = TEMPLATE
        if boot:
            result = result.replace("// BOOT", boot)
        if update:
            result = result.replace("// UPDATE", update)
        if render:
            result = result.replace("// RENDER", render)
        return result

    def build(self, code: str) -> None:
        path = self.app_path / "main.go"
        path.write_text(code)
        ...
        self.cli.build(root=self.app_path)
