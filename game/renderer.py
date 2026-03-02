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

        # Enable ANSI on Windows
        if sys.platform == 'win32':
            try:
                import colorama
                colorama.init()
            except ImportError:
                # Enable VT100 processing on Windows 10+
                try:
                    import ctypes
                    kernel32 = ctypes.windll.kernel32
                    kernel32.SetConsoleMode(
                        kernel32.GetStdHandle(-11), 7
                    )
                except Exception:
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

        if not self.border_drawn or force_full_redraw:
            self.clear_screen()
            self.hide_cursor()
            # Top border
            print("+" + "-" * self.width + "+")
            # Game area
            for row in buffer:
                print("|" + ''.join(row) + "|")
            # Bottom border
            print("+" + "-" * self.width + "+")
            # Status line
            print(f"  {status_text:<{self.width - 2}}")
            # Instructions (only when idle)
            if not status_text:
                print("\n  Press any key to launch nuke")
            self.border_drawn = True
            self.last_status = status_text
        else:
            # Incremental update — just redraw the interior rows
            for i, row in enumerate(buffer):
                # Row i+2 because line 1 is the top border
                print(f"\033[{i + 2};1H|" + ''.join(row) + "|", end="")

            # Update status if changed
            if status_text != self.last_status:
                status_row = self.height + 3
                print(f"\033[{status_row};1H  {status_text:<{self.width - 2}}", end="")
                self.last_status = status_text

            # Park cursor below the frame
            print(f"\033[{self.height + 5};1H", end="", flush=True)

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

        # Draw ship (each line is 10 chars wide, centered on ship_x)
        ship_y = self.height - 5
        for i, line in enumerate(ship_frame):
            half = len(line) // 2
            for j, char in enumerate(line):
                x = ship_x - half + j
                if 0 <= x < self.width and char != ' ':
                    if 0 <= ship_y + i < self.height:
                        buffer[ship_y + i][x] = char

        return buffer
