import abc
import importlib
import inspect
from pathlib import Path
from typing import Any, Generic, Sequence, TypeVar


class _Finder(abc.ABC):
    """_Finder possui a funcionalidade de importar recursivamente todos os módulos de
    um determinado repositório :param:`path` a partir de uma raiz :param:`root` - se
    não passada, usa o path como raiz - para encontrar estruturas que precisam existir
    no namespace da aplicação durante a inicialização. Exemplo: Na execução de um auto
    discovery de models de um determinado ORM."""

    def __init__(
        self,
        path: Path,
        root: Path | None = None,
        excluded: Sequence[str] = (),
    ):
        self.path = path
        self._targets: dict[str, type[Any]] = {}
        self.root = root or path
        self._excluded = ('__init__.py', *excluded)

    def find(self, exclude: Sequence[str] = ()):
        self._excluded = (*self._excluded, *exclude)
        if self.path.is_dir():
            self.find_from_dir()
        else:
            self.find_from_file()

    def find_from_dir(self, path: Path | None = None):
        if path is None:
            path = self.path
        if 'pycache' in path.name or '.pyc' in path.name:
            return
        for item in path.iterdir():
            if item.is_dir():
                self.find_from_dir(item)
                continue
            if self._should_skip(item):
                continue
            self.find_from_file(item)

    def _should_skip(self, item: Path):
        return not item.name.endswith('.py') or item.name in self._excluded

    def find_from_file(self, path: Path | None = None):
        if path is None:
            path = self.path
        if not path.is_file():
            return
        mod = importlib.import_module(self.get_import(path))
        for name, obj in inspect.getmembers(mod):
            if self.is_valid_object(obj):
                self._targets[name] = obj

    def get_import(self, target: Path):
        target_str = target.as_posix()
        return (
            target_str.replace(self.root.as_posix(), self.root.name)
            .replace('/', '.')
            .replace('.py', '')
        )

    @abc.abstractmethod
    def is_valid_object(self, target: Any) -> bool:
        """is_valid_object return se :param:`target` atende o critério de busca"""

    def __iter__(self):
        yield from self._targets.items()

    def dict(self):
        return dict(self)


T = TypeVar('T')


class InstanceFinder(_Finder, Generic[T]):
    """InstanceFinder filtra os resultados encontrados pelo :param:`instance_of`,
    sendo válidos todos os objetos que sejam uma instancia dele."""

    def __init__(
        self, instance_of: type[T], *, path: Path, root: Path | None = None
    ):
        self._instance_of = instance_of
        super().__init__(path, root=root)

    def is_valid_object(self, target: Any) -> bool:
        return isinstance(target, self._instance_of)


class ClassFinder(_Finder, Generic[T]):
    """Class finder filtra os resultados encontrados pelo :param:`child_of`,
    sendo válidos todas as classes que herdem `child_of` e não sejam(comparação is)
    `child_of`"""

    def __init__(
        self, child_of: type[T], *, path: Path, root: Path | None = None
    ):
        self._child_of = child_of
        super().__init__(path, root=root)

    def is_valid_object(self, target: Any) -> bool:
        if not inspect.isclass(target):
            return False
        is_child_of = issubclass(target, self._child_of)
        is_not_parent = target is not self._child_of
        return is_child_of and is_not_parent
