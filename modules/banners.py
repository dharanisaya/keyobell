from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from modules.utils import get_terminal_width


def print_banner(console) -> None:
    width = get_terminal_width()
    height = 8
    banner = """\
 
                                                                                                                                
                                                                         bbbbbbbb                                               
kkkkkkkk                                                                 b::::::b                               lllllll lllllll 
k::::::k                                                                 b::::::b                               l:::::l l:::::l 
k::::::k                                                                 b::::::b                               l:::::l l:::::l 
k::::::k                                                                  b:::::b                               l:::::l l:::::l 
 k:::::k    kkkkkkk eeeeeeeeeeee  yyyyyyy           yyyyyyy ooooooooooo   b:::::bbbbbbbbb        eeeeeeeeeeee    l::::l  l::::l 
 k:::::k   k:::::kee::::::::::::ee y:::::y         y:::::yoo:::::::::::oo b::::::::::::::bb    ee::::::::::::ee  l::::l  l::::l 
 k:::::k  k:::::ke::::::eeeee:::::eey:::::y       y:::::yo:::::::::::::::ob::::::::::::::::b  e::::::eeeee:::::eel::::l  l::::l 
 k:::::k k:::::ke::::::e     e:::::e y:::::y     y:::::y o:::::ooooo:::::ob:::::bbbbb:::::::be::::::e     e:::::el::::l  l::::l 
 k::::::k:::::k e:::::::eeeee::::::e  y:::::y   y:::::y  o::::o     o::::ob:::::b    b::::::be:::::::eeeee::::::el::::l  l::::l 
 k:::::::::::k  e:::::::::::::::::e    y:::::y y:::::y   o::::o     o::::ob:::::b     b:::::be:::::::::::::::::e l::::l  l::::l 
 k:::::::::::k  e::::::eeeeeeeeeee      y:::::y:::::y    o::::o     o::::ob:::::b     b:::::be::::::eeeeeeeeeee  l::::l  l::::l 
 k::::::k:::::k e:::::::e                y:::::::::y     o::::o     o::::ob:::::b     b:::::be:::::::e           l::::l  l::::l 
k::::::k k:::::ke::::::::e                y:::::::y      o:::::ooooo:::::ob:::::bbbbbb::::::be::::::::e         l::::::ll::::::l
k::::::k  k:::::ke::::::::eeeeeeee         y:::::y       o:::::::::::::::ob::::::::::::::::b  e::::::::eeeeeeee l::::::ll::::::l
k::::::k   k:::::kee:::::::::::::e        y:::::y         oo:::::::::::oo b:::::::::::::::b    ee:::::::::::::e l::::::ll::::::l
kkkkkkkk    kkkkkkk eeeeeeeeeeeeee       y:::::y            ooooooooooo   bbbbbbbbbbbbbbbb       eeeeeeeeeeeeee llllllllllllllll
                                        y:::::y                                                                                 
                                       y:::::y                                                                                  
                                      y:::::y                                                                                   
                                     y:::::y                                                                                    
                                    yyyyyyy                                                                                     
                                                                                                                                
                                                                                                                                


"""


    panel = Panel(
        Align(
            Text(banner, justify="center", style="blue"),
            vertical="middle",
            align="center",
        ),
        width=width,
        height=height,
        subtitle="by dharanisaya (https://auto.pwnspot.com)",
    )
    console.print(panel)
