from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from modules.utils import get_terminal_width


def print_banner(console) -> None:
    width = get_terminal_width()
    height = 8
    banner = """\
 
 _                        _            _  _ 
| | __ ___  _   _   ___  | |__    ___ | || |
| |/ // _ \| | | | / _ \ | '_ \  / _ \| || |
|   <|  __/| |_| || (_) || |_) ||  __/| || |
|_|\_\\___| \__, | \___/ |_.__/  \___||_||_|
            |___/                           
                                                                                    

"""


    panel = Panel(
        Align(
            Text(banner, justify="center", style="blue"),
            vertical="middle",
            align="center",
        ),
        width=width,
        height=height,
        subtitle="by dharanisaya (https://github.com/dharanisaya/keyobell.git)",
    )
    console.print(panel)
