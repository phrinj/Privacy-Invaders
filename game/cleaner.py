"""Claude file deletion logic"""

import os
import shutil
import json
import re
from pathlib import Path


def clean_claude_data():
    """Delete all Claude data except OAuth tokens to preserve authentication"""
    deleted_files = []
    home = Path.home()

    try:
        # Handle .claude.json with surgical precision
        claude_json_path = home / '.claude.json'
        if claude_json_path.exists():
            try:
                # Read the file
                with open(claude_json_path, 'r') as f:
                    content = f.read()

                cleaned = False

                try:
                    # Try JSON parsing approach first
                    data = json.loads(content)

                    # Empty these sections while preserving structure
                    sections_to_clean = [
                        'cachedChangelog',
                        'projects',
                        'cachedStatsigGates',
                        'cachedMobilePrivacySettings',
                        'cachedFeatureGates',
                        'cachedAnnouncementModals',
                        'activeModels',
                        'cachedSettings'
                    ]

                    for section in sections_to_clean:
                        if section in data:
                            if isinstance(data[section], dict):
                                data[section] = {}
                            elif isinstance(data[section], list):
                                data[section] = []
                            elif isinstance(data[section], str):
                                data[section] = ""

                    # Replace PII with Nedry's famous line
                    if 'oauthAccount' in data:
                        if 'email' in data['oauthAccount']:
                            data['oauthAccount']['email'] = "ah.ah.ah@you-didnt-say-the-magic-word.jp"
                        if 'emailAddress' in data['oauthAccount']:
                            data['oauthAccount']['emailAddress'] = "ah.ah.ah@you-didnt-say-the-magic-word.jp"
                        if 'displayName' in data['oauthAccount']:
                            data['oauthAccount']['displayName'] = "Ah ah ah! You didn't say the magic word!"
                        if 'organizationName' in data['oauthAccount']:
                            data['oauthAccount']['organizationName'] = "Ah ah ah! You didn't say the magic word!"

                    # Write back preserving formatting as much as possible
                    with open(claude_json_path, 'w') as f:
                        json.dump(data, f, indent=2)

                    deleted_files.append("~/.claude.json (cleaned)")
                    cleaned = True

                except json.JSONDecodeError:
                    # Fallback to regex approach for malformed JSON
                    # Clean projects array content
                    content = re.sub(
                        r'("projects"\s*:\s*\[)[^\]]*(\])',
                        r'\1\2',
                        content,
                        flags=re.DOTALL
                    )

                    # Clean cachedChangelog object content
                    content = re.sub(
                        r'("cachedChangelog"\s*:\s*\{)[^\}]*(\})',
                        r'\1\2',
                        content,
                        flags=re.DOTALL
                    )

                    # Clean other cached sections
                    for field in ['cachedStatsigGates', 'cachedMobilePrivacySettings',
                                 'cachedFeatureGates', 'cachedAnnouncementModals']:
                        # Handle as object
                        content = re.sub(
                            rf'("{field}"\s*:\s*\{{)[^}}]*(\}})',
                            r'\1\2',
                            content,
                            flags=re.DOTALL
                        )
                        # Handle as array
                        content = re.sub(
                            rf'("{field}"\s*:\s*\[)[^\]]*(\])',
                            r'\1\2',
                            content,
                            flags=re.DOTALL
                        )

                    with open(claude_json_path, 'w') as f:
                        f.write(content)

                    deleted_files.append("~/.claude.json (cleaned with regex)")
                    cleaned = True

            except Exception as e:
                # If we can't clean it surgically, skip it to avoid logout
                pass

        # Delete backup files
        for json_file in ['.claude.json.json', '.claude.json.backup']:
            file_path = home / json_file
            if file_path.exists():
                try:
                    os.remove(file_path)
                    deleted_files.append(f"~/{json_file}")
                except Exception:
                    pass

        # Delete entire .claude folder (confirmed safe)
        # But first enumerate ALL files for the meme-worthy endless scroll effect!
        claude_folder = home / '.claude'
        if claude_folder.exists():
            try:
                # Use generator for privacy - don't build full list in memory
                def enumerate_files():
                    for root, dirs, files in os.walk(claude_folder):
                        # Convert to relative path from home for privacy
                        rel_root = Path(root).relative_to(home)
                        for file in files:
                            yield f"~/{rel_root}/{file}"
                        # Also show directories being deleted
                        for dir_name in dirs:
                            yield f"~/{rel_root}/{dir_name}/"

                # Collect files but immediately clear references for privacy
                for file_path in enumerate_files():
                    deleted_files.append(file_path)

                # Actually delete the folder
                shutil.rmtree(claude_folder)

                # Add summary at the end
                deleted_files.append("~/.claude/ (entire directory tree deleted)")
            except Exception:
                pass

    except Exception:
        pass

    return deleted_files
