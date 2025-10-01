"""Cross-platform input handling for the game"""

import sys

# Platform-specific imports
if sys.platform == 'win32':
    import msvcrt
else:
    import select


def get_input():
    """Non-blocking input check that works on Windows and Unix"""
    if sys.platform == 'win32':
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8', errors='ignore').lower()
    else:
        # For Unix, would need termios setup
        if select.select([sys.stdin], [], [], 0)[0]:
            return sys.stdin.read(1).lower()
    return None


def wait_for_key():
    """Wait for any key press to continue"""
    if sys.platform == 'win32':
        msvcrt.getch()
    else:
        input()