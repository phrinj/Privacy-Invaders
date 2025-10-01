"""Claude file deletion logic"""

import os
import shutil
from pathlib import Path


def clean_claude_data():
    """NUCLEAR OPTION: Complete deletion of all Claude tracking files"""
    deleted_files = []
    home = Path.home()

    try:
        # Delete .claude.json
        claude_json = home / '.claude.json'
        if claude_json.exists():
            try:
                os.remove(claude_json)
                deleted_files.append(str(claude_json))
            except Exception:
                pass

        # Delete .claude.json.json (the hilarious double extension)
        claude_json_json = home / '.claude.json.json'
        if claude_json_json.exists():
            try:
                os.remove(claude_json_json)
                deleted_files.append(str(claude_json_json))
            except Exception:
                pass

        # Delete .claude.json.backup
        claude_json_backup = home / '.claude.json.backup'
        if claude_json_backup.exists():
            try:
                os.remove(claude_json_backup)
                deleted_files.append(str(claude_json_backup))
            except Exception:
                pass

        # Count files in .claude folder before deletion
        claude_folder = home / '.claude'
        if claude_folder.exists():
            try:
                # Recursively find all files in the folder
                for root, dirs, files in os.walk(claude_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Shorten path for display
                        display_path = file_path.replace(str(home), "~")
                        deleted_files.append(display_path)

                # Now delete the entire folder
                shutil.rmtree(claude_folder)
            except Exception:
                pass

    except Exception:
        pass

    return deleted_files