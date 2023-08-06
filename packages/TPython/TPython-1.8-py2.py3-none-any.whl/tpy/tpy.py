# Import libs
import ast
import json
import os
import sys
import traceback
import urllib.error
import urllib.request
from threading import Thread
from timeit import timeit

import tpy.config

try:
    from colorama import Fore, init
    init(autoreset=True)
except ModuleNotFoundError:
    sys.exit('Module not found: colorama')

# Vars
cell_number: int = 1
err: bool = False
ind: bool = False
namespace: dict = {}
VERSION: str = '1.8'

# Exception prettifier
def exc() -> None:
    name, value = sys.exc_info()[0:2] # type: ignore
    name: str = name.__name__ # type: ignore
    top_bar = "----------------------------------------------------------------------" if os.get_terminal_size().columns > 70 else "-"*os.get_terminal_size().columns
    if name == 'SyntaxError':
        line: str = value.args[1][3] # type: ignore
        err_highlight: str = ' '*(value.offset - 1) + ('^'*(value.end_offset - value.offset) if value.end_offset - value.offset != 0 else '^') # type: ignore
        value: str = value.args[0] # type: ignore
        if line.endswith('\n'):
            line = line.removesuffix('\n')
        exc: str = f'{Fore.LIGHTGREEN_EX}{top_bar}\n{Fore.LIGHTRED_EX}{name} {Fore.LIGHTGREEN_EX}in Cell {Fore.GREEN}{cell_number}\n{Fore.RESET}{line}\n{err_highlight}\n\n{Fore.LIGHTRED_EX}{name}{Fore.RESET}: {value}'
    else:
        exc: str = f'{Fore.LIGHTGREEN_EX}{top_bar}\n{Fore.LIGHTRED_EX}{name} {Fore.LIGHTGREEN_EX}in Cell {Fore.GREEN}{cell_number}{(len(top_bar)-len(name)-len(str(cell_number))-42)*" "}Traceback (most recent call last)\n\n{Fore.LIGHTRED_EX}{name}{Fore.RESET}: {value}'
    print(exc)

# Update notifier
if tpy.config.CONFIG['config']['notify_updates']:
    def update_checker() -> None:
        try:
            response = urllib.request.urlopen('https://pypi.org/pypi/TPython/json')
            pypi_json = json.load(response)
            pypi_version = pypi_json['info']['version']
            if pypi_version != VERSION:
                print(f'{tpy.config.CONFIG["colors"]["update"]["text_color"]}Newer version of TPython is available: {tpy.config.CONFIG["colors"]["update"]["version_color"]}{pypi_version}')
        except urllib.error.URLError:
            pass
        return
    Thread(target=update_checker).run()

# Entry point
def main() -> None:
    global cell_number, err, ind

    # Exit function
    def ext(crash_m: str = '', crash: bool = False) -> None:
        columns = os.get_terminal_size().columns
        success_m = 'Process Completed Successfully'
        if crash:
            if tpy.config.CONFIG['config']['crash_msg']:
                msg = crash_m
                for i in range((columns-len(crash_m))//2):
                    msg = f'{tpy.config.CONFIG["colors"]["exit"]["crash"]["padding_color"]}-{tpy.config.CONFIG["colors"]["exit"]["crash"]["text_color"]}{msg}{tpy.config.CONFIG["colors"]["exit"]["crash"]["padding_color"]}-'
                sys.exit(f'{msg}')
        else:
            if tpy.config.CONFIG['config']['exit_msg']:
                msg = success_m
                for i in range((columns-len(success_m))//2):
                    msg = f'{tpy.config.CONFIG["colors"]["exit"]["success"]["padding_color"]}-{tpy.config.CONFIG["colors"]["exit"]["success"]["text_color"]}{msg}{tpy.config.CONFIG["colors"]["exit"]["success"]["padding_color"]}-'
                print(f'{msg}')
            sys.exit()

    try:
        # Execute function
        def execute(code: str, timeit_b: bool = False) -> None:
            global err, cell_number
            run = False
            if timeit_b:
                try:
                    time = timeit(code, globals=namespace, number=1)
                    print(f'{tpy.config.TNP_COLORS["time_text"]["text_color"]}Execution time: {tpy.config.TNP_COLORS["time_text"]["time_color"]}{time}')
                except Exception:
                    exc()
                    err = True
            else:
                try:
                    eval_return = eval(code, namespace)
                    if eval_return != None:
                        print(repr(eval_return))
                    err = False
                except:
                    run = True
                if run:
                    try:
                        exec(code, namespace)
                        err = False
                    except Exception:
                        exc()
                        err = True
            cell_number += 1

        # Welcome message
        if tpy.config.CONFIG['config']['welcome_msg']:
            columns = os.get_terminal_size().columns
            msg = 'TPython'
            columns -= 7
            for i in range(columns//2):
                msg = f'{tpy.config.CONFIG["colors"]["welcome"]["padding_color"]}-{tpy.config.CONFIG["colors"]["welcome"]["text_color"]}{msg}{tpy.config.CONFIG["colors"]["welcome"]["padding_color"]}-'
            print(f'{msg}')

        # Input
        while True:
            try:
                indent = False
                indent_t = False
                inp = input(f'{tpy.config.INP_COLORS["sq_brackets"]}[{tpy.config.INP_COLORS["number"]["error" if err else "normal"]}{cell_number}{tpy.config.INP_COLORS["sq_brackets"]}]{tpy.config.INP_COLORS["dash"]}-{tpy.config.INP_COLORS["arrow"]}> {Fore.LIGHTWHITE_EX}')
                if not (inp.isspace() or inp == ''):
                    inp = inp.strip()
                    # Exit command
                    if inp in ('exit', 'quit', 'close'):
                        ext()
                    elif inp in ('clear', 'cls') and not ('clear' in namespace or 'cls' in namespace):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        err = False
                    # Version command
                    elif inp == 'version' and not 'version' in namespace:
                        print(f'{Fore.LIGHTCYAN_EX}{VERSION} {Fore.LIGHTGREEN_EX}from {Fore.LIGHTCYAN_EX}Python {Fore.LIGHTCYAN_EX}{sys.version_info.major}.{sys.version_info.minor}')
                    # TimeIt command
                    elif inp == 'timeit' and not 'timeit' in namespace:
                        while True:
                            tnp = input(f'{tpy.config.TNP_COLORS["sq_brackets"]}[{tpy.config.TNP_COLORS["text_color"]}TimeIt{tpy.config.TNP_COLORS["sq_brackets"]}]{tpy.config.TNP_COLORS["dash"]}-{tpy.config.TNP_COLORS["arrow"]}> {Fore.LIGHTWHITE_EX}').strip()
                            # Check for SyntaxError, if there is it will give indent promote
                            try:
                                ast.parse(inp)
                            except SyntaxError:
                                indent_t = True
                            if indent_t:
                                # Indenting
                                while True:
                                    indent = input(f'{tpy.config.TNP_COLORS_INDENT["sq_brackets"]}[{tpy.config.TNP_COLORS_INDENT["text_replace"]}------{tpy.config.TNP_COLORS_INDENT["sq_brackets"]}]{tpy.config.TNP_COLORS_INDENT["dash"]}-{tpy.config.TNP_COLORS_INDENT["arrow"]}> {Fore.LIGHTWHITE_EX}')
                                    if indent.strip() == '':
                                        if not ind:
                                            ind = True
                                        else:
                                            break
                                    else:
                                        tnp += f'\n{indent}'
                                execute(tnp, True)
                                ind = False
                                break
                            else:
                                execute(tnp, True)
                                break
                    else:
                        # Check for SyntaxError, if there is it will give indent promote
                        try:
                            ast.parse(inp)
                        except SyntaxError:
                            indent = True
                        if indent:
                            # Indenting
                            while True:
                                indent = input(f'{tpy.config.INP_COLORS_INDENT["sq_brackets"]}[{tpy.config.INP_COLORS_INDENT["number_replace"]}{":"*len(str(cell_number))}{tpy.config.INP_COLORS_INDENT["sq_brackets"]}]{tpy.config.INP_COLORS_INDENT["dash"]}-{tpy.config.INP_COLORS_INDENT["arrow"]}> {Fore.LIGHTWHITE_EX}')
                                if indent.strip() == '':
                                    if not ind:
                                        ind = True
                                    else:
                                        break
                                else:
                                    inp += f'\n{indent}'
                            execute(inp)
                            ind = False
                        else:
                            execute(inp)
            except KeyboardInterrupt:
                print(f'\n{Fore.LIGHTYELLOW_EX}KeyboardInterrupt')
                err = True
    except EOFError:
        sys.exit(f'{Fore.LIGHTYELLOW_EX}EOFError')
    except Exception as e:
        print(traceback.format_exc())
        ext(e.__name__, True) # type: ignore