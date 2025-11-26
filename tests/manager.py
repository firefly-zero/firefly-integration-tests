from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from firefly_test import CLI, App


ROOT = Path(__file__).parent.parent
CODE_TEMPLATE = (ROOT / "template" / "main.go").read_text("utf-8")
GOMOD = (ROOT / "template" / "go.mod").read_text("utf-8")
GOSUM = (ROOT / "template" / "go.sum").read_text("utf-8")
CONFIG = (ROOT / "template" / "firefly.toml").read_text("utf-8")


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
        result = CODE_TEMPLATE
        if boot:
            result = result.replace("// BOOT", boot)
        if update:
            result = result.replace("// UPDATE", update)
        if render:
            result = result.replace("// RENDER", render)
        return result

    def build(self, code: str) -> None:
        (self.app_path / "main.go").write_text(code)
        (self.app_path / "go.mod").write_text(GOMOD)
        (self.app_path / "go.sum").write_text(GOSUM)
        (self.app_path / "firefly.toml").write_text(CONFIG)
        self.cli.build(root=self.app_path)
