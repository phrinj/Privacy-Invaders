"""Game content and assets"""

# One-liners for the nuke animation
ONE_LINERS = [
    "I came here to protect my privacy and chew bubble gum, and I'm all out of gum",
    "It's a me, Mario! And Mario's pissed off about his privacy being violated!",
    "ULTRA KILL...ed a potential data breach",
    "Grandma's credit card number: SAFE!",
    "Claude won't remember this conversation... literally!",
    "Privacy invaders? More like privacy VAPORIZERS!",
    "Your secrets are safe from Claude's overeager logging"
]

# Ship frames for idle animation
SHIP_FRAMES = [
    ["  ╱▔▔╲  ", " ╱╲══╱╲ ", "╱  ╲╱  ╲", "▔▔╱  ╲▔▔"],
    ["  ╱▔▔╲  ", " ╱╲══╱╲ ", "╱  ><  ╲", "▔▔╱▔▔╲▔▔"],
]

# Planet ASCII art for nuke target
PLANET_LINES = [
    "   ╱▔▔▔▔▔▔╲   ",
    "  │ CLAUDE │  ",
    "  │  DATA  │  ",
    "   ╲▁▁▁▁▁▁╱   "
]

# Explosion animation frames
EXPLOSION_FRAMES = [
    ["     *     ", "    ***    ", "   *****   ", "    ***    ", "     *     "],
    ["    ╳╳╳    ", "  ╳╳╳╳╳╳╳  ", " ╳╳╳╳╳╳╳╳╳ ", "  ╳╳╳╳╳╳╳  ", "    ╳╳╳    "],
    ["   ░░░░░   ", " ░░░░░░░░░ ", "░░░░░░░░░░░", " ░░░░░░░░░ ", "   ░░░░░   "],
    ["    ···    ", "  ·······  ", " ········· ", "  ·······  ", "    ···    "],
]

# Star characters for the starfield
STAR_CHARS = ['.', '*', '°', '·']

# Star speeds
STAR_SPEEDS = [0.3, 0.5, 0.7, 1.0]

# Game dimensions
GAME_WIDTH = 60
GAME_HEIGHT = 20
STAR_COUNT = 15

# Welcome screen text
WELCOME_TEXT = """
  ╔════════════════════════════════════════╗
  ║         PRIVACY INVADERS               ║
  ║                                        ║
  ║     Press any key to continue          ║
  ╚════════════════════════════════════════╝"""

# Game over screen text
GAME_OVER_TEXT = """
  ╔══════════════════════════════════════════════════╗
  ║            MISSION COMPLETE                      ║
  ║     Total Violations Destroyed: {count:6d}           ║
  ║                                                  ║
  ║        Your privacy remains intact!              ║
  ║                                                  ║
  ║  Support this project:                           ║
  ║  BTC: 3B6SmUrUVFqWSBRdSbRkr4HoyA5D7S6WUj         ║
  ║                                                  ║
  ║  Follow @phrinj on:                              ║
  ║  YouTube | Instagram | Threads                   ║
  ║                                                  ║
  ║  phrinj.com                                      ║
  ╚══════════════════════════════════════════════════╝
"""