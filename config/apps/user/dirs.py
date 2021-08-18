import os
from dataclasses import dataclass
from pathlib import Path


HOME = Path(os.getenv('HOME'))

@dataclass
class UserPaths:
    Pictures: Path = HOME.joinpath('Pictures')
    Screenshots: Path = Pictures.joinpath('Screenshots')

Dirs = UserPaths()
