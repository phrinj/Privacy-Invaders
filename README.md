# Privacy Invaders

## The Space Shooter That Nukes Claude Code's Data Logging

A game that deletes Claude Code's unencrypted plaintext logs of your conversations, keystrokes, email, project paths, and session data from your machine.

![Game Preview](https://img.shields.io/badge/Genre-Space%20Shooter-brightgreen) ![Privacy](https://img.shields.io/badge/Privacy-Protected-blue) ![Fun](https://img.shields.io/badge/Fun%20Factor-Maximum-ff69b4)

## The Problem

Claude Code stores everything you type — including partial keystrokes, typos, and deleted text — in **unencrypted plaintext JSON files** on your machine. Your email, every project path you've ever opened, full conversation transcripts, shell command history, file edit snapshots, and debug logs all sit in `~/.claude/` and `~/.claude.json` with no encryption and no automatic cleanup.

**I reported this in June 2025 as [GitHub issue #2713](https://github.com/anthropics/claude-code/issues/2713). Anthropic closed it as NOT_PLANNED without responding.** The behavior is intentional.


## What's Changed Since (Timeline)

- **June 2025**: Issue #2713 filed. Confirmed by multiple users across Windows, macOS, Linux.
- **September 2025**: Anthropic [reversed their privacy-first stance](https://www.anthropic.com/news/updates-to-our-consumer-terms) — consumer data now used for training by default unless you opt out. Retention changed from 30-day auto-deletion to 5 years for users who don't opt out.
- **October 2025**: Anthropic announces "Memory" as a new premium feature — the ability for Claude to remember things across sessions. Meanwhile, Claude Code had already been silently logging every conversation, keystroke, and file path for months with no user control. They were selling a controlled version of something they were already doing without consent.
- **October 2025**: CVE-2025-59536 (CVSS 8.7) — RCE via malicious hook configuration in untrusted repos.
- **February 2026**: CVE-2026-21852 (CVSS 5.3) — API key exfiltration via malicious repository settings.
- **March 2026**: Issue #2713 still closed. Issue [#5024](https://github.com/anthropics/claude-code/issues/5024) (45+ upvotes) reports `.claude.json` growing to 90MB+, crashing MCP servers. No fix. Issue [#13797](https://github.com/anthropics/claude-code/issues/13797) documents Claude Code accidentally creating issues in the wrong public repos, exposing database schemas, Azure AD configs, and healthcare system details. Closed as stale.

The problem has gotten worse, not better.

## What Claude Code Stores (Verified March 2026)

### `~/.claude.json` (plaintext, unencrypted)

- Your **email address** in plain text
- Every **project folder path** you've ever opened
- **GitHub repo mappings** linking your username to local directories
- Feature flags and **telemetry configuration** (`tengu_*` entries)
- User ID, organization UUID, account creation date
- Referral codes, billing type, subscription dates
- Cached growth/experiment data, survey state

### `~/.claude/` directory (plaintext, unencrypted)

| Directory | What It Contains |
|-----------|-----------------|
| `projects/` | **Full conversation transcripts** — every message you sent and received, with API request IDs, token counts, model info, timestamps, tool calls and results. Stored as JSONL. |
| `projects/*/memory/` | **Persistent memory files** Claude writes about your setup — can include IP addresses, SSH configs, network topology, machine hostnames. |
| `history.jsonl` | **Every prompt you've ever typed** across all projects, with timestamps and session IDs. |
| `debug/` | Session debug logs. |
| `file-history/` | Snapshots of every file you've edited through Claude. |
| `shell-snapshots/` | Shell state captures. |
| `backups/` | Copies of `.claude.json`. |
| `statsig/` | Telemetry data. |
| `cache/` | Cached content. |
| `plans/` | Plan mode documents. |
| `todos/` | Task lists. |
| `tasks/` | Task data. |
| `paste-cache/` | Pasted content cache. |
| `telemetry/` | Additional telemetry. |

### Real examples from an actual machine

**Prompt history logging every keystroke, including typos:**
```json
{"display":"ccheck again","timestamp":1772435236894}
{"display":"it's stuck","timestamp":1772435257589}
{"display":"[casual message]","timestamp":1772437077305}
{"display":"claude --versioni","timestamp":1772436641321}
```

**Full conversation transcripts with API metadata:**
```json
{"type":"user","message":{"role":"user","content":"[sensitive financial/legal content logged verbatim]"},"sessionId":"...","timestamp":"..."}
```

**Memory files storing network infrastructure:**
```
- machine-1: [REDACTED_IP] (this machine, username)
- machine-2: [REDACTED_IP]
- PermitEmptyPasswords is currently enabled
```
Claude Code's memory system wrote a file containing Tailscale IPs, hostnames, usernames, and SSH configuration details for every machine on the network — essentially a roadmap for unauthorized access.

### Scale

- A few hours of use: ~10MB, 335 files
- Months of regular use: **1.4GB**, including 901MB of conversation logs, 426MB of debug files, 47MB of file snapshots

## The Game

Privacy Invaders is a space shooter that deletes all of the above. Press any key to launch a nuke at Claude's data planet, then watch every deleted file scroll past in the credits.

**What gets preserved:**
- `.claude/.credentials.json` — OAuth tokens (so you stay logged in)
- `.claude/settings.json` — your user preferences

**Everything else gets nuked.**

### Install

```
git clone https://github.com/phrinj/Privacy-Invaders.git
```

### Run

**Windows (CMD or PowerShell):**
```
python C:\path\to\Privacy-Invaders\privacy_invaders.py
```

**macOS / Linux:**
```
python3 /path/to/Privacy-Invaders/privacy_invaders.py
```

Run it from any directory. The splash screen will show you what Claude data exists and what's about to be deleted. Press any key to launch the nuke.

To clean a specific project's `.claude/` folder, `cd` into that project first.

### When to Run

**Only when Claude Code is idle** — not while it's thinking or processing. Running it during active use creates race conditions that can crash the session.

### Requirements

- Python 3.6+
- Windows: CMD or PowerShell (not WSL)
- macOS / Linux: any terminal

## Opt-Out Environment Variables

Claude Code also supports these environment variables to reduce (but not eliminate) data collection:

| Variable | What It Disables |
|----------|-----------------|
| `DISABLE_TELEMETRY=1` | Statsig metrics |
| `DISABLE_ERROR_REPORTING=1` | Sentry error logging |
| `DISABLE_BUG_COMMAND=1` | `/bug` command (sends full conversation to Anthropic, retained 5 years) |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` | All of the above |

**These only affect what gets sent to Anthropic's servers.** They do NOT stop the local plaintext logging that Privacy Invaders addresses.

## Other Tools

Privacy Invaders isn't the only tool addressing this:

- [CC-Cleaner](https://github.com/tk-425/CC-Cleaner) — Web GUI for browsing and cleaning Claude data (Vue.js)
- [Claude Config Editor](https://github.com/gagarinyury/claude-config-editor) — Python web tool for bulk history deletion
- [ClawCare](https://github.com/natechensan/ClawCare) — Security scanner for AI agent plugins

Privacy Invaders is the only one that makes it fun.

## FAQ

**Q: Why a game?**
A: We tried an automatic cleaner. Claude Code and the cleaner fought over files, causing race conditions and crashes. Making it manual and tying it to user input solved the problem.

**Q: Do I have to log in again after?**
A: No. OAuth credentials are preserved.

**Q: How many files get deleted?**
A: Light users: dozens. Regular users: hundreds. Power users who've never cleaned: thousands.

**Q: Will this break Claude Code?**
A: No. Claude rebuilds what it needs on next launch. Just don't run it while Claude is actively working.

## License

MIT License.

## Contributing

PRs welcome. Ideas for new animations, one-liners, or privacy features appreciated.

Built with ironic help from Claude, who seems fine helping users delete its own data collection.

---

## Support

If this helped protect your privacy:

**[Buy me a coffee](https://buymeacoffee.com/phrinj)**

[YouTube](https://youtube.com/@phrinj) | [phrinj.com](https://phrinj.com)

---
