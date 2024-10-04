from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from modules.utils import get_terminal_width


def print_banner(console) -> None:
    width = get_terminal_width()
    height = 8
    banner = """\
   _               _  _           _                 _       _             
  | |__    ___    | || |   ___   | |__     ___     | |     | |      o O O 
  | / /   / -_)    \_, |  / _ \  | '_ \   / -_)    | |     | |     o      
  |_\_\   \___|   _|__/   \___/  |_.__/   \___|   _|_|_   _|_|_   TS__[O] 
_|"""""|_|"""""|_| """"|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'


"""

    banner_small = """\

.           .     ..
;_/ _   . _ |_  _ ||
| \(/,\_|(_)[_)(/,||
      ._|           

"""

    if width < 90:
        banner = banner_small
        height = 5

    panel = Panel(
        Align(
            Text(banner, justify="center", style="blue"),
            vertical="middle",
            align="center",
        ),
        width=width,
        height=height,
        subtitle="by dharanisaya (https://keyobell.com)",
    )
    console.print(panel)
