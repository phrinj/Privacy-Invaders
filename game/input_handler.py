"""Cross-platform input handling for the game"""

import sys
import os

# Platform-specific imports
if sys.platform == 'win32':
    import msvcrt
else:
    import select
    import tty
    import termios
    import fcntl


def get_input():
    """Non-blocking input check that works on Windows and Unix"""
    if sys.platform == 'win32':
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8', errors='ignore').lower()
    else:
        # Unix/Linux - handle both terminal and non-terminal input
        try:
            import fcntl

            # Check if stdin is available for reading
            if select.select([sys.stdin], [], [], 0)[0]:
                # Try to read without blocking
                fd = sys.stdin.fileno()

                # Check if we're in a terminal
                if sys.stdin.isatty():
                    # Terminal mode - set up raw input
                    oldterm = termios.tcgetattr(fd)
                    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)

                    try:
                        # Set terminal to raw mode (no echo, immediate input)
                        newattr = termios.tcgetattr(fd)
                        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
                        termios.tcsetattr(fd, termios.TCSANOW, newattr)

                        # Set non-blocking
                        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

                        try:
                            c = sys.stdin.read(1)
                            if c:
                                return c.lower()
                        except IOError:
                            pass
                    finally:
                        # Restore terminal settings
                        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
                else:
                    # Not a terminal - just read normally
                    c = sys.stdin.read(1)
                    if c:
                        return c.lower()
        except Exception:
            # Fallback for any errors
            pass

    return None


def wait_for_key():
    """Wait for any key press to continue"""
    if sys.platform == 'win32':
        msvcrt.getch()
    else:
        input()