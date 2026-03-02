"""Game animations: nuke launch, explosions, and summary"""

import time
import random
from .content import PLANET_LINES, EXPLOSION_FRAMES, ONE_LINERS


def animate_nuke(game, renderer):
    """Animate the nuke launch sequence"""
    buffer = [[' '] * game.width for _ in range(game.height)]

    # Center planet horizontally
    planet_w = len(PLANET_LINES[0])
    planet_x = (game.width - planet_w) // 2

    for i, line in enumerate(PLANET_LINES):
        for j, char in enumerate(line):
            if planet_x + j < game.width and char != ' ':
                buffer[2 + i][planet_x + j] = char

    # Launch nuke upward
    nuke_x = game.width // 2
    nuke_y = game.height - 5
    first_frame = True

    while nuke_y > 6:
        temp_buffer = [row[:] for row in buffer]

        # Draw stars
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

        # Draw nuke missile
        if 0 <= nuke_y < game.height:
            temp_buffer[nuke_y][nuke_x] = '^'
        if 0 <= nuke_y + 1 < game.height:
            temp_buffer[nuke_y + 1][nuke_x] = '|'
        if 0 <= nuke_y + 2 < game.height:
            temp_buffer[nuke_y + 2][nuke_x] = '+'

        renderer.render(temp_buffer, game.violations_destroyed, "NUKE LAUNCHED!",
                       force_full_redraw=first_frame)
        first_frame = False
        time.sleep(0.1)
        nuke_y -= 2

    # Explosion sequence
    for explosion in EXPLOSION_FRAMES:
        temp_buffer = [row[:] for row in buffer]

        exp_w = len(explosion[0])
        exp_x = (game.width - exp_w) // 2
        exp_y = 2

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

    return one_liner


def _wrap_text(text, max_width):
    """Wrap text to fit within max_width, breaking on spaces"""
    words = text.split(' ')
    lines = []
    current = ''
    for word in words:
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= max_width:
            current += ' ' + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def show_summary(game, renderer, deleted_files, one_liner, errors=None):
    """Show a brief summary of what was deleted"""
    count = len(deleted_files)

    # Calculate total size categories
    categories = {
        'conversations': 0,
        'debug': 0,
        'history': 0,
        'file-history': 0,
        'other': 0,
    }

    for f in deleted_files:
        if 'projects/' in f or 'projects\\' in f:
            categories['conversations'] += 1
        elif 'debug/' in f or 'debug\\' in f:
            categories['debug'] += 1
        elif 'history' in f:
            categories['history'] += 1
        elif 'file-history' in f:
            categories['file-history'] += 1
        else:
            categories['other'] += 1

    # Build summary lines — all centered individually
    buffer = [[' '] * game.width for _ in range(game.height)]

    # Stars in background
    for star in game.stars:
        y = int(star['y'])
        x = int(star['x'])
        if 0 <= y < game.height and 0 <= x < game.width:
            buffer[y][x] = star['char']

    lines = [
        f"FILES NUKED: {count}",
        "",
    ]

    # Build category block with consistent width so it centers as a unit
    cat_lines = []
    if categories['conversations']:
        cat_lines.append(f"Conversation logs: {categories['conversations']}")
    if categories['debug']:
        cat_lines.append(f"Debug files:       {categories['debug']}")
    if categories['history']:
        cat_lines.append(f"Prompt history:    {categories['history']}")
    if categories['file-history']:
        cat_lines.append(f"File snapshots:    {categories['file-history']}")
    if categories['other']:
        cat_lines.append(f"Other:             {categories['other']}")

    # Pad all category lines to same width so they align when centered
    if cat_lines:
        max_cat = max(len(l) for l in cat_lines)
        for cl in cat_lines:
            lines.append(cl.ljust(max_cat))

    if errors:
        lines.append("")
        lines.append("FAILED:")
        # Wrap long error messages to fit within the game area
        max_wrap = game.width - 8  # leave margin on both sides
        for err in errors:
            wrapped = _wrap_text(err, max_wrap)
            lines.extend(wrapped)
        lines.extend([
            "",
            "Close Claude Code and run again.",
        ])
    else:
        lines.extend([
            "",
            "Your privacy is restored.",
        ])

    # Center lines vertically
    start_y = max(0, (game.height - len(lines)) // 2)

    for i, line in enumerate(lines):
        y = start_y + i
        if 0 <= y < game.height:
            x_offset = max(0, (game.width - len(line)) // 2)
            for j, char in enumerate(line):
                if 0 <= x_offset + j < game.width:
                    buffer[y][x_offset + j] = char

    renderer.render(buffer, game.violations_destroyed, one_liner,
                   force_full_redraw=True)

    # Hold longer if there are errors so user can read them
    time.sleep(5 if errors else 3)
