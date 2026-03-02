"""Core game engine"""

import os
import time
import random
import sys
import subprocess
from pathlib import Path

from .content import (
    GAME_WIDTH, GAME_HEIGHT, STAR_COUNT,
    STAR_CHARS, STAR_SPEEDS, SHIP_FRAMES,
    GAME_OVER_TEXT
)
from .renderer import Renderer
from .input_handler import get_input, wait_for_key
from .cleaner import clean_claude_data, detect_project_claude
from .animations import animate_nuke, show_summary


def _is_claude_running():
    """Check if Claude Code is currently running"""
    try:
        if sys.platform == 'win32':
            result = subprocess.run(
                ['tasklist', '/FI', 'IMAGENAME eq claude.exe', '/NH'],
                capture_output=True, text=True, timeout=5
            )
            # tasklist returns "INFO: No tasks..." when not found
            if 'claude.exe' in result.stdout.lower() and 'no tasks' not in result.stdout.lower():
                return True
            # Also check for node processes running claude
            result = subprocess.run(
                ['powershell', '-NoProfile', '-Command',
                 "Get-Process node -ErrorAction SilentlyContinue | "
                 "Where-Object {$_.CommandLine -match 'claude'} | "
                 "Select-Object -First 1 | Format-List Id"],
                capture_output=True, text=True, timeout=5
            )
            if result.stdout.strip():
                return True
        else:
            result = subprocess.run(
                ['pgrep', '-f', 'claude'],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return True
    except Exception:
        pass
    return False


def _get_data_summary():
    """Scan for Claude data and return a summary of what exists"""
    home = Path.home()
    cwd = Path.cwd()
    info = {
        'has_home': False,
        'has_project': False,
        'home_size': 0,
        'home_files': 0,
        'project_size': 0,
        'project_files': 0,
        'has_email': False,
        'has_history': False,
        'has_conversations': False,
    }

    # Check home ~/.claude/
    claude_home = home / '.claude'
    claude_json = home / '.claude.json'

    if claude_home.exists():
        info['has_home'] = True
        for root, dirs, files in os.walk(claude_home):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    info['home_size'] += os.path.getsize(fp)
                    info['home_files'] += 1
                except OSError:
                    pass
        # Check for specific data types
        info['has_history'] = (claude_home / 'history.jsonl').exists()
        info['has_conversations'] = (claude_home / 'projects').exists()

    if claude_json.exists():
        info['has_home'] = True
        try:
            import json
            with open(claude_json, 'r') as f:
                data = json.loads(f.read())
            oauth = data.get('oauthAccount', {})
            if oauth.get('emailAddress') or oauth.get('email'):
                info['has_email'] = True
        except Exception:
            pass

    # Check project .claude/
    project_claude = cwd / '.claude'
    if project_claude.exists():
        info['has_project'] = True
        for root, dirs, files in os.walk(project_claude):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    info['project_size'] += os.path.getsize(fp)
                    info['project_files'] += 1
                except OSError:
                    pass

    return info


def _format_size(size_bytes):
    """Format bytes to human-readable string"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"


def show_splash(info):
    """Show splash screen with data summary and mode selection"""
    cwd_name = Path.cwd().name
    claude_running = _is_claude_running()

    print()
    print("  PRIVACY INVADERS")
    print("  ================")
    print()

    if claude_running:
        print("  !! WARNING: Claude Code is running !!")
        print("  Close all Claude Code sessions before nuking.")
        print("  Files locked by Claude Code will not be deleted.")
        print()

    # Home folder summary
    if info['has_home']:
        print(f"  Home folder (~/.claude/)")
        print(f"    {info['home_files']} files, {_format_size(info['home_size'])}")
        if info['has_email']:
            print(f"    Email address stored in plain text")
        if info['has_history']:
            print(f"    Prompt history (every command you've typed)")
        if info['has_conversations']:
            print(f"    Full conversation transcripts")
        print()
    else:
        print("  Home folder: no Claude data found")
        print()

    # Project folder summary
    if info['has_project']:
        print(f"  This folder (./{cwd_name}/.claude/)")
        print(f"    {info['project_files']} files, {_format_size(info['project_size'])}")
        print()
    else:
        print(f"  This folder (./{cwd_name}/): no Claude data found")
        print()

    # What will happen
    if info['has_home'] and info['has_project']:
        print("  What to nuke?")
        print()
        print("    [1] Home folder only")
        print("    [2] This folder only")
        print("    [3] Both")
        print()

        while True:
            try:
                print("  Choose (1/2/3): ", end='', flush=True)
                if sys.platform == 'win32':
                    import msvcrt
                    key = msvcrt.getch().decode('utf-8', errors='ignore')
                else:
                    key = input().strip()

                if key in ('1', '2', '3'):
                    print(key)
                    print()
                    if key == '1':
                        print("  Preserved: login credentials, settings")
                        mode = 'home'
                    elif key == '2':
                        mode = 'project'
                    else:
                        print("  Preserved: login credentials, settings")
                        mode = 'both'
                    print()
                    print("  Press any key to start the game...")
                    wait_for_key()
                    return mode
            except (KeyboardInterrupt, EOFError):
                print("\n")
                sys.exit(0)

    elif info['has_home']:
        print("  Target: home folder (~/.claude/ and ~/.claude.json)")
        print("  Action: delete all logs, history, and cached data")
        print("  Preserved: login credentials, settings")
        print()
        print("  Press any key to continue...")
        wait_for_key()
        return 'home'

    elif info['has_project']:
        cwd_name = Path.cwd().name
        print(f"  Target: ./{cwd_name}/.claude/")
        print("  Action: delete all Claude data in this project folder")
        print()
        print("  Press any key to continue...")
        wait_for_key()
        return 'project'

    else:
        print("  No Claude data found. Nothing to nuke.")
        sys.exit(0)


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
        self.mode = None

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
        # Scan and show splash
        info = _get_data_summary()
        self.mode = show_splash(info)

        while self.running:
            # Draw idle animation
            buffer = [[' '] * self.width for _ in range(self.height)]
            ship_frame = self.ship_frames[self.frame % 2]
            buffer = self.renderer.draw_frame(buffer, self.stars, ship_frame, self.ship_x)

            # Force full redraw on first frame
            force_redraw = (self.frame == 0)
            self.renderer.render(buffer, self.violations_destroyed,
                               "",
                               force_full_redraw=force_redraw)

            # Update animation
            self.update_stars()
            self.frame += 1

            # Check for input
            key = get_input()
            if key is not None:  # Any key launches nuke
                # Launch nuke and get the one-liner!
                one_liner = animate_nuke(self, self.renderer)

                # Clean actual files based on chosen mode
                deleted_files, errors = clean_claude_data(mode=self.mode)
                self.violations_destroyed += len(deleted_files)

                # Show summary of what was deleted (and any errors)
                if deleted_files or errors:
                    show_summary(self, self.renderer, deleted_files, one_liner, errors)

                # Exit game after credits
                self.running = False

            # Low framerate for chill vibes
            time.sleep(0.5)

        self.renderer.show_cursor()  # Restore cursor visibility on exit
        self.renderer.clear_screen()
        print(GAME_OVER_TEXT.format(count=self.violations_destroyed))
