from re import search
from time import sleep
from sys import platform
from functools import wraps
from typing import Callable
from datetime import datetime
from os import system, environ
from contextlib import suppress

from colorama import Fore, Style

from .exceptions import BadGateway, Forbidden, ServiceUnavailable

def check_debugger() -> bool:
    """
    Checks if the program is being run in a debugger.
    """
    with suppress(Exception):
        return any([
            search("vscode", environ.get("TERM_PROGRAM")),
            search("pycharm", environ.get("TERM_PROGRAM")),
            is_repl(), is_android()
            ])

def retry(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        failed = 0
        while failed <= 2:
            try:
                return func(*args, **kwargs)
            except (
            ServiceUnavailable,
            Forbidden, BadGateway
            ):
                failed += 1
                print_retry() if check_debugger() else None
        return func(*args, **kwargs)
    return wrapper

def print_retry():
    print(f"{Fore.RED}[!] {Fore.YELLOW}An error occurred while trying to connect to the server.{Style.RESET_ALL}")
    print(f"{Fore.RED}[!] {Fore.YELLOW}Waiting 1 second before trying again.{Style.RESET_ALL}")
    sleep(1)
    
def orjson_exists() -> bool:
    """
    Checks if orjson is installed. If it isn't, it will install it.
    """
    if is_android(): return False

    try:
        from orjson import dumps as dumps
        return True
    except ImportError:
        system("pip install orjson")
        system("cls") if platform == "win32" else system("clear")
        return True
    
def is_android() -> bool:
    """
    Checks if the program is running on an Android device.
    """
    return any(key in environ for key in ("ANDROID_ROOT", "ANDROID_DATA"))

def is_repl() -> bool:
    """
    Checks if the program is running on a repl.it instance.
    """
    return any(key for key in environ if key.lower().startswith("repl"))

def notify() -> None:
    """
    Notifies the user that the bot is online.
    """
    print(f"\n{Fore.MAGENTA}[PYMINO] | {Fore.GREEN}BOT STATUS: {Fore.YELLOW}ONLINE | {Style.RESET_ALL}{datetime.now().strftime('%H:%M:%S')}\n")
    print(f"{Fore.RED}[!] {Fore.YELLOW}If you see this message, you can safely ignore it. The bot is still running and will continue to run until you stop it.{Style.RESET_ALL}\n")