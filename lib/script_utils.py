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


def check_validity_episodes(episodes: str) -> list:
    """Processes episodes input and checks its validity, exits if invalid"""
    try:
        spl_ep : list = list(map(int, episodes.split('-')))
        if len(spl_ep) != 2:
            raise Exception
        if spl_ep[0] > spl_ep[1]:
            script_exit('start larger than end episode')
        return spl_ep
    except Exception:
        script_exit('episodes input could not be processed')
