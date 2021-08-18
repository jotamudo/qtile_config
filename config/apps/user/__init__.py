from .dirs import Dirs, UserPaths
from dataclasses import dataclass

@dataclass
class UserUtils:
    Dirs: UserPaths = Dirs

User = UserUtils()
