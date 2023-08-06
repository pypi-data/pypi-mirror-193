import dataclasses
import pathlib
import typing
import datetime
import re


_OBSOLETES_REGEX = re.compile(
    r'-\s*Obsoletes\s*:\s*<!--\s*obsoletes\s*-->\s*((\d+)(\s*,\s*(\d+))*)?',
    re.RegexFlag.IGNORECASE
)


@dataclasses.dataclass(frozen=True)
class RfcMetadata:
    file: pathlib.Path
    number: int
    obsoletes: typing.List[int]
    obsoleted_by: typing.List[int]
    content_lines: typing.Optional[typing.List[str]]
    content: typing.Optional[str]

    def to_json_dict(self, modified_at: typing.Optional[datetime.datetime] = None) -> typing.Dict[str, typing.Any]:
        d = {
            'number': self.number,
            'obsoletes': self.obsoletes,
            'obsoletedBy': self.obsoleted_by
        }
        if modified_at is not None:
            d['lastModified'] = modified_at.isoformat()
        return d

    def get_content_obsoletes(self) -> typing.Optional[typing.List[int]]:
        if self.content_lines is None:
            return None
        for line in self.content_lines:
            if not line.startswith('- Obsoletes'):
                continue

            match = _OBSOLETES_REGEX.match(line)
            if match is None:
                return []
            obsoletes = match.group(1)
            if obsoletes is None:
                return []
            return sorted((int(s.strip()) for s in obsoletes.split(',')))
        return []


_RFC_REGEX = re.compile(r'\w+(\d+)')


class Rfcs:
    def __init__(self, rfcs: typing.Dict[int, RfcMetadata]):
        self.__rfcs = rfcs

    def find(self, code: typing.Union[int, str]) -> typing.Optional[RfcMetadata]:
        if isinstance(code, str):
            code = int(_RFC_REGEX.match(code)[1])
        if code in self.__rfcs:
            return self.__rfcs[code]
        return None

    def get_latest_number(self) -> int:
        if len(self.__rfcs) == 0:
            return 0
        return sorted(self.__rfcs.keys())[-1] + 1

    @property
    def rfcs(self) -> typing.Iterable[RfcMetadata]:
        return self.__rfcs.values()
