"""Claude file deletion logic"""

import os
import shutil
import json
import re
from pathlib import Path


# Files to preserve in ~/.claude/ during home folder cleaning
HOME_PRESERVE = ['.credentials.json', 'settings.json']


def clean_claude_data(mode='home'):
    """Delete Claude data based on mode.

    mode='home': Clean ~/.claude.json and ~/.claude/ (preserves credentials and settings)
    mode='project': Clean .claude/ in the current working directory
    mode='both': Clean both

    Returns (deleted_files, errors) tuple.
    """
    deleted_files = []
    errors = []

    if mode in ('home', 'both'):
        files, errs = _clean_home()
        deleted_files.extend(files)
        errors.extend(errs)

    if mode in ('project', 'both'):
        files, errs = _clean_project()
        deleted_files.extend(files)
        errors.extend(errs)

    return deleted_files, errors


def _clean_home():
    """Clean ~/.claude.json and ~/.claude/ in the home directory.
    Returns (deleted_files, errors) tuple."""
    deleted_files = []
    errors = []
    home = Path.home()

    try:
        # Handle .claude.json with surgical precision
        claude_json_path = home / '.claude.json'
        if claude_json_path.exists():
            try:
                with open(claude_json_path, 'r') as f:
                    content = f.read()

                try:
                    data = json.loads(content)

                    # Sections to clean — updated March 2026
                    sections_to_clean = [
                        # Legacy sections (may or may not exist)
                        'cachedChangelog',
                        'cachedStatsigGates',
                        'cachedMobilePrivacySettings',
                        'cachedFeatureGates',
                        'cachedAnnouncementModals',
                        'activeModels',
                        'cachedSettings',
                        # Current sections (as of March 2026)
                        'projects',
                        'tipsHistory',
                        'cachedGrowthBookFeatures',
                        'cachedDynamicConfigs',
                        'groveConfigCache',
                        'clientDataCache',
                        'passesEligibilityCache',
                        'feedbackSurveyState',
                        'githubRepoPaths',
                        'hasShownOpus46Notice',
                    ]

                    for section in sections_to_clean:
                        if section in data:
                            if isinstance(data[section], dict):
                                data[section] = {}
                            elif isinstance(data[section], list):
                                data[section] = []
                            elif isinstance(data[section], str):
                                data[section] = ""

                    # Remove tracking fields
                    for field in ['userID', 'changelogLastFetched',
                                  'cachedExtraUsageDisabledReason',
                                  'claudeCodeFirstTokenDate']:
                        data.pop(field, None)

                    # Replace PII with Nedry's famous line
                    if 'oauthAccount' in data:
                        for key in ['email', 'emailAddress']:
                            if key in data['oauthAccount']:
                                data['oauthAccount'][key] = "ah.ah.ah@you-didnt-say-the-magic-word.jp"
                        for key in ['displayName', 'organizationName']:
                            if key in data['oauthAccount']:
                                data['oauthAccount'][key] = "Ah ah ah! You didn't say the magic word!"

                    with open(claude_json_path, 'w') as f:
                        json.dump(data, f, indent=2)

                    deleted_files.append("~/.claude.json (cleaned)")

                except json.JSONDecodeError:
                    # Fallback to regex for malformed JSON
                    for field in ['projects', 'cachedChangelog', 'cachedStatsigGates',
                                  'cachedMobilePrivacySettings', 'cachedFeatureGates',
                                  'cachedAnnouncementModals', 'tipsHistory',
                                  'cachedGrowthBookFeatures', 'cachedDynamicConfigs',
                                  'githubRepoPaths']:
                        content = re.sub(
                            rf'("{field}"\s*:\s*\{{)[^}}]*(\}})',
                            r'\1\2', content, flags=re.DOTALL
                        )
                        content = re.sub(
                            rf'("{field}"\s*:\s*\[)[^\]]*(\])',
                            r'\1\2', content, flags=re.DOTALL
                        )

                    with open(claude_json_path, 'w') as f:
                        f.write(content)

                    deleted_files.append("~/.claude.json (cleaned with regex)")

            except Exception as e:
                errors.append(f"Failed to clean ~/.claude.json: {e}")

        # Delete backup files
        for json_file in ['.claude.json.json', '.claude.json.backup']:
            file_path = home / json_file
            if file_path.exists():
                try:
                    os.remove(file_path)
                    deleted_files.append(f"~/{json_file}")
                except Exception as e:
                    errors.append(f"Failed to delete ~/{json_file}: {e}")

        # Delete .claude folder but preserve credentials and settings
        claude_folder = home / '.claude'
        if claude_folder.exists():
            try:
                # Back up files we want to preserve
                preserved = {}
                for filename in HOME_PRESERVE:
                    filepath = claude_folder / filename
                    if filepath.exists():
                        try:
                            with open(filepath, 'r') as f:
                                preserved[filename] = f.read()
                        except Exception:
                            pass

                # Enumerate all files for the credits scroll
                def enumerate_files():
                    for root, dirs, files in os.walk(claude_folder):
                        rel_root = Path(root).relative_to(home)
                        for file in files:
                            file_path = f"~/{rel_root}/{file}"
                            if file in HOME_PRESERVE:
                                yield f"{file_path} (preserved)"
                            else:
                                yield file_path
                        for dir_name in dirs:
                            yield f"~/{rel_root}/{dir_name}/"

                for file_path in enumerate_files():
                    deleted_files.append(file_path)

                # Nuke it
                shutil.rmtree(claude_folder)

                # Restore preserved files
                if preserved:
                    try:
                        claude_folder.mkdir(parents=True, exist_ok=True)
                        for filename, content in preserved.items():
                            filepath = claude_folder / filename
                            with open(filepath, 'w') as f:
                                f.write(content)
                            os.chmod(filepath, 0o600)
                    except Exception:
                        pass

                deleted_files.append("~/.claude/ (nuked, credentials + settings preserved)")
            except PermissionError:
                errors.append("~/.claude/ is locked by Claude Code")
            except Exception as e:
                errors.append(f"~/.claude/ failed: {e}")

    except Exception as e:
        errors.append(f"Home folder cleanup failed: {e}")

    return deleted_files, errors


def _clean_project():
    """Clean .claude/ in the current working directory.
    Returns (deleted_files, errors) tuple."""
    deleted_files = []
    errors = []
    cwd = Path.cwd()
    claude_folder = cwd / '.claude'

    if not claude_folder.exists():
        return deleted_files, errors

    try:
        # Enumerate files for credits
        for root, dirs, files in os.walk(claude_folder):
            rel_root = Path(root).relative_to(cwd)
            for file in files:
                deleted_files.append(f"./{rel_root}/{file}")
            for dir_name in dirs:
                deleted_files.append(f"./{rel_root}/{dir_name}/")

        # Nuke the project .claude folder
        shutil.rmtree(claude_folder)
        deleted_files.append(f".claude/ (deleted from {cwd.name})")

    except PermissionError:
        errors.append(f"./{cwd.name}/.claude/ is locked by Claude Code")
    except Exception as e:
        errors.append(f"./{cwd.name}/.claude/ failed: {e}")

    return deleted_files, errors


def detect_project_claude():
    """Check if there's a .claude/ folder in the current directory"""
    return (Path.cwd() / '.claude').exists()
