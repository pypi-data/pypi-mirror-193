from colorama import Fore, Style


def output(color: str, url: str) -> None:

    # Blue means the url has already been recorded
    if color == 'blue':
        print(Fore.BLUE + f"{url}" + Fore.RESET)
        Style.RESET_ALL

    # Cyan means that the file name alrady exists in the local directory
    if color == 'cyan':
        print(Fore.CYAN + f"{url}" + Fore.RESET)
        Style.RESET_ALL

    # Green means the file is downloading
    if color == 'green':
        print(Fore.GREEN + f"{url}" + Fore.RESET)
        Style.RESET_ALL

    # Red means there was an error with the download. Check logs
    if color == 'red':
        print(Fore.RED + f"{url}" + Fore.RESET)
        Style.RESET_ALL
