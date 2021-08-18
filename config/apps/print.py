from libqtile.lazy import lazy
from libqtile.log_utils import logger
from datetime import datetime
from .user import User


def screenshots(selection: bool=False, clipboard: bool=False) -> None:
    """Takes a usual screeshot
    """
    global count
    now = datetime.now()
    nowfmt = now.strftime("%Y.%m.%d-%H.%M.%S")
    maim_args = '-u -b 3 -m 5'
    filename = User.Dirs.Screenshots.joinpath(f'{nowfmt}.screenshot.png')
    logger.warning(filename)

    if selection:
        maim_args += ' -s'

    cmd = f'maim {maim_args} {filename}'
    if clipboard:
        cmd += f' && xclip -selection clipboard -t image/png {filename} &>/dev/null'
    logger.warning(f'\n{filename = }\n{cmd = }\n{selection = }\n {clipboard = }\n')
    lazy.spawn(cmd)
