#!/usr/bin/env python3
"""
Privacy Invaders: The Claude Data Destroyer Game
A zen space journey that occasionally nukes privacy violations

This is now just the entry point - all game logic is in the game/ module
"""

import sys
import os

# Fix Unicode output on Windows by setting console code page
if sys.platform == 'win32':
    os.system('chcp 65001 > nul 2>&1')  # Set UTF-8 code page silently

from game.engine import PrivacyInvaders


def main():
    """Main entry point for the game"""
    game = PrivacyInvaders()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\n  Privacy protection aborted by user.")


if __name__ == "__main__":
    main()