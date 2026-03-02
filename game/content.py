"""Game content and assets"""

# One-liners for the nuke animation
ONE_LINERS = [
    "I came here to protect my privacy and chew bubble gum, and I'm all out of gum",
    "ULTRA KILL...ed a potential data breach",
    "Grandma's credit card number: SAFE!",
    "Claude won't remember this conversation... literally!",
    "Privacy invaders? More like privacy VAPORIZERS!",
    "Your secrets are safe from Claude's overeager logging",
    "Issue #2713: closed. Your data: also closed.",
    "1.4 GB of logs? Not anymore.",
]

# Ship frames for idle animation (ASCII-safe, consistent width)
SHIP_FRAMES = [
    ["    /\\    ",
     "   /  \\   ",
     "  /|==|\\  ",
     " / |  | \\ ",],
    ["    /\\    ",
     "   /  \\   ",
     "  /|==|\\  ",
     " / |><| \\ ",],
]

# Planet ASCII art for nuke target
PLANET_LINES = [
    "  .--------.  ",
    " /  CLAUDE  \\ ",
    " \\   DATA   / ",
    "  '--------'  ",
]

# Explosion animation frames (ASCII-safe)
EXPLOSION_FRAMES = [
    ["     *     ",
     "    ***    ",
     "   *****   ",
     "    ***    ",
     "     *     ",],
    ["    xxx    ",
     "  xxxxxxx  ",
     " xxxxxxxxx ",
     "  xxxxxxx  ",
     "    xxx    ",],
    ["    ...    ",
     "  .......  ",
     " ......... ",
     "  .......  ",
     "    ...    ",],
    ["           ",
     "    . .    ",
     "   . . .   ",
     "    . .    ",
     "           ",],
]

# Star characters for the starfield
STAR_CHARS = ['.', '*', '+', '`']

# Star speeds
STAR_SPEEDS = [0.3, 0.5, 0.7, 1.0]

# Game dimensions
GAME_WIDTH = 60
GAME_HEIGHT = 20
STAR_COUNT = 15

# Game over screen text
# Border: +---(48 dashes)---+  Each row: | + 48 chars + |
GAME_OVER_TEXT = (
    "\n"
    "  +------------------------------------------------+\n"
    "  |                MISSION COMPLETE                |\n"
    "  |    Total Violations Destroyed: {count:6d}          |\n"
    "  |                                                |\n"
    "  |          Your privacy remains intact!          |\n"
    "  |                                                |\n"
    "  |  Support: buymeacoffee.com/phrinj              |\n"
    "  |  Web:     phrinj.com                           |\n"
    "  +------------------------------------------------+\n"
)
