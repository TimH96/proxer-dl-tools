"""
    lib/script_utils.py

    lib for utility functions for cl script execution
"""

from sys import exit


def _script_exit(reason: str) -> None:
    """Wrapper for script exit on error"""
    print(f'exit with error: {reason}')
    exit()
