from libqtile.config import Key
from ..apps import screenshots

from . import mod
print_keys = [
        Key([],               'Print', screenshots(selection=False, clipboard=False)),
        Key(["control"],      'Print', screenshots(selection=False, clipboard=True )),
        Key([mod],            'Print', screenshots(selection=True,  clipboard=False)),
        Key([mod, "control"], 'Print', screenshots(clipboard=True,  selection=True  )),
        ]
