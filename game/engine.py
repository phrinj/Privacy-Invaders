"""Core game engine"""

import time
import random
from pathlib import Path

from .content import (
    GAME_WIDTH, GAME_HEIGHT, STAR_COUNT,
    STAR_CHARS, STAR_SPEEDS, SHIP_FRAMES,
    GAME_OVER_TEXT
)
from .renderer import Renderer
from .input_handler import get_input
from .cleaner import clean_claude_data
from .animations import animate_nuke, show_deletion_credits


class PrivacyInvaders:
    """Main game engine class"""

    def __init__(self):
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.ship_x = self.width // 2
        self.stars = []
        self.frame = 0
        self.violations_destroyed = 0
        self.running = True
        self.home = Path.home()
        self.ship_frames = SHIP_FRAMES

        # Initialize renderer
        self.renderer = Renderer(self.width, self.height)

        # Initialize starfield
        for _ in range(STAR_COUNT):
            self.stars.append({
                'x': random.randint(0, self.width - 1),
                'y': random.randint(0, self.height - 5),
                'char': random.choice(STAR_CHARS),
                'speed': random.choice(STAR_SPEEDS)
            })

    def update_stars(self):
        """Move stars down slowly"""
        for star in self.stars:
            star['y'] += star['speed']
            if star['y'] >= self.height - 4:
                star['y'] = 0
                star['x'] = random.randint(0, self.width - 1)

    def run(self):
        """Main game loop"""
        while self.running:
            # Draw idle animation
            buffer = [[' '] * self.width for _ in range(self.height)]
            ship_frame = self.ship_frames[self.frame % 2]
            buffer = self.renderer.draw_frame(buffer, self.stars, ship_frame, self.ship_x)

            # Force full redraw on first frame
            force_redraw = (self.frame == 0)
            self.renderer.render(buffer, self.violations_destroyed,
                               "",  # Removed all text below game area
                               force_full_redraw=force_redraw)

            # Update animation
            self.update_stars()
            self.frame += 1

            # Check for input
            key = get_input()
            if key is not None:  # Any key launches nuke
                # Launch nuke and get the one-liner!
                one_liner = animate_nuke(self, self.renderer)

                # Clean actual files (preserves OAuth token only)
                deleted_files = clean_claude_data()
                self.violations_destroyed += len(deleted_files)

                # Show scrolling credits of deleted files with the one-liner
                if deleted_files:
                    show_deletion_credits(self, self.renderer, deleted_files, one_liner)

                # Exit game after credits
                self.running = False

            # Low framerate for chill vibes
            time.sleep(0.5)

        self.renderer.show_cursor()  # Restore cursor visibility on exit
        self.renderer.clear_screen()
        print(GAME_OVER_TEXT.format(count=self.violations_destroyed))