from colorama import *

def name():

    name = f"""\
{Fore.CYAN}
   █████████                         █████████                                      ████ 
  ███░░░░░███                       ███░░░░░███                                    ░░███ 
 ███     ░░░   ██████              ███     ░░░  ████████   ██████   █████ ███ █████ ░███ 
░███          ░░░░░███  ██████████░███         ░░███░░███ ░░░░░███ ░░███ ░███░░███  ░███ 
░███           ███████ ░░░░░░░░░░ ░███          ░███ ░░░   ███████  ░███ ░███ ░███  ░███ 
░░███     ███ ███░░███            ░░███     ███ ░███      ███░░███  ░░███████████   ░███ 
 ░░█████████ ░░████████            ░░█████████  █████    ░░████████  ░░████░████    █████
  ░░░░░░░░░   ░░░░░░░░              ░░░░░░░░░  ░░░░░      ░░░░░░░░    ░░░░ ░░░░    ░░░░░ 
                                                    {Style.RESET_ALL}v.1.0 https://github.com/cagrialis/ca-crawl
    """
    description = f"{Fore.RED}{Style.BRIGHT}Description :\n" \
                  f"{Style.RESET_ALL}CaCrawl is a crawling tool, development with Python. \n" \

    print(name)
    print(description)