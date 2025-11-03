"""Game animations: nuke launch, explosions, and credits"""

import time
import random
from .content import PLANET_LINES, EXPLOSION_FRAMES, ONE_LINERS


def animate_nuke(game, renderer):
    """Animate the nuke launch sequence"""
    buffer = [[' '] * game.width for _ in range(game.height)]

    # Position planet
    planet_x = game.width // 2 - 7
    for i, line in enumerate(PLANET_LINES):
        for j, char in enumerate(line):
            if planet_x + j < game.width and char != ' ':
                buffer[2 + i][planet_x + j] = char

    # Launch nuke
    nuke_y = game.height - 5
    while nuke_y > 6:
        # Clear previous nuke position
        temp_buffer = [row[:] for row in buffer]

        # Draw stars in background
        for star in game.stars:
            y = int(star['y'])
            x = int(star['x'])
            if 0 <= y < game.height and 0 <= x < game.width:
                temp_buffer[y][x] = star['char']

        # Redraw planet
        for i, line in enumerate(PLANET_LINES):
            for j, char in enumerate(line):
                if planet_x + j < game.width and char != ' ':
                    temp_buffer[2 + i][planet_x + j] = char

        # Draw nuke
        if nuke_y < game.height:
            temp_buffer[nuke_y][game.width // 2] = '☢'
            if nuke_y + 1 < game.height:
                temp_buffer[nuke_y + 1][game.width // 2] = '║'
            if nuke_y + 2 < game.height:
                temp_buffer[nuke_y + 2][game.width // 2] = '╬'

        renderer.render(temp_buffer, game.violations_destroyed, "NUKE LAUNCHED!",
                       force_full_redraw=(nuke_y == game.height - 5))
        time.sleep(0.1)
        nuke_y -= 2

    # Explosion sequence
    for explosion in EXPLOSION_FRAMES:
        temp_buffer = [row[:] for row in buffer]

        # Draw explosion
        exp_y = 2
        exp_x = game.width // 2 - 5
        for i, line in enumerate(explosion):
            for j, char in enumerate(line):
                if 0 <= exp_y + i < game.height and 0 <= exp_x + j < game.width:
                    if char != ' ':
                        temp_buffer[exp_y + i][exp_x + j] = char

        renderer.render(temp_buffer, game.violations_destroyed, "BOOM!")
        time.sleep(0.15)

    # Show one-liner
    one_liner = random.choice(ONE_LINERS)
    renderer.render([[' '] * game.width for _ in range(game.height)],
                   game.violations_destroyed, one_liner)
    time.sleep(2)


def show_deletion_credits(game, renderer, deleted_files):
    """Show a scrolling credits sequence of deleted files"""
    import gc  # For explicit garbage collection

    buffer = [[' '] * game.width for _ in range(game.height)]

    # Prepare credits text
    credits = [
        "═══ PRIVACY VIOLATIONS DESTROYED ═══",
        "",
    ]

    for file in deleted_files:
        # Truncate long paths to fit in the box
        if len(file) > game.width - 4:
            file = "..." + file[-(game.width - 7):]
        credits.append(file)

    credits.extend([
        "",
        "═══════════════════════════════════",
        "",
        f"TOTAL FILES NUKED: {len(deleted_files)}",
        "",
        "Your privacy is restored!"
    ])

    # Clear the original list immediately for privacy
    del deleted_files
    gc.collect()  # Force garbage collection to clear memory

    # Scroll the credits
    credit_y = game.height
    frames_to_show = len(credits) + game.height + 5

    for frame in range(frames_to_show):
        # Clear buffer
        buffer = [[' '] * game.width for _ in range(game.height)]

        # Draw stars in background
        for star in game.stars:
            y = int(star['y'])
            x = int(star['x'])
            if 0 <= y < game.height and 0 <= x < game.width:
                buffer[y][x] = star['char']

        # Draw credits
        for i, line in enumerate(credits):
            y = credit_y + i
            if 0 <= y < game.height:
                # Center the text
                x_offset = (game.width - len(line)) // 2
                for j, char in enumerate(line):
                    if 0 <= x_offset + j < game.width:
                        buffer[y][x_offset + j] = char

        # Render - force redraw on first frame
        renderer.render(buffer, game.violations_destroyed, "DELETION COMPLETE",
                       force_full_redraw=(frame == 0))

        # Move credits up
        credit_y -= 1

        # Update stars
        game.update_stars()

        time.sleep(0.15)