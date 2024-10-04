from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from modules.utils import get_terminal_width


def print_banner(console) -> None:
    width = get_terminal_width()
    height = 12
    banner = """\

    __                        __           __ __
   / /__ ___   __  __ ____   / /_   ___   / // /
  / //_// _ \ / / / // __ \ / __ \ / _ \ / // / 
 / ,<  /  __// /_/ // /_/ // /_/ //  __// // /  
/_/|_| \___/ \__, / \____//_.___/ \___//_//_/   
            /____/                              
                                                         

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
