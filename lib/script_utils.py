"""
    lib/script_utils.py

    lib for utility functions for cl script execution
"""

from sys import exit


def script_exit(reason: str) -> None:
    """Wrapper for script exit on error"""
    print(f'exit with error: {reason}')
    exit()


def check_validity_token(token: str) -> list:
    """Processes token input and checks its validity, exits if invalid"""
    try:
        spl_token : list = token.split('=')
        if len(spl_token[0]) <= 0 or len(spl_token[1]) <= 0:
            raise Exception
        else:
            return spl_token
    except Exception:
        script_exit('auth token could not be parsed')


def check_validity_file(filepath: str) -> bool:
    """Checks if filepath can be written, exits if it can't"""
    try:
        with open(filepath, 'wb'):
            pass
    except Exception:
        script_exit(f'file {filepath} could not be opened')
