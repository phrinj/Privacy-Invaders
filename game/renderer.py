"""Game rendering engine with smooth updates"""

import os
import sys


class Renderer:
    """Handles all game rendering with minimal flicker"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.last_status = ""
        self.border_drawn = False

        # Initialize colorama on Windows
        if sys.platform == 'win32':
            try:
                import colorama
                colorama.init()
            except ImportError:
                pass

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if sys.platform == 'win32' else 'clear')

    def hide_cursor(self):
        """Hide the terminal cursor"""
        print('\033[?25l', end='', flush=True)

    def show_cursor(self):
        """Show the terminal cursor"""
        print('\033[?25h', end='', flush=True)

    def render(self, buffer, violations_count=0, status_text="", force_full_redraw=False):
        """Render buffer to screen with minimal flicker"""

        # Only clear and redraw border if needed
        if not self.border_drawn or force_full_redraw:
            self.clear_screen()
            self.hide_cursor()  # Hide cursor for cleaner game display
            print("╔" + "═" * self.width + "╗")
            for row in buffer:
                print("║" + ''.join(row) + "║")
            print("╚" + "═" * self.width + "╝")
            # print(f"\n  Privacy Violations Destroyed: {violations_count}")  # Removed redundant text
            # print(f"  {status_text:<60}")  # Removed all text below game area
            print("\n  Press any key to launch nuke or Q to Quit")
            # print("  NOTE: You'll need to re-login each Claude terminal session")  # Removed all text below game area
            self.border_drawn = True
            self.last_status = status_text
        else:
            # Use ANSI codes to just update the interior
            for i, row in enumerate(buffer):
                print(f"\033[{i+2};1H║" + ''.join(row) + "║", end="")

            # Update status if changed
            # Removed all text below game area
            # if status_text != self.last_status:
            #     print(f"\033[{self.height + 4};3H  {status_text:<60}", end="")
            #     self.last_status = status_text

            # Update violations count - Removed redundant text
            # print(f"\033[{self.height + 3};3HPrivacy Violations Destroyed: {violations_count}  ", end="")

            # Move cursor to safe position
            print(f"\033[{self.height + 5};1H", end="", flush=True)  # Adjusted position for text below

    def draw_frame(self, buffer, stars, ship_frame, ship_x):
        """Draw a frame to the buffer"""
        # Clear buffer
        for y in range(self.height):
            buffer[y] = [' '] * self.width

        # Draw stars
        for star in stars:
            y = int(star['y'])
            x = int(star['x'])
            if 0 <= y < self.height and 0 <= x < self.width:
                buffer[y][x] = star['char']

        # Draw ship
        ship_y = self.height - 4
        for i, line in enumerate(ship_frame):
            for j, char in enumerate(line):
                x = ship_x - 4 + j
                if 0 <= x < self.width and char != ' ':
                    buffer[ship_y + i][x] = char

        return buffer