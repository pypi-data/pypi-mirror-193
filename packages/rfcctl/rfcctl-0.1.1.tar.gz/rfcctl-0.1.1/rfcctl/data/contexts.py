import dataclasses
import typing
import pathlib
import json


@dataclasses.dataclass(frozen=True)
class Context:
    user: str
    name: str
    directory: str
    initial_status: str
    obsoleted_status: str


@dataclasses.dataclass(frozen=True)
class Contexts:
    current: str
    contexts: typing.Dict[str, Context]

    def switch(self, new: str):
        if new in self.contexts:
            return Contexts(new, self.contexts)
        raise RuntimeError('Context not found')

    def add(self, context: Context):
        new = self.contexts.copy()
        new[context.name] = context
        return Contexts(self.current, new)

    @property
    def current_context(self) -> Context:
        return self.contexts[self.current]

    @classmethod
    def load(cls, base_dir: pathlib.Path, *, empty_if_not_exists: bool = False):
        jf = base_dir / 'context.json'
        try:
            with open(jf) as fp:
                jo = json.load(fp)
                [print(cjo) for cjo in jo['contexts']]
                return cls(
                    current=jo['current'],
                    contexts={key: Context(**cjo) for key, cjo in jo['contexts'].items()}
                )
        except FileNotFoundError:
            if empty_if_not_exists:
                return cls('', {})
            raise

    def save(self, base_dir: pathlib.Path):
        jf = base_dir / 'context.json'
        with open(jf, 'w') as fp:
            json.dump(dataclasses.asdict(self), fp, indent=2)
